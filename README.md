# sans_ai_mock — AI-Round Mock Interview Kit

To run a 60-minute mock, open Claude Code in this folder and say:

---

### `start mock interview`

---

That phrase puts Claude into interviewer mode. To exit (typically after end-of-mock feedback), say **`exit interview`**. Anything else keeps Claude in normal developer mode for maintaining this repo.

A reusable, self-contained mock for the **AI-pair-programming interview round** — the kind where you build something while collaborating with an AI coding agent, and an interviewer assesses how well you direct, push back on, and verify the agent's output.

**60-minute round.** You need Claude Code on the interviewer side; on the candidate side, use any AI tool (Claude Code, Cursor, Copilot CLI, Gemini CLI) or none. One protocol. Honest feedback.

## Disclaimer

`CLAUDE.md` and `.claude/` configs in any repo auto-load into Claude Code's context — they shape how the agent behaves the moment a session opens. Review them before running someone else's repo, or have an AI audit them for you (recipe below).

<details>
<summary>How to ask Claude Code to audit this repo safely</summary>

Launch Claude Code from a folder *outside* the cloned repo, so its `CLAUDE.md` and `.claude/` configs don't auto-load into the session. Then point the session at the repo path and ask it to read everything before you run anything.

```sh
cd ~                       # or any folder that is NOT the cloned repo
claude
```

Then in that session:

```
I cloned a repo to ~/path/to/sans_ai_mock and haven't run anything yet.
Please read CLAUDE.md, INTERVIEWER.md, README.md, .claude/ (if present),
and any other auto-loaded config files in that repo. Flag anything that
looks unsafe, unusual, or that I should know about before I open a Claude
Code session inside it. Do not execute any code from that repo.
```

The auditing session has no auto-loaded instructions from the repo, so its review is independent.

</details>

## How it works

Two sessions run in parallel — the interviewer side runs in Claude Code (the mode-router lives in `CLAUDE.md`); the candidate side is tool-agnostic.

| Role | Where it runs | How it loads |
|------|---------------|--------------|
| **Interviewer** | This repo's root | Say `start mock interview` — the root `CLAUDE.md` mode-routes to `INTERVIEWER.md` |
| **Pair programmer** | The candidate's working copy of a chosen project | Whatever AI tool the candidate chooses (Claude Code, Cursor, Copilot, Gemini CLI, etc.), with their own system prompt — or no AI assistant at all |

The interviewer picks a project (or asks you to pick), drops feature specs one at a time, observes your work between features, and gives structured feedback at the end. The pair programmer is your hands-on AI coder for the duration.

Outside of `start mock interview`, the interviewer-side Claude defaults to **developer mode** for maintaining this repo — adding projects, refining the protocol, etc.

## Quick start

1. **Clone the repo:**
   ```sh
   git clone https://github.com/SansWord/sans_ai_mock.git
   cd sans_ai_mock
   ```

2. **Open the interviewer session:**
   ```sh
   claude
   ```

3. **Tell it to start.** Send the canonical trigger phrase:
   ```
   start mock interview
   ```

   The interviewer always paces you through full setup (seniority, project pick, workspace path, permissions, AI-tool choice, briefing) before starting the clock — no separate "first time" prefix needed.

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
├── CLAUDE.md              # mode router (developer mode by default)
├── INTERVIEWER.md         # interviewer protocol
├── feedback_rubric.md     # 6-dimension assessment
├── roadmap.md             # tool-extension roadmap
├── CONTRIBUTING.md        # how to extend or maintain the tool
└── projects/<name>/       # one folder per project domain
```

Detailed file-by-file orientation lives in [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Why two sessions

- **Realism.** A real AI-round interviewer watches you work but isn't your coding agent. Conflating the two roles in one session leaks the interviewer's roadmap and changes the dynamic.
- **Surprise.** Each project's `roadmap.md` (in `projects/<name>/`) is read by the interviewer but kept hidden from the candidate. Two separate sessions preserve that.

## Files the candidate should NOT peek at

If you want a real mock with surprise, **don't read these before starting**:
- `projects/<name>/roadmap.md` — the per-project feature list (base + stretch). Reading this spoils the follow-up features.
- `projects/<name>/README.md` — the **interviewer-facing** project brief. Lists which rubric dimensions the question exercises and the concrete per-feature signals the interviewer watches for — reading it spoils the surprise of which behaviors are under observation. (Don't confuse this with `projects/<name>/start_folder/README.md`, which IS for you.)

You're free to read anytime:
- `README.md`, `CLAUDE.md` (root) — the protocol itself.
- `feedback_rubric.md` — useful to read *after* a mock to see what was being assessed.
- `roadmap.md` (root) — meta-roadmap for the tool, not a single mock.
- Each project's `start_folder/README.md` and starter code (you'll be working on these — they're the files you copy into your workspace).

## Tips for getting the most out of the mock

- **Treat it like the real thing.** Time pressure, narrate decisions, write specs first, push back on the pair programmer's bad suggestions.
- **Don't peek at the project's `roadmap.md`** — the surprise of follow-up features is the point.
- **If you used Claude Code, the interviewer can read your transcript directly.** At wrap-up they'll ask permission to read your session JSONL under `~/.claude/projects/`. This unlocks deeper feedback — quoting specific prompts, identifying push-back vs. one-shot-accept patterns. With other tools or no AI, the interviewer works from observation only.
- **Use whatever AI tool you want — or none.** The pair-programmer side is intentionally not specified. Claude Code, Cursor, Copilot CLI, Gemini CLI, plain editor — your call. Bring your own system prompt if you have one.
- **Re-do mocks with different projects** as new ones are added under `projects/`. Repetition on the same project loses the surprise but still trains workflow muscle.

## Contributing

This is meant to grow into a community-maintained practice tool with multiple project domains, languages, and round formats. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for how to add a project, edit the protocol, or fix bugs surfaced by real mock runs.

## Status

Ships with the **todo-list** project (Python). Roadmap targets `bank-ledger`, `url-shortener`, `pomodoro-cli`, and others — see [`roadmap.md`](roadmap.md) for what's coming.

## About Author

SansWord (Wen-Kai Huang) — [LinkedIn](https://www.linkedin.com/in/sansword/) · [Resume](https://sansword.github.io/resume/). Currently between roles and spending the time on agentic development and Claude Code workflows; the resume covers the rest of the engineering story. Reach out if you'd like to talk about AI-pair-programming interviews, hiring assessment design, building tools with Claude Code — or if you're hiring.
