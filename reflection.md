# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- Bugs Found 
- 1: Opposite hints, when the target number was higher it showed lower as the hint, when the target number was lower it showed higher as the hint
- 2: You can submit the same number multiple times as guesses, when it should not allow that stating an error message and not using your guess
- 3: You can submit not valid numbers/ words and it takes up a guess even though it shows an error message, when it should not take a guess and show an error message.
- 4: New game button does not reset the ability to guess again, only resets the secret number when it should reset the ability to guess so the user can play a new game.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The unnesscarry parsing of the guessed number into a string.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  It assumed how i wanted the test folder ran and put it into test_game_logic.py instead of creating a new test file.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  Through human trial and error and manually checking.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  Fact checking the new game button works whether a win or lost.  
- Did AI help you design or understand any tests? How?
  Yes it explained the logic behind the functions and gave them clear names in the function.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  It basically reruns  your code everytime it gets interacted with but this creates issues as variables get recreated so random variables become differnt and session states allow you to keep data over. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

     Most likely using AI to help diagnoise the problem area and then breaking down the issue.

- What is one thing you would do differently next time you work with AI on a coding task?

  Be more specific with what I want and spefically the area i want it to work in. Preventing any miscommunications with AI is a must.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

 I was typically against AI code because to me it makes me think less but in reality it just switches my job to debugger and makes me understand why companies are requireing AI usage because this is super fast, as this is my real project using AI to help code.
