# Source domains

How to gather material from the domains drawn by `scripts/pick_seeds.py`. The domain list itself lives in the script. Draw domains rather than choosing them, because LLMs choose the same few every time (see `research-basis.md`, section 4).

## Contents
1. Gathering material
2. What to collect, by kind of domain
3. Distance
4. Foreign and Japanese words

## 1. Gathering material

Use this prompt shape for each domain:

> List eight specific, little-known things in DOMAIN that VERB (the product's core action). Give the name of each thing and one line on how it does that.

Asking for things rather than names avoids the typical-name attractor. Then keep only items that share how the product works, not just how it looks.

## 2. What to collect, by kind of domain

| Kind of domain | Collect |
|---|---|
| Natural science (geology, weather, biology) | Named minerals, landforms, cloud types, organisms, behaviors |
| Crafts and trades | Tool and part names, process names, trade jargon |
| Food and fermentation | Process steps, utensils, folk names for microbes |
| Infrastructure (ports, rail, post) | Signals, fittings, procedures, informal terms |
| Performing arts and games | Stage machinery, roles, move names |
| Language (dialects, archaic words, onomatopoeia) | Words with a concrete image and a short sound |
| Places and heraldry | Small place names, old province names, shop names, crests |
| History of technology | Component names, obsolete instruments |

## 3. Distance

Far-field, uncommon material raises novelty, but material that is too remote lowers quality (`research-basis.md`, section 4). Aim for the middle:

- **Near:** shares the product's field. Gives safe, low-novelty names.
- **Middle:** a different field that shares the product's mechanism, for example another trade that inspects incoming goods for a product that inspects incoming code. This is the target.
- **Too far:** you can only connect it by surface features, such as color or shape. Redraw.

## 4. Foreign and Japanese words

- Real words from other languages combine meaning with low collision risk. Verify each word's meaning in a dictionary or another reliable source, and say "unverified" if you cannot.
- Search for slang or negative meanings in each target market.
- For Japanese-origin words, pick ones that are short and readable in romaji, and check how English speakers will read them.
- English /r/ and /l/ merge for Japanese listeners, so names that depend on that contrast blur in katakana. [Wikipedia]

[Wikipedia]: https://en.wikipedia.org/wiki/Perception_of_English_/r/_and_/l/_by_Japanese_speakers
