"""A simple fortune-telling console application."""

from __future__ import annotations

import random

FORTUNES = [
    "A pleasant surprise is waiting for you this week.",
    "Your curiosity will lead you to an exciting opportunity.",
    "A kind word you share today will come back to you tenfold.",
    "You are closer to your goal than you realize.",
    "Good news will arrive from an unexpected place.",
    "Trust your instincts; they are especially sharp right now.",
    "A small step today creates big momentum tomorrow.",
    "A new friendship will bring fresh perspective.",
    "Your next challenge will reveal a hidden talent.",
    "Fortune favors your patience and persistence.",
]


def generate_fortune() -> str:
    """Return a random fortune cookie message."""
    return random.choice(FORTUNES)


def main() -> None:
    print("🥠 Welcome to the Fortune Cookie Teller! 🥠")
    input("Press Enter to reveal your fortune...")
    print(f"\n✨ Your fortune: {generate_fortune()}")


if __name__ == "__main__":
    main()
