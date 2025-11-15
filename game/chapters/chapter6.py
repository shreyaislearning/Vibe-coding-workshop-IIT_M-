# game/chapters/chapter6.py
from game.utils import load_quests

def start(player):
    print("\nChapter 6: SOCIAL WORLD & CAREER")
    print("This chapter is about finding your place in the world.")

    quests = load_quests()
        
    career_quest = quests['chapter6'][0]
    
    print(f"\n-- Quest: {career_quest['title']} --")
    print(career_quest['description'])

    for i, option in enumerate(career_quest['options']):
        print(f"{i + 1}. {option}")
        
    while True:
        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(career_quest['options']):
                chosen_field = career_quest['options'][choice]
                break
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    player.career_clarity += career_quest['rewards']['career_clarity']
    player.hope += career_quest['rewards']['hope']

    print(f"\nYou've started thinking about a future in '{chosen_field}'. The path ahead is a little clearer now.")
    print(f"Career Clarity +{career_quest['rewards']['career_clarity']}, Hope +{career_quest['rewards']['hope']}")
