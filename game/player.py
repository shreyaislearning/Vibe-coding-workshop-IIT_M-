# game/player.py

class Player:
    def __init__(self):
        self.name = ""
        self.personality_seeds = []
        self.trauma_load = ""
        self.energy_levels = ""
        # Base stats
        self.clarity = 0
        self.confidence = 10
        self.energy = 20
        self.hope = 10
        self.emotional_stability = 5
        self.willpower = 10
        self.self_compassion = 5
        self.style_points = 0
        self.self_expression = 0
        self.personal_style = ""
        self.home_organization = 0
        self.discipline = 0
        self.communication_skills = 0
        self.career_clarity = 0

    def setup(self):
        print("Let's start by creating your character.")
        
        print("\nChoose your personality seeds (e.g., Calm, Bold, Curious, Kind).")
        self.personality_seeds = [seed.strip() for seed in input("Enter up to 3, separated by commas: ").split(',')]
        
        print("\nWhat is your current trauma load? (Light, Medium, Heavy)")
        self.trauma_load = input("> ").lower()

        print("\nWhat are your current energy levels? (Low, Medium, High)")
        self.energy_levels = input("> ").lower()

        # Adjust stats based on choices
        if self.trauma_load == 'medium':
            self.hope -= 5
        elif self.trauma_load == 'heavy':
            self.hope -= 10
            self.confidence -= 5

        if self.energy_levels == 'high':
            self.energy += 10
        elif self.energy_levels == 'low':
            self.energy -= 10
            self.willpower -= 5
        
        print("\nYour starting choices have shaped your initial stats.")
