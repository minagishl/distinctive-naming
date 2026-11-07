# Name patterns to filter

Used at step 6 to filter candidates. Each row states what evidence supports it. A match is a reason to look harder, not an automatic rejection. Bracketed numbers refer to the sources in `research-basis.md`.

## Contents
1. Patterns
2. Exclusion checklist

## 1. Patterns

| Pattern | Examples | Evidence |
|---|---|---|
| AI self-names and default character names | Nova, Sol, Atlas, Elara; Marcus Chen, Kira Voss, Eleanor | Chatbot self-naming tests [9], 100-run counts [4], next-token skew [3], Namerology's "Name of the Year" [5] |
| Smooth, -a-ending assistant names with no cultural baggage | Luna, Aria, Sage, Elara | Reported for assistant and person names [6]. This is a secondary source citing a naming expert. |
| Alliterative CamelCase compounds | DataDrive, CogniCore | Observed as a chatbot default by a naming agency [10] |
| Famous-scientist mash-ups | TuringWave, LovelaceLabs | Same source [10] |
| Crowded real-world stems | flow, agent, loop, bit, deep, "AI" as a separate word | Most frequent in YC 2023–26 names (`research-basis.md` section 8). This is copycat risk rather than an AI tell. |
| Suffix coinages | -ly, -ify, -io, -ai | Rare among real startups (≤2%), so they read as generator output. This is an inference from the YC data. |
| Purely descriptive names | DepScanner, MeetingNotes | Weakest trademark class, and no competitive edge [23][26] |
| Misspellings for domain availability | vowel-dropped names | SCRATCH "spelling challenged": they look like typos (`evaluation.md`) |

## 2. Exclusion checklist

1. **Obvious territory.** Is it one of the step 2 names, or inside one of its categories? If so, drop it.
2. **Probability.** Is its verbalized probability 0.10 or higher? If so, drop it.
3. **Stock words.** Is it an industry stock word used as-is or lightly modified? If so, drop it, unless the brief asks for plainness.
4. **Origin.** Can you state its origin in one sentence? If not, it is decoration, so drop it.
5. **Pattern matches.** Does it match two or more rows in the table above? Keep it only with a strong reason.
6. **Sound and spelling.** Say it aloud. Is the spelling obvious from the sound, and the sound obvious from the spelling?
