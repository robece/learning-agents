Build scenario 3 of BUNKER, a classic 90s-style shooter game: the maze with a 2D map and enemies from scenarios 1 and 2, plus shooting, ammo, and a victory condition.

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
- If `scenario-2.html` exists in this folder, copy it to `scenario-3.html` and extend it. Do not rewrite what already works or modify the original.
- If it does not exist, create `scenario-3.html` from scratch, also including everything from scenarios 1 and 2 (lists below).

## Deliverable
- One new file: `scenario-3.html` (HTML + CSS + JavaScript in the same file). No libraries, images, or external audio.
- At most about 360 lines in total.
- At the top of the file, a comment with: the game idea (2 lines), "Scenario 3 of 3", the controls, and the code structure (list of sections: map, player, enemies, shooting, render, 2D map, loop).
- On screen: the title "BUNKER · Scenario 3" and one line with the controls.

## Scenario 1 (base)
1. Raycasting over a 12x12 grid map shaped like a maze (corridors, corners, and dead ends), defined in the code.
2. Walls in 3 colors, darker on the side faces and with distance. Sky and floor in different colors.
3. Movement with W and S (or the up and down arrows), turning with A and D (or the left and right arrows), with collision against the walls.
4. A `requestAnimationFrame` loop and movement independent of frames per second.
5. A 2D map on a second canvas placed below the 3D view, the same size as it (for example 560x315 each) and never on top of it. It draws the whole maze map with square cells centered, the walls in color, and the player as a dot with a line for the direction it is facing. It updates every frame.

## Scenario 2 (enemies)
1. 4 enemies placed on the map, drawn as simple red sprites (canvas shapes, no images).
2. The sprites scale with distance and are hidden by the walls (use a z-buffer).
3. The enemies slowly move toward the player. If they touch the player, they take away health.
4. A simple health bar at the bottom of the 3D view. At 0 health: the text "GAME OVER".

## What scenario 3 adds (only this)
1. A crosshair at the center of the screen.
2. Shooting with the space bar or a click: it eliminates the enemy at the center of the crosshair that is not hidden by a wall.
3. A simple weapon at the bottom, with a brief flash when firing.
4. Ammo limited to 20, with an on-screen counter along with the enemies remaining.
5. When all the enemies are eliminated: the text "VICTORY". The R key restarts (also after GAME OVER).

## Process
1. A plan of at most 3 lines, then continue without waiting for a reply.
2. Write `scenario-3.html`.
3. **Verify:** extract the `<script>` content to `.check.js` inside this folder, validate it with `node --check`, fix any errors, and delete `.check.js` when finished.
4. Open the game with `open scenario-3.html`.

## Done when
You can walk around, the enemies chase you, you can shoot and eliminate them, and GAME OVER or VICTORY appears as appropriate.

## Response format
Brief. At the end: the controls in 2 lines and 3 ideas to improve it.
