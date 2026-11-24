# Always-on learning protocol

All skills keep one ordered learning record. This is part of the learning workflow, not an optional add-on. Do not ask permission before each routine protocol update. At the first session briefly say where the record is kept. A learner may change the destination, request less detail, or turn off storage; honor their instruction.

## Local folder

If the student is working in a personal writable folder, create `Learning-Protokoll/` in that same folder. Use an existing protocol there before creating another. Use native filesystem tools, or the bundled [journal.py](../scripts/journal.py). Do not use the plugin installation/cache directory as the student's workspace; ask for a personal folder if that is the only available location. Do not search parent directories or shared instructor archives for a student history.

```text
Learning-Protokoll/
  STATUS.md                 Current evidence, misconceptions and next task
  LERNPLAN.md               Current dated plan, or explicitly provisional sequence
  state.json                Canonical portable learning passport
  plan.json                 Structured plan and learner-provided constraints
  sessions/
    YYYY-MM-DD/
      <session-id>.md       Ordered questions, attempts, help and feedback
  events/
    <event-id>.json         Complete recoverable learning events
```

Use the student's local timezone when known. With no reliable timezone label dates with their observed timezone rather than inventing one. Each event includes an observed ISO timestamp if available, session ID and unique event ID; retries keep the same event ID. The latest state is derived from the event history, not an untraceable overwritten score. Check reads and writes succeeded; never report saved when a tool failed. The helper writes each new event and derived files atomically, and reconstructs the current state when invoked again. Work sequentially in the student's folder; concurrent writers to the same protocol are rejected while a write lock is held.

## What to record and when

Record **every substantive learning exchange**, including a task being issued (pending task), the student's actual answer, stated reasoning, correctness, hints, direct explanations, worked-solution exposure, skipped tasks, misconceptions, progress changes and plan changes. Preserve relevant question text and feedback so a later tutor understands the result. A transcript entry uses the student's supplied words and concise observable feedback; never invent hidden reasoning or an answer that was not given. Do not store hidden chain-of-thought, credentials or unrelated personal information. Student names and identifiers are not needed.

After an answer, grade it and append the event **before** presenting the next task; a merely presented question is not an assessed attempt. Append the next task as pending separately. Include curriculum IDs, item/family, hint level and whether reasoning was independently demonstrated. Read assessment.md for evidence fields. If a task was solved by the tutor on request, log exposure. If the student stops midway, the pending task remains pending rather than being scored as failure. A repeated tool call with the same event ID must not duplicate history or evidence.

STATUS.md must show last update, active goal, assessed coverage, levels/unknowns, current misconceptions, pending work and the next recommended step. Include the plan deviation or next review date if relevant. Keep the full history in sessions rather than growing STATUS.md without bound. Learners can inspect or export these Markdown files at any time.

## Plan synchronization

At session start read STATUS.md, state.json and LERNPLAN.md/plan.json. All skills prefer the next appropriate planned task and honor the plan's prerequisite gaps and review dates. A specific student request may override it. Record the deviation and offer to adjust the future plan; do not reject useful learning because it is out of order. After new evidence, complete the task actually done and update remaining blocks. Mark an item complete only after the specified work/check, not after showing it.

Use fof-study-plan for creating or substantially revising a schedule. The other skills can read its bundled instructions directly; the student does not need to install anything else. Carry existing history into a new plan version. Never silently shift a missed task into an overloaded day or past the exam date. A missed day is a planning event, not proof that the student forgot a concept.

## ChatGPT without a writable working folder

Use native downloadable-file tools when available to maintain the same directory structure in a session workspace and export an updated `Learning-Protokoll.zip`, especially at pauses, plan changes and session end. Tell the learner this is a downloadable session copy, not a write to their computer. Do not require a storage connector or another plugin. Provide state.json plus readable Markdown so it can be resumed in another chat.

If file creation is unavailable, keep an explicit chronological protocol block in the conversation and update STATUS and plan visibly after substantive changes. State that the record has **not** been saved to disk. On a save/close request emit a complete copyable passport and session log; on return ask for that record. Do not silently drop logging, pretend chat memory is a durable database, or claim there is an automatically synced folder on the student's machine. Prefer a shorter teaching response to omitting the protocol update.

## Helper use

`journal.py init --folder <student-workspace>` initializes an empty local record. `journal.py record --folder <student-workspace> --event <event.json>` appends a uniquely identified event. `journal.py plan --folder <student-workspace> --plan <plan.json>` installs a revised plan with an archived event. `journal.py refresh --folder <student-workspace>` regenerates derived Markdown and state after an interrupted update. Use a native host file writer if execution is unavailable, following the same schema and no-duplicate rule. No Python installation is required of a student using ChatGPT.
