# game/chapters/chapter4.py
from game.utils import load_quests

def start(player):
    print("\nChapter 4: ENVIRONMENT")
    print("This chapter is about creating a space that nurtures your well-being.")

    quests = load_quests()
        
    declutter_quest = quests['chapter4'][0]
    
    print(f"\n-- Quest: {declutter_quest['title']} --")
    print(declutter_quest['description'])

    for i, option in enumerate(declutter_quest['options']):
        print(f"{i + 1}. {option}")
        
    while True:
        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(declutter_quest['options']):
                chosen_item = declutter_quest['options'][choice]
                break
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    player.home_organization += declutter_quest['rewards']['home_organization']
    player.clarity += declutter_quest['rewards']['clarity']

    print(f"\nYou've decided to deal with the '{chosen_item}'. Your space and mind feel clearer.")
    print(f"Home Organization +{declutter_quest['rewards']['home_organization']}, Clarity +{declutter_quest['rewards']['clarity']}")
