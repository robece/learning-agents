Build scenario 2 of BUNKER, a classic 90s-style shooter game: the pseudo-3D maze with a 2D map from scenario 1, plus enemies that chase you, health, and game over.

Do not ask questions: if something is not defined, pick the simplest option and keep going. Move fast, this is a demo of a few minutes. The only exception is the working limit below.

## Working limit (mandatory)
Your only authorized folder is:
`/Users/robece/Workspace/projects/learning-agents/demo-2-doom/game`

- Before doing anything, run `pwd`. If it is not exactly that path, stop and tell me.
- You may only read, create, and edit files inside that path, using relative paths.
- Never leave it: no `cd ..`, no `~`, no `/tmp`, no `sudo`, no `rm -r`. Do not touch the parent folder.
- Do not install anything or use the internet.
- Never modify or delete another scenario's file: only create this one's.

## Starting point
- If `scenario-1.html` exists in this folder, copy it to `scenario-2.html` and extend it. Do not rewrite what already works or modify the original.
- If it does not exist, create `scenario-2.html` from scratch, also including everything from scenario 1 (list below).

## Deliverable
- One new file: `scenario-2.html` (HTML + CSS + JavaScript in the same file). No libraries, images, or external audio.
- At most about 270 lines in total.
- At the top of the file, a comment with: the game idea (2 lines), "Scenario 2 of 3", the controls, and the code structure (list of sections: map, player, enemies, render, 2D map, loop).
- On screen: the title "BUNKER · Scenario 2" and one line with the controls.

## Scenario 1 (base)
1. Raycasting over a 12x12 grid map shaped like a maze (corridors, corners, and dead ends), defined in the code.
2. Walls in 3 colors, darker on the side faces and with distance. Sky and floor in different colors.
3. Movement with W and S (or the up and down arrows), turning with A and D (or the left and right arrows), with collision against the walls.
4. A `requestAnimationFrame` loop and movement independent of frames per second.
5. A 2D map on a second canvas placed below the 3D view, the same size as it (for example 560x315 each) and never on top of it. It draws the whole maze map with square cells centered, the walls in color, and the player as a dot with a line for the direction it is facing. It updates every frame.

## What scenario 2 adds (only this)
1. 4 enemies placed on the map, drawn as simple red sprites (canvas shapes, no images).
2. The sprites scale with distance and are hidden by the walls (use a z-buffer).
3. The enemies slowly move toward the player. If they touch the player, they take away health.
4. A simple health bar at the bottom of the 3D view.
5. At 0 health: the text "GAME OVER". The R key restarts.

## Process
1. A plan of at most 3 lines, then continue without waiting for a reply.
2. Write `scenario-2.html`.
3. **Verify:** extract the `<script>` content to `.check.js` inside this folder, validate it with `node --check`, fix any errors, and delete `.check.js` when finished.
4. Open the game with `open scenario-2.html`.

## Done when
You can walk without going through walls, the enemies are visible, they chase you, they take away your health, and GAME OVER appears.

## Response format
Brief. A summary of at most 2 lines.
