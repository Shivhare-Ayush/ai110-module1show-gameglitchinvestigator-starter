# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the app, it looked fine on the surface, but the hints felt wrong almost immediately. I guessed a number that was clearly too high, and the app told me to go higher instead. After a few rounds, Hard mode also felt easier than Normal, so I checked the ranges and found they were backwards. I also noticed the feedback could change in strange ways on alternating turns, which led me to a type mismatch bug.

**Bug 1 - Hints are backwards (`app.py`, lines 38-39)**
- **Expected:** If my guess is too high, the app should tell me to go lower.
- **Actual:** When `guess > secret`, the code returns "📈 Go HIGHER!". The `>` and `<` feedback branches are swapped.

**Bug 2 - Hard difficulty has a smaller range than Normal (`app.py`, lines 9-10)**
- **Expected:** Hard mode should use a wider range so the game is actually harder.
- **Actual:** `"Hard"` returns `(1, 50)` while `"Normal"` returns `(1, 100)`, so Hard mode is easier.

**Bug 3 - Secret is cast to a string on even-numbered attempts (`app.py`, lines 158-161)**
- **Expected:** Every guess should be compared as numbers, so `guess=9` should correctly be "Too High" when `secret=5`.
- **Actual:** On even attempts, the secret is converted with `str()`, so Python compares an `int` to a `str`, triggers a `TypeError`, and falls back to string comparison. That can produce incorrect ordering, like `"9" > "50"`, and the win condition can fail.

---

## 2. How did you use AI as a teammate?

I used GitHub Copilot Chat (Agent mode and Inline Chat) and Claude Code to work through one bug at a time. One correct AI suggestion was to move `check_guess` and `parse_guess` out of `app.py` into `logic_utils.py`, then fix the reversed high/low hint branches in one place. I verified that suggestion by running pytest and confirming the regression tests passed, especially the case where a guess of 60 against a secret of 50 is "Too High" with a "Go LOWER" hint. One misleading suggestion was treating `import app` as a full smoke test, because that only validates imports and does not test real Streamlit interaction. I verified this limitation by running `streamlit run app.py` and manually checking gameplay behavior in the browser.

---

## 3. Debugging and testing your fixes

I treated a bug as fixed only when both automated tests and live gameplay matched the expected behavior. I ran pytest and confirmed the full test set passed, including regression tests for hint direction and integer comparison behavior. One important test was `check_guess(60, 50)`, which now consistently returns "Too High" and a message that tells the player to go lower. I also ran the app with Streamlit and played several rounds to confirm the even-attempt type glitch was gone and the win condition still worked. AI helped by proposing targeted regression tests, and I used those suggestions as a starting point before verifying each one myself.

---

## 4. What did you learn about Streamlit and state?

I would explain Streamlit reruns as: every time you click a widget, Streamlit runs your script from top to bottom again. If you store values in regular local variables, they can reset on every click and make the app feel buggy. Session state is the way to keep important data like the secret number, attempts, score, and status across reruns. Once I understood this, it became much easier to reason about why the app behavior changed after each submit. I also learned to check exactly where state is initialized and updated, because one wrong assignment can break game flow.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing or updating a regression test right after I fix each bug, so I can prove the bug is gone and protect against future regressions. Next time, I would use even smaller AI prompts and keep each chat session focused on one function and one behavior, then review diffs before accepting anything. I would also reject quick "it imports so it works" conclusions and always do at least one real runtime check in the actual app. This project changed how I think about AI-generated code because I now treat AI as a collaborator, not an authority. AI can move work faster, but I am still responsible for correctness, testing, and final decisions.
