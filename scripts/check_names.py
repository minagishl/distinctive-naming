#!/usr/bin/env python3
"""Flag name patterns that read as generator output, are crowded, or are hard to use.

Every rule cites its basis; see references/research-basis.md for the sources.
Warnings are hints for judgment, not verdicts.

Usage:
  python3 check_names.py NAME [NAME ...]
  python3 check_names.py --corpus NAME [NAME ...]   # also compare with YC company names
"""

import argparse
import json
import os
import re
import sys
import urllib.request

# Names documented as LLM defaults: chatbot self-names (TechRadar) and repeated
# character names from 100-run tests (seehuhn.de, Hugging Face name-diversity blog).
DOCUMENTED_AI_DEFAULTS = [
    'nova', 'sol', 'atlas', 'elara', 'kira', 'voss', 'vance', 'chen', 'marcus', 'eleanor',
    'aldric', 'malachi', 'kaleb', 'turing', 'lovelace',
    # Assistant names reported as LLM favorites (usecarly.com, citing Laura Wattenberg).
    'luna', 'aria', 'sage',
]

# Frequent stems among YC companies founded 2023-26 (first word of name, yc-oss data).
CROWDED_STEMS = ['flow', 'agent', 'loop', 'deep', 'stack', 'sync', 'forge', 'pilot']

# Suffixes that are rare among real startups (<=2% of YC names in every era) but
# common in generator output; an inference, so the warning is worded softly.
GENERATOR_SUFFIXES = ['ify', 'fy', 'ly', 'io', 'ai']

YC_URL = 'https://raw.githubusercontent.com/yc-oss/api/main/companies/all.json'
CACHE = os.path.join(os.path.expanduser('~'), '.cache', 'distinctive-naming', 'yc.json')


def letters_of(name: str) -> str:
    return re.sub(r'[^a-z]', '', name.lower())


def check(name: str) -> list[str]:
    warnings = []
    lower = name.lower()
    letters = letters_of(name)

    hits = [w for w in DOCUMENTED_AI_DEFAULTS if re.search(rf'(^|[^a-z]){w}', lower)]
    if hits:
        warnings.append(f'documented LLM default: {", ".join(hits)}')

    if re.search(r'\bai\b', lower) or re.search(r'[a-z]AI\b', name):
        warnings.append('contains "AI" as a word (6.1% of YC 2023-26 names; crowded)')

    crowded = [s for s in CROWDED_STEMS if s in letters]
    if crowded:
        warnings.append(f'crowded stem in recent YC names: {", ".join(crowded)}')

    for suffix in sorted(GENERATOR_SUFFIXES, key=len, reverse=True):
        if letters.endswith(suffix) and len(letters) > len(suffix) + 2:
            warnings.append(f'-{suffix} ending: rare in real startups, common in generators')
            break

    if re.search(r'[a-z][A-Z]', name):
        cap_words = re.findall(r'[A-Z][a-z]+', name)
        if len(cap_words) >= 2 and cap_words[0][0] == cap_words[1][0]:
            warnings.append('alliterative CamelCase compound (observed chatbot default)')
        else:
            warnings.append('CamelCase compound: check both halves are not stock words')

    if re.search(r'[^aeiouy]{4,}', letters):
        warnings.append('4+ consonant cluster: may hurt pronounceability (fluency)')

    if re.search(r'[bcdfghjklmnpqstvwxz]r$', letters):
        warnings.append('dropped-vowel ending: SCRATCH "spelling challenged"')

    if len(letters) > 12:
        warnings.append(f'{len(letters)} letters: longer than 99% of YC first words')

    if re.search(r'l[aeiouy]?r|r[aeiouy]?l', letters):
        warnings.append('l and r close together: merge for Japanese listeners')

    return warnings


def load_corpus() -> list[str] | None:
    try:
        if not os.path.exists(CACHE):
            os.makedirs(os.path.dirname(CACHE), exist_ok=True)
            req = urllib.request.Request(YC_URL, headers={'User-Agent': 'distinctive-naming'})
            with urllib.request.urlopen(req, timeout=60) as res, open(CACHE, 'wb') as out:
                out.write(res.read())
        with open(CACHE, encoding='utf-8') as f:
            return [c['name'] for c in json.load(f)]
    except Exception as err:
        print(f'corpus unavailable ({err}); similarity check skipped', file=sys.stderr)
        return None


def longest_common(a: str, b: str) -> int:
    best = 0
    prev = [0] * (len(b) + 1)
    for ca in a:
        cur = [0] * (len(b) + 1)
        for j, cb in enumerate(b, 1):
            if ca == cb:
                cur[j] = prev[j - 1] + 1
                best = max(best, cur[j])
        prev = cur
    return best


def similar(name: str, corpus: list[str], limit: int = 5) -> list[str]:
    target = letters_of(name)
    if len(target) < 4:
        return []
    need = min(len(target), max(5, len(target) - 2))
    scored = []
    for other in corpus:
        o = letters_of(other.split(' ')[0])
        if not o:
            continue
        common = longest_common(target, o)
        if o == target or common >= need:
            scored.append((o != target, -common, other))
    scored.sort()
    return [s[2] for s in scored[:limit]]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('names', nargs='+')
    parser.add_argument('--corpus', action='store_true', help='compare with YC company names')
    args = parser.parse_args()

    corpus = load_corpus() if args.corpus else None
    for name in args.names:
        warnings = check(name)
        print(f'{name}: {"; ".join(warnings) if warnings else "no pattern warnings"}')
        if corpus is not None:
            near = similar(name, corpus)
            print(f'  similar YC names: {", ".join(near) if near else "none"}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
