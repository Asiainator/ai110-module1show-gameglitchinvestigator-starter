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

- [ ] Describe the game's purpose.
   Higher or Lower guessing game with a range of number
- [ ] Detail which bugs you found.
   - Bugs Found 
- 1: Opposite hints, when the target number was higher it showed lower as the hint, when the target number was lower it showed higher as the hint
- 2: You can submit the same number multiple times as guesses, when it should not allow that stating an error message and not using your guess
- 3: You can submit not valid numbers/ words and it takes up a guess even though it shows an error message, when it should not take a guess and show an error message.
- 4: New game button does not reset the ability to guess again, only resets the secret number when it should reset the ability to guess so the user can play a new game.
- [ ] Explain what fixes you applied.
- Fixing opposite hints was fixing comparison.
- Adding Duplicate Guessing Detection
- Fixing when the Attempts Counter is added to, to make it consistent and more correct
= Adding a playing state to make sure the user can create a new game

## 📸 Demo

- ![screenshot](demo.png) [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
