# Research basis

The evidence behind each design decision in SKILL.md. Where evidence is indirect or weak, this file says so. Bracketed numbers refer to section 10.

## Contents
1. Why LLM names converge
2. Step 1: the user's own material
3. Step 2: keeping the obvious territory in view
4. Step 3: random seeds, distance and personas
5. Step 4: drafting, revising and verbalized sampling
6. Step 6: why self-evaluation is limited
7. Name type and trademark strength
8. What real startup names look like (YC data)
9. Known limits of this design
10. Sources

## 1. Why LLM names converge

- **Typicality bias.** Human preference data rewards familiar, fluent text. When candidates tie on quality, typicality breaks the tie, so preference tuning sharpens models toward stereotypical outputs. [1]
- **Alignment trades away originality.** Base models beat their aligned versions at random number generation, mixed-strategy games and creative writing. Aligned models prefer pleasant writing over originality, and better scores on common benchmarks correlate with worse performance on these tasks. [2]
- **Instruct models skew name choice.** In next-token probabilities for a character's name, one instruct model's top 10 names took 77% of the mass, while most base models' top pick was about 4% or less. [3]
- **Claude collapses too.** Asked 100 times to name a software developer, Claude Sonnet 4.5 said "Marcus Chen" 100 times. Voss, Chen and Vance recurred across categories. [4]
- **Elara.** The name is extremely rare among humans but pervasive in AI output, and Namerology named it the 2025 Name of the Year on that basis. [5] One account attributes its appeal to smooth sounds, an -a ending and no cultural baggage. [6]
- **Models converge with each other,** more strongly than a single model repeats itself. [7] Across 20 models, output diversity fell well short of human writers, and larger models in a family were often less diverse than smaller ones. [8]
- **Self-names.** Asked to name themselves, ChatGPT chose Nova (Sol with memory enabled), and Gemini chose Atlas after being pushed. [9]
- **Practitioner observation.** A chatbot tested by a naming agency defaulted to alliterative CamelCase names and to famous computer scientists (Turing, Lovelace), and it often ignored instructions to change approach. [10]

## 2. Step 1: the user's own material

- The naming agency above argues that strong names often come from personal memories and sensory experience that the model lacks. [10] This is practitioner opinion, not a measured result.
- Writers given LLM story ideas produced stories rated more creative individually, but the stories were more similar to one another than stories written without AI. [11] Material supplied by the user is outside the shared model distribution, and it counteracts that narrowing. This is an inference from [11], not a tested intervention.

## 3. Step 2: keeping the obvious territory in view

- **Seeing earlier answers works.** In NoveltyBench, asking for a different answer while all previous answers stayed in context was the most successful strategy: three frontier models roughly matched the diversity of human writers. A "be unique" system prompt and paraphrased prompts were only marginally effective. [8]
- **Generating outside categories works.** IDEAFix compared 25 prompting strategies across 14,350 inputs. Strategies that generate ideas, group them, and then generate outside those groups, along with short brainstorming prompts carrying cues like "wild" or "unconventional", beat the controls on novelty and rarity. Complex method-based prompts (SCAMPER, Design Thinking, C-K) rarely did. [12]
- **No white-bear effect in LLMs.** Telling humans to make ideas different from their first ones slightly reduced diversity, consistent with the white-bear effect. LLMs showed no such cost, and the same instruction raised their diversity. [13]
- **Correction to an earlier version.** An earlier version of this skill told the model not to reread its first names, citing the "pink elephant" problem. That problem concerns avoiding a topic in conversation [14], not diversifying a list. The evidence in [8] and [13] points the other way, so step 2 now keeps the names in view.
- **Humans:** later ideas tend to be rated more creative than early ones (the serial order effect). [15] This is human evidence and is used only by analogy.

## 4. Step 3: random seeds, distance and personas

- **LLMs are bad samplers.** Across 11 models and 15 distributions, batch generation passed a median of 13% of tests, and independent requests almost never passed. The authors recommend external random number generators. [16] Aligned models also prefer "7" when asked for a random digit. [2]
- **Far and uncommon sources raise novelty, at a cost.** Far-field, less-common examples produced more novel design concepts than a control group; neither property alone did. Quality became more variable, and fewer ideas were produced. [17]
- **Too far hurts.** In a follow-up study, far stimuli lowered maximum novelty and quality compared with near stimuli. The authors tentatively suggest a "sweet spot" of distance. [18]
- **Ordinary personas.** LLM sessions start from a shared, central region of the knowledge space, so their first ideas are far less varied than humans' first ideas. Personas drawn from ordinary people restored that spread and beat curated "creative" personas modeled on famous founders. Combined with draft-then-revise prompting, they exceeded human diversity on the combination metric by 22%. On a newer model, the gap between ordinary and creative personas narrowed, but ordinary personas still did not fall behind. [13]

