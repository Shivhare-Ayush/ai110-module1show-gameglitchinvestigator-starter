# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
   - This project is a Streamlit number guessing game used to practice debugging AI-generated code and validating fixes with tests.
- [x] Detail which bugs you found.
   - I found reversed hint logic (too high showed "Go HIGHER"), a type bug where the secret was cast to a string on even attempts, and a difficulty-range issue where Hard mode used a smaller range than Normal.
- [x] Explain what fixes you applied.
   - I refactored game logic from `app.py` into `logic_utils.py`, fixed the high/low direction logic in `check_guess`, removed the string-cast bug in the submit flow, and added regression tests in `tests/test_game_logic.py`.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
- [ ] [Insert a screenshot of pytest passing results here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
