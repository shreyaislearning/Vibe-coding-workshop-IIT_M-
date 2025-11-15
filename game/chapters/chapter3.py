# game/chapters/chapter3.py
from game.utils import load_quests

def start(player):
    print("\nChapter 3: OUTER SELF")
    print("This chapter is about defining your style and expressing yourself.")

    quests = load_quests()
        
    style_quest = quests['chapter3'][0]
    
    print(f"\n-- Quest: {style_quest['title']} --")
    print(style_quest['description'])

    for i, option in enumerate(style_quest['options']):
        print(f"{i + 1}. {option}")

    while True:
        try:
            choice = int(input("> ")) - 1
            if 0 <= choice < len(style_quest['options']):
                chosen_style = style_quest['options'][choice]
                break
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    player.personal_style = chosen_style

    player.self_expression += style_quest['rewards']['self_expression']
    player.confidence += style_quest['rewards']['confidence']

    print(f"\nYou've chosen the '{chosen_style}' style. Your self-expression and confidence have grown.")
    print(f"Self-Expression +{style_quest['rewards']['self_expression']}, Confidence +{style_quest['rewards']['confidence']}")

