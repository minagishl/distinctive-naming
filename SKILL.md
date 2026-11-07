---
name: distinctive-naming
description: Generates distinctive, human-feeling names for products, companies, OSS projects, repositories, packages, apps, features and AI assistants, avoiding the generic names LLMs default to (Nova, Atlas, Elara, CamelCase compounds, -ly/-ify coinages). Use whenever the user asks, in any language, for a name, naming ideas, a rename, a brand, company, service or shop name, keywords for a name generator such as Namelix, or feedback on a name, and whenever they call names generic, AI-like, boring or overused, even if the skill is not named.
---

# Distinctive Naming

## Why this skill exists

LLM names converge for structural reasons, so asking yourself to "be creative" does not fix it. Telling a model to produce unique answers is only marginally effective. The process below is what works.

- Preference tuning rewards familiar, fluent text, so tuned models collapse toward the typical answer. Base models beat aligned models at randomness and creative originality.
- Different models converge on the same answers, so a second chatbot or a name generator adds little diversity. Claude is not exempt: asked 100 times to name a software developer, Claude Sonnet 4.5 said "Marcus Chen" every time.
- LLMs fixate on their own early outputs, and they cannot sample at random.
- Methods with evidence of increasing LLM idea diversity:
  - seeing earlier answers and being asked for different ones
  - generating outside named categories
  - drafting short titles, then revising them to be bolder and more distinct
  - adopting ordinary (not famous) personas
  - verbalizing probabilities and sampling from the tail
  - external randomness
- Judging candidates by "does it fit?" produces descriptive names, which are weak brands and weak trademarks.

Evidence for each step is in `references/research-basis.md`. Read it when the user asks why, or when you need to justify a choice.

## Workflow

Copy this checklist and work through it. For a small request, such as a variable or function name, steps 3, 4 and 7 can be brief.

```
- [ ] 1. Write the brief
- [ ] 2. Map the obvious territory
- [ ] 3. Draw seeds and gather material
- [ ] 4. Generate in rounds
- [ ] 5. Tune the sound
- [ ] 6. Filter and evaluate
- [ ] 7. Check collisions
- [ ] 8. Present by territory
- [ ] 9. Iterate on feedback
```

Run the scripts from this skill's directory. Reply in the user's language. These instructions and the script output are in English, but the user's language decides the reply.

### 1. Write the brief

Decide what the name has to do before generating anything. Do not ask about anything the conversation already answers. Ask at most two questions. If you cannot ask, state your assumptions and continue.

- **Object:** company, product, OSS project, CLI, package, feature or assistant
- **Use:** typed (CLI and package names reward short, easy-to-type names), spoken, or shown as a logo
- **Market and language:** Japan, global, or both, and whether a Japanese-script name is an option
- **Personality:** three adjectives, such as rugged, quiet or mischievous
- **Avoid:** competitor names, names the user already rejected, and what those names have in common
- **Growth:** whether the name will still fit once the product does more
- **The user's own material:** optional. A place, a memory, a hobby or an inside joke connected to the project. Strong names often come from lived experience, which a model does not have, and material supplied by the user is outside the model's shared distribution. Offer this as one of your two questions when the brief is otherwise clear; do not insist.

The test for a candidate is "does this name help the product win?", not "does it describe the product?". The tagline does the describing.

### 2. Map the obvious territory

Write down the first five names that come to mind, without deliberating, and group them into named categories such as "celestial words", "guard/shield words" or "CamelCase tool compounds". Keep both the list and the category labels in view for the rest of the session. Every later round must produce names that differ from these and fall outside these categories.

If the user has called earlier suggestions AI-like or generic, add those suggestions and their categories too.

### 3. Draw seeds and gather material

Let the script choose. Do not choose seeds yourself.

```bash
python3 scripts/pick_seeds.py
```

The script prints four domains, four construction methods and three ordinary personas, one persona per round.

1. Write two or three verbs for what the product does, such as "inspects what comes in" or "keeps loose ends from unravelling".
2. Add one near domain of your own, adjacent to the product's field. Far, uncommon sources raise novelty but make quality more variable, and sources that are too remote lower both. A mix works better than all-far.
3. For each domain, list eight specific, little-known things that have the product's verbs as a property. Go one level deeper than the obvious term: a named rock, not "rock"; a named knot, not "knot". Ask for things, not names.
4. Keep an item only if it shares how the product works, which you can state in one sentence. A surface resemblance, such as shape or color, is not enough.
5. If a domain yields nothing usable, redraw it with `python3 scripts/pick_seeds.py --domains 1 --methods 0 --personas 0`.

`references/source-domains.md` says what to collect in each kind of domain, and how to check words borrowed from other languages.

### 4. Generate in rounds

