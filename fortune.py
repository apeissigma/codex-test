"""A simple fortune-telling console application."""

from __future__ import annotations

import random

FORTUNES = [
    "When the lotus opens, an unexpected blessing finds your doorstep.",
    "The river of effort you begin today will return as quiet abundance.",
    "A patient heart will hear the answer before the question is spoken.",
    "What seems delayed is only ripening under the lantern of heaven.",
    "A teacher appears when your spirit is ready to listen deeply.",
    "Walk gently; the path of least noise reveals your next victory.",
    "A single mindful step now becomes ten thousand fortunate steps later.",
    "Harmony with others will uncover a hidden gate of opportunity.",
    "Your next trial is a disguised lesson, and the lesson is a gift.",
    "The jade of persistence is polished by calm and steady hands.",
]


def generate_fortune() -> str:
    """Return a random fortune cookie message."""
    return random.choice(FORTUNES)


def wants_another_fortune() -> bool:
    """Return True if the user wishes to consult another fortune."""
    answer = input("\nShall the oracle reveal another fortune? (y/n): ").strip().lower()
    return answer in {"y", "yes"}


def main() -> None:
    print("🥠 Welcome, seeker, to the Temple of Fortunes. 🥠")

    while True:
        input("Breathe in, then press Enter to unveil your fortune... ")
        print(f"\n✨ The oracle whispers: {generate_fortune()}")

        if not wants_another_fortune():
            print("\n🌟 May balance and good fortune accompany your journey. Farewell.")
            break


if __name__ == "__main__":
    main()
