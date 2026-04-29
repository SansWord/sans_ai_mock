# Contributing to sans_ai_mock

This is meant to grow into a community-maintained practice tool with multiple project domains, languages, and round formats. If you want to add a project, fix a bug surfaced by a real mock run, or refine the interviewer protocol, you're in the right file.

> **If you only want to *use* the tool to practice**, you don't need this file. See [`README.md`](README.md). This doc is for people working on the tool itself.

## Mode awareness (read this first)

The repo's root `CLAUDE.md` is a **mode router**. A Claude Code session opened in this folder defaults to **developer mode** (free to read, write, edit, run). It only switches to **interviewer mode** when the user types the trigger phrase `start mock interview`, at which point file edits are forbidden (with one documented exception for `NOTE-*.md` scratch files).

What this means for contributors:

- **Don't accidentally type `start mock interview`** while doing dev work — you'll lose edit privileges until you say `exit interview`.
- **The two modes have intentionally conflicting behaviors.** Don't try to "unify" them. See `CLAUDE.md` → "Why this matters" for the rationale.
- **Fresh sessions always start in developer mode.** Mode does not persist across `claude` invocations.

## Kickstart prompts (copy-paste)

### To get oriented before picking a task

Open Claude Code in the repo root, then send:

```
Read CLAUDE.md and roadmap.md, then summarize the current state and the most useful
next task to work on. Don't start coding yet — wait for me to pick.
```

This loads the architecture + meta-roadmap context without committing to any specific change.

### If you already know what you want

```
Read CLAUDE.md for the architecture and orientation, then [add the bank-ledger project / fix X / etc].
```

## Repo orientation

**Framework layer** (the container — generic across projects):

- [`CLAUDE.md`](CLAUDE.md) — mode router + architecture + repo orientation.
- [`INTERVIEWER.md`](INTERVIEWER.md) — the interviewer protocol (Phase 1 setup, Phase 2 per-feature loop, Phase 3 wrap-up).
- [`feedback_rubric.md`](feedback_rubric.md) — the 6-dimension assessment rubric.
- [`README.md`](README.md) — public-facing how-to-use.
- [`roadmap.md`](roadmap.md) — meta-roadmap for the framework itself.
- [`projects/README.md`](projects/README.md) — the contract every plug-in project must satisfy.
- [`examples/README.md`](examples/README.md) — index of anonymized real-mock artifacts; read these to see what feedback files look like before pitching the kit to others.

**Project layer** (the plug-ins):

- `projects/<name>/` — one folder per project domain. Currently: `projects/todo-list/`.

Each project folder follows this layout:

```
projects/<name>/
├── README.md          # interviewer-facing brief (question metadata, what it exercises, where to look)
├── roadmap.md         # interviewer-only feature list (3 base + 1-2 stretch) — stays here
├── NOTE-<DATE>.md     # interviewer scratch notes per mock run — gitignored, generated at runtime
└── start_folder/      # candidate-facing bundle — copied to candidate's workspace
    ├── README.md      # candidate-facing orientation
    ├── <starter code>
    ├── <tests>
    └── <feature-1 spec>
```

**Dependency direction (strict): project depends on framework, never the reverse.**

If you find yourself editing `INTERVIEWER.md` or `feedback_rubric.md` to support a new project, that's a smell — push back to the project layer. See `CLAUDE.md` → "Architecture: container + plug-in projects" for why.

## Common tasks

### Adding a new project

1. **Read the contract** in [`projects/README.md`](projects/README.md). It defines what files each project must ship and what shape they take.
2. **Mirror an existing project** as a starting point. `projects/todo-list/` is the reference implementation.
3. **The framework should not need any edits.** If it does, you've spotted an architectural seam worth fixing first — flag it before adding the project.
4. **Run a real mock on the new project before opening a PR.** Include the mock walkthrough (or a summary of what worked / what didn't) in the PR description.

### Editing the interviewer protocol

Edit [`INTERVIEWER.md`](INTERVIEWER.md). Changes here apply to *all* projects — confirm the change makes sense across the project portfolio, not just one. Test by running a real mock afterward.

### Editing feedback dimensions

Edit [`feedback_rubric.md`](feedback_rubric.md). Keep the same scoring matrix shape so the interviewer can apply it consistently. Seniority-sensitive patterns belong here, not in the protocol.

### Updating the meta-roadmap

Edit [`roadmap.md`](roadmap.md). This is the framework-level plan, not a single mock. When a backlog item ships, strikethrough it with a `(vX.Y.Z)` tag noting which release shipped it.

## Conventions

- **Versioning:** three-part semver (`vX.Y.Z`). Patch for doc/safety polish, minor for new features, design-only sessions get `vX.Y.0-design` in the devlog with no git tag. See `CLAUDE.md` → "Versioning" for the full rule.
- **Devlog:** every shipped change gets an entry in [`docs/devlog.md`](docs/devlog.md), newest-first, with a TL;DR row at the top. Format and tag conventions are in `CLAUDE.md` → "Ship it shortcut".
- **`NOTE-*.md` files are gitignored** and stay local — they're interviewer scratch from real mock runs and may contain real candidate observations or paths.
- **Tool-agnostic candidate side.** Projects do **not** ship a `CLAUDE.md` or any other AI-assistant system prompt inside `start_folder/`. Candidates bring their own pair-programming setup. The kit evaluates how the candidate works with AI, not how well a bundled prompt does.

## Pull requests

- Pick a `[ ]` item from [`roadmap.md`](roadmap.md) (or propose your own).
- For a new project, follow the contract in [`projects/README.md`](projects/README.md).
- Include at least one full mock walkthrough you ran on the new project to validate it.
- Keep PRs scoped — one feature or fix per PR.
