# sans_ai_mock — AI-Round Mock Interview Kit

To run a mock, open Claude Code in this folder and say:

---

### `start mock interview`

---

That phrase puts Claude into interviewer mode. To exit (typically after end-of-mock feedback), say **`exit interview`**. Anything else keeps Claude in normal developer mode for maintaining this repo.

A reusable, self-contained mock for the **AI-pair-programming interview round** — the kind where you build something while collaborating with an AI coding agent, and an interviewer assesses how well you direct, push back on, and verify the agent's output.

Multiple project domains. One protocol. Honest feedback.

## Kickstart prompts (copy-paste)

### To run your first mock

Open Claude Code in the repo root, then send:

```
help me setup and start mock interview
```

The interviewer will walk you through prep (project pick, working-directory path, permission grant, second-terminal pair-programmer setup) before starting the clock. Have a second terminal ready.

Once you know the flow, drop the prefix and just send:

```
start mock interview
```

### To work on the tool itself (developer mode)

Open Claude Code in the repo root, then send:

```
Read HANDOFF.md and roadmap.md, then summarize the current state and the most useful
next task to work on. Don't start coding yet — wait for me to pick.
```

This loads context (handoff notes + meta-roadmap) without committing to any specific change. The default mode is developer mode, so Claude is free to edit files once you give direction.

If you already know what you want:

```
Read HANDOFF.md for context, then [add the bank-ledger project / fix X / etc].
```

---

## How it works

Two Claude (or compatible) sessions run in parallel:

| Role | Where it runs | How it loads |
|------|---------------|--------------|
| **Interviewer** | This repo's root | Say `start mock interview` — the root `CLAUDE.md` mode-routes to `INTERVIEWER.md` |
| **Pair programmer** | The candidate's working copy of a chosen project | Whatever AI tool the candidate chooses (Claude Code, Cursor, Copilot, Gemini CLI, etc.), with their own system prompt — or no AI assistant at all |

The interviewer picks a project (or asks you to pick), drops feature specs one at a time, observes your work between features, and gives structured feedback at the end. The pair programmer is your hands-on AI coder for the duration.

Outside of `start mock interview`, the interviewer-side Claude defaults to **developer mode** for maintaining this repo — adding projects, refining the protocol, etc.

## Quick start

1. **Clone the repo:**
   ```sh
   git clone <repo-url> sans_ai_mock
   cd sans_ai_mock
   ```

2. **Open the interviewer session:**
   ```sh
   claude
   ```

3. **Tell it to start.** First-timers — ask for setup help so the interviewer paces you through the prep before kickoff:
   ```
   help me setup and start mock interview
   ```

   On later runs, once you know the flow, just send the bare phrase:
   ```
   start mock interview
   ```

4. The interviewer will:
   - List the available projects and ask you to pick one (or say "random").
   - Tell you to copy the chosen project to a fresh working directory and `git init` it.
   - Ask for the path and permission to inspect `git diff` / files there.
   - Brief you on the workflow.
   - Start the clock and drop the first feature.

5. **In a separate terminal**, open your pair-programmer session using whatever AI tool you prefer (Claude Code, Cursor, Copilot CLI, Gemini CLI, etc.) — or skip it and code unaided. Bring your own system prompt if you have one. The kit is intentionally tool-agnostic; the mock evaluates how *you* work with AI, not how well a bundled prompt does.

   Example with Claude Code:
   ```sh
   cd ~/your-working-copy
   claude
   ```

## Repo structure

