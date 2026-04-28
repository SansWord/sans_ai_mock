# Projects

This folder contains the project domains the interviewer can pick from when running a mock. Each subfolder is a self-contained project. Inside each project, **`start_folder/`** is the candidate-facing bundle — that's the only thing the candidate copies out. Everything else in the project folder (notably `roadmap.md`) is interviewer-only.

## Project layout

```
projects/<project-name>/
├── README.md                 # interviewer-facing — question metadata, what it exercises, where to look
├── roadmap.md                # interviewer-only — feature list, spoilers
├── NOTE-<YYYY-MM-DD>.md      # interviewer scratch notes per mock run (gitignored, generated at runtime)
└── start_folder/             # everything the candidate copies into their workspace
    ├── README.md             # candidate-facing orientation (first paragraph = picker description)
    ├── <starter code>
    ├── <tests>
    └── <feature-1 spec>
```

`NOTE-<YYYY-MM-DD>.md` files appear automatically when the interviewer runs a mock — they're durable observation records that survive context compaction during the round. They're gitignored (`projects/*/NOTE-*.md`) so per-mock notes stay local and don't pollute the kit's commit history. They're not part of the project contract; contributors don't author them.

There are **two READMEs per project**, deliberately:
- `projects/<name>/README.md` — interviewer-facing. Question metadata (domain, language, prerequisite knowledge), what this question exercises (which rubric dimensions it stresses, with concrete per-feature signals), and where to look. Does NOT contain interview-policy decisions — round length, target seniority, when-to-pick, and pass/fail bar live in `INTERVIEWER.md` and `feedback_rubric.md`, applied uniformly across questions.
- `projects/<name>/start_folder/README.md` — candidate-facing. Domain orientation and how to use the starter code.

## How a mock uses this folder

When the candidate says "start mock interview", the interviewer:
1. Lists the available projects (subfolders here) and shows a 1-line description of each (read from each project's `start_folder/README.md` first paragraph).
2. Asks the candidate: "Pick one, or say 'random' and I'll choose for you."
3. Reads the chosen project's `roadmap.md` (interviewer-only — stays at `projects/<name>/roadmap.md`, never copied out).
4. Tells the candidate to copy the chosen project's `start_folder/` (just the contents, not the folder itself) to their working directory.

## Contract — what every project must contain

`projects/<name>/` itself contains:

| File | Purpose | Required? |
|------|---------|-----------|
| `README.md` | Interviewer-facing project brief, **scoped to the question itself** — not interview policy. Should cover: a metadata table (domain, language, prerequisite domain knowledge), what this question exercises (which rubric dimensions it stresses, with concrete per-feature signals), and where to look. Does NOT cover round length, target seniority, when-to-pick, or pass/fail bar — those are interviewer-protocol concerns owned by `INTERVIEWER.md` and `feedback_rubric.md`, applied uniformly across questions. | ✅ |
| `roadmap.md` | Interviewer-only feature list. 3 base + 1-2 stretch features, each with a `### Spec` block ready to copy and a "what to look for" note. Includes per-feature time estimates (a property of the question). Lives outside `start_folder/` so the candidate never sees it. | ✅ |
| `start_folder/` | The candidate-facing bundle (see below). | ✅ |

`projects/<name>/start_folder/` contains:

| File | Purpose | Required? |
|------|---------|-----------|
| `README.md` | Candidate-facing orientation: domain context, current state, how to use the project. First paragraph = 1-line description for the picker. | ✅ |
| Starter code | Working baseline — at least one source file with a minimal feature implemented. | ✅ |
| Tests | Test file(s) covering the baseline. Should pass on a fresh checkout. | ✅ |
| First-feature spec | A markdown file (e.g., `<topic>_feature.md`) with the spec for Feature 1, so the candidate has something to work on without the interviewer doing anything yet. | ✅ |

> **Note on AI tooling:** projects do **not** ship a `CLAUDE.md` (or any other AI-assistant system prompt) inside `start_folder/`. The candidate brings their own pair-programming setup — Claude Code with their own `CLAUDE.md`, Cursor, Copilot, Gemini CLI, or no AI assistant at all. Keeping projects tool-agnostic is intentional: the mock evaluates how the candidate works with AI, not how well our prompt does.

## Contract — naming conventions

- Folder name: kebab-case (`url-shortener`, not `url_shortener` or `URLShortener`)
- Folder name describes the **domain**, not the language (`bank-ledger`, not `bank-ledger-python`)
- If you add a multi-language version, use a `-<lang>` suffix (`bank-ledger-go`)

## Contract — `roadmap.md` shape

Each feature block in a project's `roadmap.md` should have:

```markdown
## Feature N — <name> (BASE | STRETCH, ~<time> min)

### Spec

\`\`\`markdown
<the full markdown spec the interviewer copies to the candidate, ready to paste>
\`\`\`

### What to look for

- <bullet about AI-pairing skill this feature exercises>
- <bullet about edge case the candidate should catch>
- ...
```

The `### Spec` block is the only thing the candidate sees. The "what to look for" section is the interviewer's cheat sheet — never share it.

## Contract — feature progression

- **3 base features** that must complete for "Pass"
- **1-2 stretch features** that the interviewer drops only if time allows
- Features should build on each other (each preserves previous behavior) so the codebase grows naturally
- Difficulty should curve: F1 simple, F2 modest mutation, F3 introduces a new dimension (persistence, schema, etc.), stretch goals push refactoring or harder design

## Adding a new project

1. Create `projects/<your-domain>/` with the layout above (`roadmap.md` outside, candidate files inside `start_folder/`).
2. Test it yourself: copy `start_folder/` contents to a fresh working dir, run a full mock as the interviewer, and walk through all features as the candidate.
3. Update `roadmap.md` (top-level) — check off your project under "additional projects".
4. Open a PR.

## Available projects

(The interviewer auto-detects what's here, so this list is informational.)

- **todo-list** — In-memory todo list library. Tests basic API design, persistence, refactoring.
