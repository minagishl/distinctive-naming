# Construction methods

Ways to turn material into a name. `scripts/pick_seeds.py` draws four methods per session, and using several methods keeps the shortlist from collapsing into one style.

## Contents
1. Name categories
2. Methods
3. Combining well

## 1. Name categories

Igor's four categories [24], cross-referenced with the trademark spectrum [23]:

| Category | What it is | Example | Trademark class | Note |
|---|---|---|---|---|
| Functional | Says what it does | "The Naming Company" | descriptive | Rarely stands out; weakest mark |
| Invented | A new word | Kodak, Xerox | fanciful | Strongest mark, but needs a story or spending to be remembered |
| Experiential | Names the experience of use | Safari | usually suggestive | Can drift toward stock words |
| Evocative | Points elsewhere, evokes a character | Apple, Virgin | arbitrary | Igor considers this the strongest category |

LLM output leans functional and toward smooth coinages. Push toward evocative names and invented names with a clear origin.

**A worked case: BlackBerry.** Lexicon's team noticed that the device's small keys resembled the skin of a fruit, brainstormed fruit names, and wanted a joyful name to counter the stress of work email. "Strawberry" was rejected as too slow. "BlackBerry" made a shortlist of about 40, and both B's were later capitalized because the linguists considered B a reliable sound across languages. [Quartz]

## 2. Methods

| Method | What it does | Example | Fits |
|---|---|---|---|
| Repurposed real word | An existing word from another field | Apple, Amazon, Slack | The basic evocative move |
| Metaphor | Casts the product's function as something else's | A file converter as a hermit crab that borrows shells | Brings its origin story with it |
| Compound | Joins two words | Facebook, PowerBook | Take one half from a far domain; two in-field words give "DataFlow" |
| Blend | Overlaps two words into one | (choose words that share sounds) | Where an overlap is natural |
| Truncation | Uses part of a word | (a clipped technical term) | Falls back to average if the source word is a stock word |
| Foreign real word | A real word from another language | (verify meaning first) | Check meaning and slang in target markets |
| Phrase or imperative | A short phrase | (a two- or three-word command) | Poor for typed names |
| Person or place name | A real or invented person or place | Tesla, Patagonia | Real names carry rights and connotations |
| Onomatopoeia and mimetics | A sound or a manner | Japanese giongo and gitaigo are a rich source | Good for playful briefs |
| Coinage from same-family parts | Builds a word from parts of one language family | Kodak (an invented sound) | Last resort; give it an origin |

Examples marked in parentheses are deliberately left abstract. Concrete examples in a prompt get copied, and Anthropic's guidance warns that examples can be over-learned ([Anthropic]: https://platform.claude.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices).

## 3. Combining well

- Try two or three methods on each strong piece of material. One item becomes different names through repurposing, metaphor and a foreign word.
- In a compound, if one half comes from the product's field, take the other from far away.
- Typed names (CLI, packages) suit short repurposed words and truncations. Company names suit evocative names and person or place names.
- For romanized Japanese, check spelling variants (ou / o / oh) and how the name reads to English speakers.

Numbered references point to the source list in `research-basis.md`. [Quartz]: https://qz.com/49115/rim-renames-itself-blackberry-heres-how-that-name-came-to-be/
