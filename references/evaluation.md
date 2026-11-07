# Evaluation

Criteria for cutting the shortlist to about five names, after `scripts/check_names.py`.

## SMILE: qualities of a strong name

From Alexandra Watkins, *Hello, My Name Is Awesome*. [W][E]

| Criterion | Question |
|---|---|
| Suggestive | Does it hint at the brand, without describing it? |
| Meaningful | Does it resonate with users, not just the founders? |
| Imagery | Can you picture it? Pictures aid memory. |
| Legs | Can it carry a theme: command names, feature names, a logo? |
| Emotional | Does it move people, or make them smile? |

## SCRATCH: pitfalls

| Pitfall | Question |
|---|---|
| Spelling challenged | Does it look like a typo? Was the spelling bent to fit a domain? |
| Copycat | Is it close to competitors' names or a crowded stem? (`check_names.py --corpus`) |
| Restrictive | Will it limit future growth? |
| Annoying | Does it feel forced? |
| Tame | Is it flat, descriptive or uninspired? |
| Curse of knowledge | Does it only make sense to insiders? |
| Hard to pronounce | Is the pronunciation obvious? |

## How to judge

- Ask "is it right for the brief?", not "do I like it?". [E]
- Put each name in a real sentence: a README first line, a CLI invocation, a sentence in conversation. [E]
- Do not choose by polling or majority. Group votes favor the least objectionable name. [E] Placek likewise treats polarization as a sign of strength. [P]
- Do not drop names early for domain availability. Prefixes and other TLDs usually solve it. [E]
- Discount your own enthusiasm. LLMs prefer their own outputs (`research-basis.md`, section 6).

## Sources

- [W] Watkins, A. (2014). Hello, My Name Is Awesome. Berrett-Koehler. ISBN 9781626561861. https://www.oreilly.com/library/view/hello-my-name/9781626561861/
- [E] https://www.nateliason.com/notes/hello-name-awesome
- [P] https://www.antoinebuteau.com/lessons-from-david-placek.md
