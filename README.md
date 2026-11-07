# Distinctive Naming Skill

An [Agent Skill](https://docs.claude.com/en/docs/claude-code/skills) that generates distinctive, human-feeling names for products, companies, OSS projects, repositories, packages, apps, features and AI assistants.

LLMs keep suggesting the same names (Nova, Atlas, Elara, CamelCase compounds, `-ly`/`-ify` coinages). Asking a model to "be more creative" barely helps. This skill replaces that with a process that does.

## How it works

The skill walks the model through a nine-step workflow:

1. Write the brief (object, use, market, personality, things to avoid)
2. Map the obvious territory, so later rounds can stay away from it
3. Draw random seeds (domains, construction methods, ordinary personas) with a script, because LLMs cannot sample at random
4. Generate in three rounds: draft titles, revise for distance, verbalize probabilities, keep the low-probability names that still have a real origin
5. Tune the sound (sound symbolism, pronounceability)
6. Filter and evaluate with `check_names.py` and the SMILE/SCRATCH criteria
7. Check collisions on npm, PyPI, crates.io, Homebrew, GitHub and domains with `check_registries.py`
8. Present a shortlist by territory, with origin, concerns and what was verified
9. Iterate on feedback with fresh seeds

The evidence behind each step is collected in [`references/research-basis.md`](references/research-basis.md).

## Install

### npx (skills CLI)

Works with Claude Code, Codex, Cursor and other agents supported by the [skills](https://github.com/vercel-labs/skills) CLI.

```bash
npx skills add minagishl/distinctive-naming
```

The CLI asks which agents to install for, and whether to install into the current project or globally.

### Manual

Copy this directory into your skills directory.

```bash
# Claude Code, available in all projects
git clone https://github.com/minagishl/distinctive-naming ~/.claude/skills/distinctive-naming

# or only for one project
git clone https://github.com/minagishl/distinctive-naming .claude/skills/distinctive-naming
```

### ChatGPT

1. Download `distinctive-naming.skill` (or `distinctive-naming.zip`) from the [latest release](https://github.com/minagishl/distinctive-naming/releases/latest).
2. Open <https://chatgpt.com/skills>.
3. Click **Add** at the top right and select the downloaded file.

The skill triggers on its own when you ask for a name, naming ideas, a rename, a brand, or when you call suggested names generic or AI-like. It replies in your language.

## Layout

```
SKILL.md                         Skill definition and workflow
references/
  research-basis.md              Research behind each step
  source-domains.md              What to collect from each kind of domain
  construction-methods.md        Ways to turn material into names
  sound-symbolism.md             Sound and personality
  evaluation.md                  SMILE/SCRATCH criteria
  ai-name-patterns.md            Patterns that read as generator output
scripts/
  pick_seeds.py                  Random domains, methods and personas
  check_names.py                 Flags generic, crowded or hard-to-use names
  check_registries.py            Registry, GitHub and domain availability
```

## Scripts

The scripts use only the Python 3 standard library. Run them from the skill's directory.

```bash
python3 scripts/pick_seeds.py
python3 scripts/pick_seeds.py --domains 1 --methods 0 --personas 0   # redraw one domain

python3 scripts/check_names.py NAME1 NAME2
python3 scripts/check_names.py --corpus NAME1 NAME2                  # also compare with YC company names

python3 scripts/check_registries.py NAME1 NAME2
python3 scripts/check_registries.py --tlds com,dev,app,io NAME
```

`check_names.py` and `check_registries.py` need network access for some checks. A result of `unknown` means unverified, not free. Trademarks are not checked: use J-PlatPat (Japan) or USPTO (US), and a registrar to confirm domains.

## License

[MIT](LICENSE)