```
sans_ai_mock/
├── README.md              # this file
├── CLAUDE.md              # mode router: developer mode by default, switches to interviewer on "start mock interview"
├── INTERVIEWER.md         # interviewer protocol; loaded only when in interview mode
├── roadmap.md             # meta: roadmap for extending this tool itself
├── feedback_rubric.md     # 6-dimension assessment guide used at end of mock
├── HANDOFF.md             # notes from the initial-build session
└── projects/
    ├── README.md              # contract for adding a new project
    └── <project-name>/        # one folder per project domain
        ├── README.md          # interviewer-facing brief (metadata, what this tests, pass/fail anchor)
        ├── roadmap.md         # interviewer-only feature list (3 base + 1-2 stretch) — stays here
        ├── NOTE-<DATE>.md     # interviewer scratch notes per mock run — gitignored, generated at runtime
        └── start_folder/      # candidate-facing bundle — copied to candidate's workspace
            ├── README.md      # candidate-facing orientation
            ├── <starter code>
            ├── <tests>
            └── <feature-1 spec>
```

## Why two sessions

- **Realism.** A real AI-round interviewer watches you work but isn't your coding agent. Conflating the two roles in one session leaks the interviewer's roadmap and changes the dynamic.
- **Surprise.** Each project's `roadmap.md` (in `projects/<name>/`) is read by the interviewer but kept hidden from the candidate. Two separate sessions preserve that.

## Files the candidate should NOT peek at

If you want a real mock with surprise, **don't read these before starting**:
- `projects/<name>/roadmap.md` — the per-project feature list (base + stretch). Reading this spoils the follow-up features.
- `projects/<name>/README.md` — the **interviewer-facing** project brief. Spoils the pass/fail anchor, target seniority, and exactly what behaviors the interviewer is watching for. (Don't confuse this with `projects/<name>/start_folder/README.md`, which IS for you.)

You're free to read anytime:
- `README.md`, `CLAUDE.md` (root) — the protocol itself.
- `feedback_rubric.md` — useful to read *after* a mock to see what was being assessed.
- `roadmap.md` (root) — meta-roadmap for the tool, not a single mock.
- Each project's `start_folder/README.md` and starter code (you'll be working on these — they're the files you copy into your workspace).

## Tips for getting the most out of the mock

- **Treat it like the real thing.** Time pressure, narrate decisions, write specs first, push back on the pair programmer's bad suggestions.
- **Don't peek at the project's `roadmap.md`** — the surprise of follow-up features is the point.
- **If you used Claude Code, the interviewer can read your transcript directly.** Claude Code stores session transcripts as JSONL under `~/.claude/projects/<encoded-path>/`. The encoding roughly replaces `/` with `-` (e.g. workspace `/Users/you/scratch` → `~/.claude/projects/-Users-you-scratch/`), but additional special characters in your path may be encoded too — if the derived path doesn't match, the interviewer will list `~/.claude/projects/` and find the right entry. Since the interviewer already knows your workspace path from setup, at wrap-up time they'll just ask for permission to read that JSONL directory — no copy-paste. This unlocks deeper feedback (quoting specific prompts, identifying push-back vs. one-shot-accept patterns). With other tools or no AI, the interviewer works from observation only.
- **Use whatever AI tool you want — or none.** The pair-programmer side is intentionally not specified. Claude Code, Cursor, Copilot CLI, Gemini CLI, plain editor — your call. Bring your own system prompt if you have one.
- **Re-do mocks with different projects** as new ones are added under `projects/`. Repetition on the same project loses the surprise but still trains workflow muscle.

## Contributing

This is meant to grow into a community-maintained practice tool with multiple project domains, languages, and round formats. See `roadmap.md` (top-level) for the meta-plan, and `projects/README.md` for the contract on adding a new project.

## Status

Initial release. One project (todo-list). Honest feedback at the end. See top-level `roadmap.md` for what's coming.

## About

**Author:** SansWord (Wen-Kai Huang) — [LinkedIn](https://www.linkedin.com/in/sansword/) · [Resume](https://sansword.github.io/resume/). Currently between roles and spending the time on agentic development and Claude Code workflows; the resume covers the rest of the engineering story. Reach out if you'd like to talk about AI-pair-programming interviews, hiring assessment design, building tools with Claude Code — or if you're hiring.
