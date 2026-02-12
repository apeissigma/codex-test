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


def wants_another_fortune() -> bool:
    """Return True if the user wants to reveal another fortune."""
    answer = input("\nReveal another fortune? (y/n): ").strip().lower()
    return answer in {"y", "yes"}


def main() -> None:
    print("🥠 Welcome to the Fortune Cookie Teller! 🥠")

    while True:
        input("Press Enter to reveal your fortune...")
        print(f"\n✨ Your fortune: {generate_fortune()}")

        if not wants_another_fortune():
            print("\n🌟 Thanks for visiting. Goodbye!")
            break


if __name__ == "__main__":
    main()