## 5. Step 4: drafting, revising and verbalized sampling

- **Draft titles, revise for distance, then elaborate.** Among 35 prompts given to GPT-4, the chain-of-thought prompt produced the most diverse ideas and the most unique ideas. It asked for short titles first, then for edits making them "bolder and more different", then for elaboration. [19] Deng et al. replicated the effect: drafting titles first limits early elaboration, which anchors later output, and the explicit revision step counters typicality. [13]
- **Verbalized Sampling** asks for k responses, each with a verbalized probability. Its tail variant requires each probability to be below a threshold. [1]
  - k = 5 is the default, and quality degrades when k is too large.
  - The "explicit" probability wording used in step 4 suited the single-shot variant best, though no wording was universally better.
  - Lowering the threshold increases diversity. Around 0.1 gave the strongest gains, and at 0.01 or below results showed diminishing returns and instability.
  - Precision falls as the threshold drops, so the best threshold depends on the task.
  - Creative-writing diversity rose 1.6 to 2.1 times over direct prompting, with no loss of quality. Gains are larger in larger models, and weaker models can lose quality.
- Step 4 combines these methods: titles, revision, then probability-filtered selection, keeping at most five per round. The combination itself has not been benchmarked. Its parts have.
- **Volume saturates.** Of 4,000 LLM-generated research ideas, only about 200 were non-duplicates. [20] So seeds and personas change between rounds instead of each round simply producing more.

## 6. Step 6: why self-evaluation is limited

- LLMs recognize their own outputs, and they rate them above other models' and humans' outputs. Self-recognition correlates linearly with this self-preference. [21]
- The best LLM judge of research ideas agreed with human reviewers 53.3% of the time, against 56.1% agreement among the experts themselves. [20]
- Selection still matters. When GPT-4 and students generated product ideas, the AI ideas varied more in quality, and most of the best ideas in the pooled set came from GPT-4. [22] Generating broadly and then filtering hard is a sound approach, but the filter should not be the model's own taste alone.

## 7. Name type and trademark strength

- **Trademark strength,** strongest to weakest: fanciful (Kodak, Xerox), arbitrary (Apple for computers, Amazon for books), suggestive (Netflix, Coppertone), descriptive, generic. Descriptive marks generally need acquired distinctiveness to register, and generic terms never register. [23]
- **Igor** calls functional names the least successful, notes that invented names need heavy spending to build recognition, and calls evocative names (Apple, Virgin) the strongest. [24]
- **Suggestive names** help early positioning but may hamper later repositioning. [25]
- **David Placek (Lexicon)** argues that asking whether a name fits the concept leads to descriptive names, and descriptive names create no advantage. [26]

## 8. What real startup names look like (YC data)

Analysis of 6,374 Y Combinator companies (yc-oss dataset [27]), first word of each name. `scripts/check_names.py --corpus` downloads the same data.

| Pattern | 2005–14 | 2015–20 | 2021–22 | 2023–26 |
|---|---|---|---|---|
| ends in -ly | 1.5% | 1.9% | 1.9% | 0.9% |
| ends in -io | 1.5% | 0.9% | 1.3% | 1.1% |
| ends in -ai | 0.3% | 1.4% | 2.2% | 1.6% |
| contains the word "AI" | 0.0% | 1.5% | 2.5% | 6.1% |

The most frequent stems in 2023–26 names were flow (25), bit (13), agent (11), deep (10) and loop (9). Nova, Atlas, Aegis and Sentinel appear 0–2 times each.

- Suffix coinages such as -ly, -ify and -io are rare among real funded startups (about 2% or less in every era). They read as "AI-like" because generators produce them so often, not because real names are full of them.
- Nova and Atlas are AI defaults [9] rather than common real names.
- "AI" as a separate word, and stems such as agent, flow and loop, are genuinely crowded now. That is copycat risk, which is distinct from sounding AI-generated.
- Name length: half of first words are 7 letters or fewer, and 99% are 12 or fewer. A vowel share of 0.6 or more occurs in 5.5% of names. The script does not flag vowel share, because the only source linking it to AI output concerns personal names [6].

## 9. Known limits of this design