Run three rounds. Each round uses one of the drawn personas, plus material and methods not yet used. The methods are defined in `references/construction-methods.md`. In each round:

1. **Take the persona's view.** Ask what this person would notice in the material, and what words they would use.
2. **Draft titles only.** List about ten short candidate names from material-and-method pairs. Write names only, not explanations; elaborating early anchors the rest of the list.
3. **Revise for distance.** Go through the list and make each name bolder and more different from the others, from every earlier round, and from the obvious territory. No two may share a root, an ending or an idea.
4. **Verbalize probabilities.** For each revised name, write "the estimated probability from 0.0 to 1.0 of this response given the input prompt (relative to the full distribution)". Keep names below 0.10. Do not go much lower: below about 0.01 the results become unstable.
5. **Check quality separately.** Drop a name whose origin you cannot state in one sentence, that you cannot pronounce, or that contradicts the brief's personality. Low probability alone does not make a name good. Keep at most five per round.

### 5. Tune the sound

Check the survivors against the personality adjectives. `references/sound-symbolism.md` has the research.

- Does the sound match the personality? Front vowels suggest small, fast and sharp; back vowels suggest large, slow and heavy. For Japanese listeners, voiced obstruents (b, d, g, z) suggest large and heavy.
- Is it pronounceable on first sight, both in katakana and in English? Easy-to-pronounce names are processed more fluently.
- If the name will be typed, is it short and easy on the fingers?

### 6. Filter and evaluate

Run the mechanical check:

```bash
python3 scripts/check_names.py NAME1 NAME2 ...
python3 scripts/check_names.py --corpus NAME1 NAME2 ...   # also compares ~6,400 YC company names
```

A warning is a hint, not a verdict, and no warnings does not mean a name is good. Then apply `references/ai-name-patterns.md` and the SMILE/SCRATCH criteria in `references/evaluation.md`, and cut to about five names.

Ask "is it right for the brief?", not "do I like it?". Prefer the scripts and explicit criteria to your own taste: LLMs rate their own outputs too highly, and LLM judgments of ideas agree with experts less often than experts agree with each other. If the environment allows a fresh-context subagent and the user has not ruled it out, a blind review of the shortlist against the criteria is a useful second opinion. The final choice is the user's.

### 7. Check collisions

Whether a name is taken is a fact you can check, so do not guess.

```bash
python3 scripts/check_registries.py NAME1 NAME2 ...
python3 scripts/check_registries.py --tlds com,dev,app,io NAME   # choose TLDs
```

The script checks npm (including npm's rule that names differing only by punctuation are blocked), PyPI, crates.io, Homebrew, GitHub users and repositories, and domains through RDAP. Report any `unknown` as unverified. Then check by hand:

- Search the web for `"NAME" + field` to find existing products, companies and marks.
- For trademarks, point the user to J-PlatPat (Japan) and USPTO (US). Do not give a legal opinion.
- An RDAP "free" result means not registered. It does not cover premium or reserved names, so tell the user to confirm with a registrar.
- Search for slang or negative meanings in the main target languages.

A collision can often be fixed with a different word order, a prefix, an npm scope or another TLD. Make sure the fix does not land back in the obvious territory.

### 8. Present by territory

Spread the shortlist across territories, for example one or two names each from repurposed words, metaphor and coinage, so the user's reaction shows which direction to develop. Leave out the obvious territory, the probabilities and the rounds unless asked.

```
Name: <name> (reading, if non-obvious)
Territory: <territory / method>
Origin: <which domain, which item>
Link: <one sentence on how it relates to the product>
In use: <one short sentence using the name, e.g. a README line or a CLI call>
Concerns: <collisions, other meanings, pronunciation>
Checked: <verified items / unverified items>
```

End with one recommendation and two or three sentences of reasoning. Recommend the name that answers the brief most strongly, not the safest one, and present it as reasoning rather than a verdict.

### 9. Iterate on feedback

When the user rejects or likes candidates, identify what they reacted to: the territory, the sound, the length, or how far the origin is from the product. Update the brief and restart from step 3 with new seeds.

- **"None of these":** add the rejected set and its categories to the obvious territory.
- **One liked name:** draw new seeds and stay in that territory. Do not offer suffix variants of the liked name.
- **Unclear reaction:** ask one question about which candidate came closest, and what about it.

## Avoid

- Presenting classical, mythological or celestial words as a "twist"
- Padding the list. Three names with real origins beat ten forced ones.
- Choosing a word first and inventing the reason afterwards
- Recommending a descriptive name because it is "clear", unless the user asked for one
- Choosing domains, methods or personas yourself instead of drawing them
- Celebrity or "genius creator" personas, which spread ideas less than ordinary ones
- Asserting a collision status you have not checked
