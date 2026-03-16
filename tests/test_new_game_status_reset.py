"""
Tests targeting the bug where clicking "New Game" did not reset `status`
back to "playing", causing the st.stop() guard in app.py to keep blocking
guesses even after a reset.

The guard in app.py (line 80):
    if st.session_state.status != "playing":
        st.stop()

The fix was adding `st.session_state.status = "playing"` to the new-game
reset block. These tests verify that logic.
"""

import pytest


def simulate_new_game(state: dict) -> dict:
    """Mirrors the new-game reset block in app.py lines 72-76."""
    state["attempts"] = 0
    state["secret"] = 99  # deterministic stand-in for random.randint
    state["status"] = "playing"
    state["history"] = []
    return state


def can_guess(state: dict) -> bool:
    """Mirrors the guard condition at app.py line 80."""
    return state["status"] == "playing"


# --- Core bug regression tests ---

def test_new_game_resets_status_from_won():
    # Bug: status stayed "won" after reset, blocking all further guesses
    state = {"status": "won", "attempts": 3, "secret": 42, "history": [10, 20, 42]}
    state = simulate_new_game(state)
    assert state["status"] == "playing"


def test_new_game_resets_status_from_lost():
    # Bug: same issue from the "lost" path
    state = {"status": "lost", "attempts": 8, "secret": 42, "history": list(range(1, 9))}
    state = simulate_new_game(state)
    assert state["status"] == "playing"


# --- Guard condition tests ---

def test_won_status_blocks_guessing():
    # The guard should stop the player when the game is already won
    state = {"status": "won"}
    assert can_guess(state) is False


def test_lost_status_blocks_guessing():
    # The guard should stop the player when the game is already lost
    state = {"status": "lost"}
    assert can_guess(state) is False


def test_playing_status_allows_guessing():
    # A fresh / reset game must pass the guard
    state = {"status": "playing"}
    assert can_guess(state) is True


# --- New game also resets related state ---

def test_new_game_clears_history():
    # History must be wiped so duplicate-guess detection starts fresh
    state = {"status": "won", "attempts": 3, "secret": 42, "history": [10, 20, 42]}
    state = simulate_new_game(state)
    assert state["history"] == []


def test_new_game_resets_attempts():
    # Attempt counter must be reset so the attempt limit is enforced correctly
    state = {"status": "lost", "attempts": 8, "secret": 42, "history": []}
    state = simulate_new_game(state)
    assert state["attempts"] == 0


# --- Full flow: win → new game → can guess again ---

def test_full_flow_win_then_new_game_allows_guessing():
    state = {"status": "playing", "attempts": 0, "secret": 42, "history": []}

    # Player wins
    state["status"] = "won"
    assert can_guess(state) is False  # blocked before reset

    # New game
    state = simulate_new_game(state)
    assert can_guess(state) is True   # unblocked after reset


# --- Full flow: lose → new game → can guess again ---

def test_full_flow_lose_then_new_game_allows_guessing():
    state = {"status": "playing", "attempts": 0, "secret": 42, "history": []}

    # Player loses
    state["status"] = "lost"
    assert can_guess(state) is False  # blocked before reset

    # New game
    state = simulate_new_game(state)
    assert can_guess(state) is True   # unblocked after reset