- The design-creativity studies [15, 17, 18] used human participants and are applied here by analogy.
- No prompting strategy has removed homogenization across models. [12] This skill reduces convergence; it does not eliminate it.
- Verbalized probabilities are a device for noticing typicality. Their calibration for names is unmeasured.
- Most diversity studies measured product ideas, stories or research ideas, not names.
- The skill has not been benchmarked against a baseline. Paired runs, with and without the skill and across different seeds, would measure its effect.

## 10. Sources

1. Zhang et al. (2025). Verbalized Sampling: How to Mitigate Mode Collapse and Unlock LLM Diversity. https://arxiv.org/abs/2510.01171
2. West & Potts (2025). Base Models Beat Aligned Models at Randomness and Creativity. COLM 2025. https://arxiv.org/abs/2505.00047
3. Exploring Name Diversity in Modern LLMs: A Grimdark Trilogy Experiment. https://huggingface.co/blog/ChuckMcSneed/name-diversity-in-llms-experiment
4. Voss, J. AI names. https://www.seehuhn.de/blog/ai-names/
5. VICE. This is the perfect baby name, according to AI. https://www.vice.com/en/article/this-is-the-perfect-baby-name-according-to-ai/
6. Carly. AI Assistant Names: The Elara Problem. https://www.usecarly.com/blog/ai-assistant-names/
7. Jiang et al. (2025). Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond). NeurIPS 2025. https://neurips.cc/virtual/2025/poster/121421
8. Zhang et al. (2025). NoveltyBench: Evaluating Language Models for Humanlike Diversity. COLM 2025. https://arxiv.org/abs/2504.05228
9. TechRadar. Why do so many AI chatbots call themselves Nova? https://techradar.com/ai-platforms-assistants/chatgpt/why-do-so-many-ai-chatbots-call-themselves-nova-i-asked-chatgpt-claude-gemini-and-more-to-name-themselves
10. River + Wolf. Further out and deeper in: why generative AI struggles with brand naming. https://riverandwolf.com/further-out-and-deeper-in-why-generative-ai-struggles-with-brand-naming/
11. Doshi & Hauser (2024). Generative AI enhances individual creativity but reduces the collective diversity of novel content. Science Advances 10(28). https://doi.org/10.1126/sciadv.adn5290
12. Carichon et al. (2026). IDEAFix: Evaluation Framework for Creative Defixation Prompting in LLMs. https://arxiv.org/abs/2606.00875
13. Deng, Brucks & Toubia (2026). A Cognitive Framework for Idea Diversity in Large Language Models. https://arxiv.org/abs/2602.20408
14. Castricato et al. (2024). Suppressing Pink Elephants with Direct Principle Feedback. https://arxiv.org/abs/2402.07896
15. Beaty & Silvia (2012). Why do ideas get more creative across time? Psychology of Aesthetics, Creativity, and the Arts 6(4), 309–319. https://doi.org/10.1037/a0029171
16. Zhao, Du & Wang (2026). Large Language Models Are Bad Dice Players. https://arxiv.org/abs/2601.05414
17. Chan et al. (2011). On the benefits and pitfalls of analogies for innovative design. Journal of Mechanical Design 133(8). https://doi.org/10.1115/1.4004396
18. Fu et al. (2013). The Meaning of "Near" and "Far". Journal of Mechanical Design 135(2). https://doi.org/10.1115/1.4023158
19. Meincke, Mollick & Terwiesch (2024). Prompting Diverse Ideas: Increasing AI Idea Variance. https://arxiv.org/abs/2402.01727
20. Si, Yang & Hashimoto (2024). Can LLMs Generate Novel Research Ideas? https://arxiv.org/abs/2409.04109
21. Panickssery, Bowman & Feng (2024). LLM Evaluators Recognize and Favor Their Own Generations. NeurIPS 2024. https://arxiv.org/abs/2404.13076
22. Girotra, Meincke, Terwiesch & Ulrich (2023). Ideas Are Dimes A Dozen: Large Language Models For Idea Generation In Innovation. https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2023/08/LLM-Ideas-Working-Paper.pdf
23. Revision Legal. Trademark strength spectrum explained. https://revisionlegal.com/trademark/trademark-law/trademark-strength-spectrum-explained/
24. Igor. Naming guide summary. https://www.igorinternational.com/llms.txt
25. Keller, Heckler & Houston. The Effects of Brand Name Suggestiveness on Advertising Recall. MSI working paper. https://www.msi.org/working-papers/the-effects-of-brand-name-suggestiveness-on-advertising-recall/
26. Lessons from David Placek. https://www.antoinebuteau.com/lessons-from-david-placek.md
27. yc-oss/api, companies/all.json. https://github.com/yc-oss/api
