# game/chapters/chapter5.py
from game.utils import load_quests

def start(player):
    print("\nChapter 5: HABITS & ROUTINES")
    print("This chapter is about building a life that runs smoothly.")

    quests = load_quests()
        
    routine_quest = quests['chapter5'][0]
    
    print(f"\n-- Quest: {routine_quest['title']} --")
    print(routine_quest['description'])

    for i, option in enumerate(routine_quest['options']):
        print(f"{i + 1}. {option}")
        
    while True:
        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(routine_quest['options']):
                chosen_habit = routine_quest['options'][choice]
                break
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    player.discipline += routine_quest['rewards']['discipline']
    player.willpower += routine_quest['rewards']['willpower']

    print(f"\nYou've committed to '{chosen_habit}'. A small step towards a more disciplined life.")
    print(f"Discipline +{routine_quest['rewards']['discipline']}, Willpower +{routine_quest['rewards']['willpower']}")
