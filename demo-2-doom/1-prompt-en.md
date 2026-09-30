Build scenario 1 of BUNKER, a classic 90s-style shooter game: a pseudo-3D maze (raycasting) you can walk through, with a 2D map below it. This is the base; scenarios 2 and 3 will come later.

Do not ask questions: if something is not defined, pick the simplest option and keep going. Move fast, this is a demo of a few minutes. The only exception is the working limit below.

## Working limit (mandatory)
Your only authorized folder is:
`/Users/robece/Workspace/projects/learning-agents/demo-2-doom/game`

- Before doing anything, run `pwd`. If it is not exactly that path, stop and tell me.
- You may only read, create, and edit files inside that path, using relative paths.
- Never leave it: no `cd ..`, no `~`, no `/tmp`, no `sudo`, no `rm -r`. Do not touch the parent folder.
- Do not install anything or use the internet.
- Never modify or delete another scenario's file: only create this one's.

## Deliverable
- One new file: `scenario-1.html` (HTML + CSS + JavaScript in the same file). No libraries, images, or external audio.
- At most about 190 lines.
- At the top of the file, a comment with: the game idea (2 lines), "Scenario 1 of 3", the controls, and the code structure (list of sections: map, player, render, 2D map, loop).
- On screen: the title "BUNKER · Scenario 1" and one line with the controls.

## What it must have (only this)
1. Raycasting over a 12x12 grid map shaped like a maze (corridors, corners, and dead ends), defined in the code.
2. Walls in 3 colors, darker on the side faces and with distance. Sky and floor in different colors.
3. Movement with W and S (or the up and down arrows), turning with A and D (or the left and right arrows), with collision against the walls.
4. A `requestAnimationFrame` loop and movement independent of frames per second.
5. A 2D map on a second canvas placed below the 3D view, the same size as it (for example 560x315 each) and never on top of it. It draws the whole maze map with square cells centered, the walls in color, and the player as a dot with a line for the direction it is facing. It updates every frame.

## Process
1. A plan of at most 3 lines, then continue without waiting for a reply.
2. Write `scenario-1.html`.
3. **Verify:** extract the `<script>` content to `.check.js` inside this folder, validate it with `node --check`, fix any errors, and delete `.check.js` when finished.
4. Open the game with `open scenario-1.html`.

## Done when
The file opens in the browser, you can walk around without going through the walls, and the 2D map below shows the player moving.

## Response format
Brief. At the end: the controls in 2 lines.
