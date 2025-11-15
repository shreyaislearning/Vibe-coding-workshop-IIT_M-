# game/chapters/chapter1.py
from game.utils import load_quests

def start(player):
    print("Chapter 1: WHO AM I?")
    
    quests = load_quests()
    
    name_quest = quests['chapter1'][0]
    
    print(f"\n-- Quest: {name_quest['title']} --")
    print(name_quest['description'])
    
    new_name = input("> ")
    player.name = new_name
    
    player.clarity += name_quest['rewards']['clarity']
    player.confidence += name_quest['rewards']['confidence']
    
    print(f"\nYou have named yourself '{player.name}'.")
    print(f"Clarity +{name_quest['rewards']['clarity']}, Confidence +{name_quest['rewards']['confidence']}")
