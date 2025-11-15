# game/chapters/chapter2.py
from game.utils import load_quests

def start(player):
    print("\nChapter 2: BUILD FROM INSIDE")
    print("This chapter is about building your inner world.")
    
    quests = load_quests()
        
    emotion_quest = quests['chapter2'][0]
    
    print(f"\n-- Quest: {emotion_quest['title']} --")
    print(emotion_quest['description'])
    
    positive_emotions = []
    negative_emotions = []
    
    for emotion in emotion_quest['emotions']:
        while True:
            choice = input(f"Is '{emotion}' a positive or negative emotion? (p/n): ").lower()
            if choice in ['p', 'n']:
                if choice == 'p':
                    positive_emotions.append(emotion)
                else:
                    negative_emotions.append(emotion)
                break
            else:
                print("Invalid input. Please enter 'p' or 'n'.")
            
    # More robust check for correctness using sets
    correct_pos = set(positive_emotions) == set(emotion_quest['solution']['positive'])
    correct_neg = set(negative_emotions) == set(emotion_quest['solution']['negative'])
    
    if correct_pos and correct_neg:
        print("\nWell done. You've sorted your emotions correctly.")
        player.emotional_stability += emotion_quest['rewards']['emotional_stability']
        player.clarity += emotion_quest['rewards']['clarity']
        print(f"Emotional Stability +{emotion_quest['rewards']['emotional_stability']}, Clarity +{emotion_quest['rewards']['clarity']}")
    else:
        print("\nThat's a good start. Reflecting on our feelings is what matters most.")
        # Lesser reward for trying
        player.emotional_stability += 5
        print("Emotional Stability +5")
