# learning-agents

Materials for a session on working with AI agents, given at the 4th Coloquio Universitario de Tecnología y Educación 2026: the slides and two live demos with reusable prompts for Claude Code.

## Slides

The deck is a single self-contained HTML file (`docs/index.html`) published with GitHub Pages: https://robece.github.io/learning-agents/

Navigate with the arrow keys or a click; `F` toggles full screen. The deck is available in Spanish (default) and English: use the ES | EN button in the top-left corner, press `L`, or open the page with `?lang=en`. The choice is remembered in the browser.

## Live demos

Two demos, each with reusable prompts to paste into Claude Code.

## Demo 1: organize a messy folder (`demo-1-organize/`)

Files:
- `create_messy_folder.py`: creates `downloads-demo/` with 40 mixed files (same files, same dates, every run). Running it again resets the folder.
- `prompt-es.md` / `prompt-en.md`: the prompt to paste, in Spanish or English.
- `verify.py`: independent check of the result (same files, same names, same content, none loose in the root).
- `manifest.json`: generated; names and hashes of the original files.

Run:
```
python3 demo-1-organize/create_messy_folder.py
cd demo-1-organize/downloads-demo
claude
```
Paste `prompt-es.md` (or `prompt-en.md`). The agent explores, shows a plan and waits for approval. Approve, let it execute, then check independently:
```
python3 ../verify.py
```
Reset between takes by running the create script again.

## Demo 2: a Doom-style game in three scenarios (`demo-2-doom/`)

Files:
- `1-prompt-es.md` / `1-prompt-en.md`: scenario 1, a 3D corridor you can walk through (raycasting). Creates `escenario-1.html` / `scenario-1.html`.
- `2-prompt-es.md` / `2-prompt-en.md`: scenario 2, adds chasing enemies, health and game over. Creates `escenario-2.html` / `scenario-2.html`.
- `3-prompt-es.md` / `3-prompt-en.md`: scenario 3, adds shooting, ammo and a victory screen. Creates `escenario-3.html` / `scenario-3.html`.
- `game/`: the only folder the agent may touch.

Each prompt is self-contained: if the previous scenario's file exists it copies and extends it; if not, it builds everything up to that scenario from scratch. So you can start at any scenario. Earlier scenarios are never modified, so you keep all three files.

Run:
```
cd demo-2-doom/game
claude
```
Paste the `1-prompt`, then the `2-prompt`, then the `3-prompt` of the language you want (`-es` for Spanish, `-en` for English). Each scenario writes its own HTML file, validates the JavaScript with `node --check` and opens it in the browser. Empty `game/` between takes (delete the files inside, keep the folder).

## Guardrails

Every prompt (Spanish and English versions) starts with a mandatory working-folder limit that names the absolute path:
- Demo 1: `/Users/robece/Workspace/projects/learning-agents/demo-1-organize/downloads-demo`
- Demo 2: `/Users/robece/Workspace/projects/learning-agents/demo-2-doom/game`

The agent must run `pwd` first and stop if it is not in that folder, keep to relative paths inside it, and never `cd ..`, use `sudo`, or touch the parent folder. Launch Claude Code from the exact folder above, or the agent will refuse to start. If you clone the repo somewhere else, replace the absolute path in each prompt with your own.

## Consistency tips

- Rehearse each demo once and time it; the countdown is 2 minutes on slide 18 (demo 1) and 4 minutes on slide 19 (demo 2).
- Start Claude Code fresh in the target folder for each take so earlier context does not change the result.
- Pick the model before the session and keep it: Sonnet for speed, Opus if you prefer higher first-try success.
- Keep a short screen recording of a good run as a backup in case the network fails.
- Requires Node (for `node --check`) and Python 3.
