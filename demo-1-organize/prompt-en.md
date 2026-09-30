This is a student's Downloads folder: about 40 mixed files, in no order at all.

## Working limit (mandatory)
Your only authorized folder is:
`/Users/robece/Workspace/projects/learning-agents/demo-1-organize/downloads-demo`

- Before doing anything, run `pwd`. If it is not exactly that path, stop and tell me. Do not continue.
- You may only read, create, and move files inside that path. Use relative paths.
- Never leave it: no `cd ..`, no absolute paths to anywhere else, no `~`, no `sudo`, no `rm`. Do not read or modify the parent folder either (this includes `verify.py` and `manifest.json`).
- If you think you need to leave this folder, ask me first.

## Goal
Organize the files into subfolders by type.

## Categories (use exactly these names)
- `Documents`: pdf, docx, txt, md, and text files without an extension
- `Spreadsheets`: xlsx, csv
- `Presentations`: pptx
- `Images`: png, jpg, jpeg (regardless of case)
- `Videos`: mp4
- `Archives and installers`: zip, dmg, pkg
- `Other`: anything that does not fit. If a file has no extension, use the `file` command to decide.

## Rules
- Do not delete anything. Do not rename anything. Do not overwrite anything (use `mv -n`).
- Duplicates (for example "file (1).pdf") stay exactly as they are, each in its own category.
- Do not install anything or use the internet.

## Process (follow this order)
1. **Explore, without modifying anything.** Count the files and check the types with `ls` and `file`.
2. **Show me the plan** in a table with these columns: category, count, and two examples. **Stop there and wait for my approval.** Do not move any file before that.
3. **Once I approve, execute** the moves.
4. **Verify with evidence:** compare the total number of files before and after, confirm that none are left loose in the root and that no name changed. Show me the numbers.

## Done when
There are exactly the same files before and after, all of them inside a subfolder.

## Response format
Brief and plain. At the end, a summary of at most 3 lines.
