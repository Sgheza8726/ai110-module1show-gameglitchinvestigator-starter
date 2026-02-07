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

## 📸 Demo

Here's the fixed game running successfully with all features working:

*final_game_demo*

**What's different:**
- ✅ "New Game" button resets the game without freezing
- ✅ Hints now point in the correct direction (no more backwards advice)
- ✅ Attempt counter works correctly and doesn't prematurely reveal the answer
- ✅ Secret number stays consistent across all guesses
- ✅ All 8 pytest tests pass

## 📝 Document Your Experience

### Bugs Found & Fixed

**Bug #1: New Game Button Freezes**
- **What was wrong:** Clicking "New Game" froze the UI and prevented further interaction
- **Root cause:** The `status` field wasn't being reset back to "playing", so `st.stop()` would execute and halt the app
- **How I fixed it:** Added `st.session_state.status = "playing"` in the New Game button handler
- **How I verified:** Clicked the New Game button and successfully submitted a guess

**Bug #2: Backwards Hints**
- **What was wrong:** The game told you to "go lower" when you should have guessed higher
- **Root cause:** On even attempts, the secret was converted to a string. Comparing `guess (int)` to `secret (str)` caused Python to use lexicographic string comparison instead of numeric comparison
- **How I fixed it:** Removed the string conversion entirely—the secret is always an int now
- **How I verified:** Created pytest tests that verify guess=60 with secret=50 correctly returns "Too High"

**Bug #3: Off-by-One Attempt Counter**
- **What was wrong:** When it showed "Attempts left: 1", you actually had zero attempts left
- **Root cause:** `st.session_state.attempts` was incremented before validation, throwing off the counter display
- **How I fixed it:** This was fixed by removing the string conversion bug (Bug #2), which was the real culprit causing weird behavior
- **How I verified:** Ran through a full game and watched the attempt counter stay accurate

### AI Collaboration

I used **Copilot in VS Code** as my debugging partner. Here's what worked well and what I had to push back on:

**What Worked:**
- Asking Copilot to explain the `check_guess()` function line-by-line helped me spot the string conversion issue
- Using Copilot to generate pytest test cases targeting each specific bug was super efficient
- Copilot's suggestions for refactoring game logic into `logic_utils.py` made the codebase cleaner

**What I Rejected:**
- Copilot initially suggested keeping the string conversion but "fixing the comparison logic." I pushed back because that would've been treating the symptom, not the disease. The real bug was mixing types in the first place
- I had to be clear that the logic should live in `logic_utils.py`, not `app.py`, even when Copilot tried to keep everything in one file

### Testing Strategy

I used a two-pronged approach:
1. **Automated tests**: Wrote 5 new pytest cases to catch the specific bugs (hint direction, input parsing, difficulty ranges)
2. **Manual testing**: Actually played the game to make sure it felt right and didn't crash

All 8 tests pass, and the Streamlit app starts without errors.
