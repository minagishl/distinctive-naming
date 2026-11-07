#!/usr/bin/env python3
"""Check whether names are taken on package registries, GitHub and domain registries.

Usage:
  python3 check_registries.py NAME [NAME ...]
  python3 check_registries.py --tlds com,dev,app,io NAME ...

Every result is "taken", "free" or "unknown". Report "unknown" as unverified.
Trademarks are not checked here.

Notes on rules this script encodes:
- npm rejects a new package whose name equals an existing one once punctuation (. - _)
  is removed, e.g. reactnative vs react-native (npm blog, "New package moniker rules").
- PyPI treats runs of -, _ and . as equivalent (PEP 503 normalization).
- Domains use RDAP via rdap.org. A 404 is trusted only when rdap.org redirected to the
  registry's own RDAP server; some TLDs (e.g. .io, .jp) have no RDAP service there, and
  rdap.org then answers 404 even for registered domains.
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

HEADERS = {'User-Agent': 'distinctive-naming-check'}


def fetch(url: str) -> tuple[int | None, str, bytes]:
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as res:
            return res.status, res.geturl(), res.read()
    except urllib.error.HTTPError as err:
        return err.code, err.geturl() or url, b''
    except Exception:
        return None, url, b''


def by_status(url: str) -> str:
    code, _, _ = fetch(url)
    if code == 200:
        return 'taken'
    if code == 404:
        return 'free'
    return f'unknown (status {code})'


def strip_punct(name: str) -> str:
    return re.sub(r'[._-]', '', name.lower())


def npm(name: str) -> str:
    exact = by_status(f'https://registry.npmjs.org/{urllib.parse.quote(name)}')
    query = urllib.parse.quote(name)
    code, _, body = fetch(f'https://registry.npmjs.org/-/v1/search?text={query}&size=50')
    if code != 200:
        return f'{exact}; similarity rule unchecked'
    names = [o['package']['name'] for o in json.loads(body).get('objects', [])]
    clashes = [n for n in names if n != name and strip_punct(n) == strip_punct(name)]
    if clashes:
        return f'{exact}; blocked by punctuation rule (clashes with {", ".join(clashes)})'
    return exact


def pypi(name: str) -> str:
    normalized = re.sub(r'[-_.]+', '-', name.lower())
    return by_status(f'https://pypi.org/pypi/{urllib.parse.quote(normalized)}/json')


def github_repos(name: str) -> str:
    query = urllib.parse.quote(f'{name} in:name')
    code, _, body = fetch(f'https://api.github.com/search/repositories?q={query}&per_page=100')
    if code != 200:
        return f'unknown (status {code})'
    exact = [i for i in json.loads(body).get('items', []) if i['name'].lower() == name]
    if not exact:
        return 'no repo with this exact name'
    top = max(exact, key=lambda i: i['stargazers_count'])
    return f'{len(exact)} exact repo(s); top {top["full_name"]} ({top["stargazers_count"]} stars)'


def domain(fqdn: str) -> str:
    code, final_url, _ = fetch(f'https://rdap.org/domain/{fqdn}')
    via_registry = urllib.parse.urlparse(final_url).netloc not in ('', 'rdap.org')
    if code == 200:
        return 'taken'
    if code == 404 and via_registry:
        return 'free (not registered per registry RDAP; confirm at a registrar)'
    if code == 404:
        return 'unknown (no RDAP service for this TLD; check a registrar)'
    return f'unknown (status {code})'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('names', nargs='+')
    parser.add_argument('--tlds', default='com,dev,app', help='comma-separated TLDs')
    args = parser.parse_args()

    for name in args.names:
        slug = name.lower()
        label = re.sub(r'[^a-z0-9-]', '', slug)
        print(f'{name}:')
        print(f'  npm:       {npm(slug)}')
        print(f'  pypi:      {pypi(slug)}')
        print(f'  crates:    {by_status(f"https://crates.io/api/v1/crates/{label}")}')
        print(f'  homebrew:  {by_status(f"https://formulae.brew.sh/api/formula/{label}.json")}')
        print(f'  gh user:   {by_status(f"https://api.github.com/users/{label}")}')
        print(f'  gh repos:  {github_repos(slug)}')
        for tld in [t.strip() for t in args.tlds.split(',') if t.strip()]:
            print(f'  .{tld:<8} {domain(f"{label}.{tld}")}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
