# main.py
from game.player import Player
from game.chapters import chapter1, chapter2, chapter3, chapter4, chapter5, chapter6

def main():
    print("Welcome to RESET - Build Your Life from Zero")
    player = Player()
    player.setup()
    
    print("\nYour journey begins now.")
    
    chapters = [chapter1, chapter2, chapter3, chapter4, chapter5, chapter6]
    current_chapter = 0

    # Game loop
    while True:
        print("\nWhat would you like to do?")
        if current_chapter < len(chapters):
            print(f"1. Start Chapter {current_chapter + 1}")
        else:
            print("1. Continue your journey (coming soon)")
        print("2. View your stats")
        print("3. Quit")
        
        try:
            choice = int(input("> "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            if current_chapter < len(chapters):
                chapters[current_chapter].start(player)
                current_chapter += 1
            else:
                print("You have completed all available chapters. Thank you for playing!")
        elif choice == 2:
            print(f"\n--- Your Stats ---")
            print(f"Name: {player.name}")
            print(f"Clarity: {player.clarity}")
            print(f"Confidence: {player.confidence}")
            print(f"Energy: {player.energy}")
            print(f"Hope: {player.hope}")
            print(f"Emotional Stability: {player.emotional_stability}")
            print(f"Willpower: {player.willpower}")
            print(f"Self-Compassion: {player.self_compassion}")
            print(f"Self-Expression: {player.self_expression}")
            print(f"Personal Style: {player.personal_style}")
            print(f"Home Organization: {player.home_organization}")
            print(f"Discipline: {player.discipline}")
            print(f"Communication Skills: {player.communication_skills}")
            print(f"Career Clarity: {player.career_clarity}")
            print(f"--------------------")
        elif choice == 3:
            print("Thank you for playing RESET. See you next time.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
