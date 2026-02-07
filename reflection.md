# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- Clicking "New Game" froze the screen instead of resetting it, so I couldn't submit my first guess or do anything else.
- The hint system gave backwards advice—it told me to guess lower when my number was already too low, which made no sense.
- The attempt counter was off by one. When it said "Attempts left: 1," I thought I had another guess, but it actually revealed the answer and ended the game.


---

## 2. How did you use AI as a teammate?

I used Copilot in VS Code to understand the bugs and help me fix them. First, I had Copilot explain the logic in the check_guess function line-by-line so I could see why the hints were backwards on even attempts. That helped me realize the secret was being converted to a string, breaking the comparison.

One thing Copilot suggested that was actually wrong: it initially suggested I keep the string conversion but just "fix the comparison logic." That wouldn't have solved the real problem—the bug was in mixing types in the first place. I rejected that idea and instead removed the string conversion entirely, which was the real fix.

Another suggestion from Copilot that worked great: it helped me generate test cases for each bug. I asked it to write tests that would catch the "too high/too low" bug, and it created tests that verify hints point in the right direction with integer secrets. Running pytest confirmed these tests all pass now.

---

## 3. Debugging and testing your fixes

I decided a bug was really fixed by running pytest and also testing the game live. For the "backwards hints" bug, I wrote a test that checks if guess=60 and secret=50 returns "Too High"—and it does now. For the "frozen New Game button," I verified by actually clicking the New Game button in the app and making sure the game let me submit a guess without freezing.

I ran pytest with all 8 tests (the original 3 plus 5 new ones I wrote for the bugs), and they all passed. Then I started the Streamlit app and confirmed it doesn't throw any import errors. The app boots successfully now without crashes.

Copilot helped a lot here. I asked it to generate tests that specifically target each bug, and it created tests for the hint direction, input parsing, and difficulty ranges. That made it easy to catch if something broke again.

---

## 4. What did you learn about Streamlit and state?

The secret number kept changing in the original app because the New Game button wasn't resetting st.session_state.status back to "playing." So every time the page reran, st.stop() would execute and freeze before a new secret could be properly set. I fixed it by explicitly setting status = "playing" when New Game is clicked.

Streamlit reruns are kind of like this: every time something changes (you submit a guess, click a button), the entire script runs from top to bottom again. Session state is how you remember things between reruns—it's like a dictionary that survives each run. Without it, variables would reset every time. It's actually pretty cool once you understand it, because it means the UI is always synced with your data.

The change that finally fixed the secret number issue was adding one line: `st.session_state.status = "playing"` right after resetting attempts in the New Game button handler. That let the code proceed past st.stop() and actually start a new game.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse: marking bugs with FIXME comments right in the code before fixing them. It gave me a specific point to reference when asking Copilot for help, and it made the codebase way clearer. I'll do this on future projects instead of just holding bug descriptions in my head.

Next time I work with AI on code, I'll be more skeptical of the first suggestion and ask follow-up questions. Copilot's initial idea to "just fix the comparison" sounded plausible until I really thought through the root cause. I'd push back earlier and ask "why is this the right fix?" instead of accepting it at face value.

This project made me realize that AI-generated code isn't inherently bad—it's often just untested. The real skill is knowing how to test it thoroughly and being willing to look under the hood to understand why bugs exist. That's way more valuable than having perfect code handed to you.
