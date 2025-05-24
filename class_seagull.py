import random
from class_table import Table
from art import render_table, render_seagull_meme, render_intro, render_game_end

# Seagull class - game logic for actions and stats
class Seagull:
    MAX = 10
    MIN = 0
    MAX_ACTIONS_PER_DAY = 3
    MAX_DAYS = 12

    def __init__(self, name: str):
        render_intro()  # show welcome message
        self.name = name
        self.day = 1
        self.life = 5
        self.stamina = 5
        self.health = 5
        self.skill = 5
        self.actions_today = 0
        self.stats_today = {"chips": 0, "fish": 0, "fly": 0, "walk": 0, "idle": 0}

    def next_day(self):
        self.day += 1
        self.actions_today = 0
        self.stats_today = {key: 0 for key in self.stats_today}
        recovered = min(2, self.MAX - self.stamina)
        self.stamina = min(self.stamina + 2, self.MAX)
        print(f"\n🌅 A new day begins... (+{recovered} Stamina)\n")
        render_seagull_meme()  # show seagull quote
        if self.day > self.MAX_DAYS:
            print("📆 You've reached Day 12. The journey ends here.")
            print("🌟 Your seagull legacy will echo across Manly Beach.")
            render_game_end()
            exit()

    def can_act(self):
        return self.actions_today < self.MAX_ACTIONS_PER_DAY

    def act(self, action: str):
        if not self.can_act():
            print("🕒 You've used all actions today. End the day to continue.")
            return

        self.actions_today += 1
        if action in self.stats_today:
            self.stats_today[action] += 1

        # handle different actions
        if action == "chips":
            table = Table()
            table.place_fries()
            flavor = table.get_fries()
            render_table(flavor)
            if flavor == 'Original':
                self.life_up()
                self.health_down()
            elif flavor == 'Sichuan Chili':
                self.life_up()
                self.health_down()
                self.health_down()
            elif flavor == 'Beef Gravy':
                self.life_up()
                self.life_up()
                self.health_down()
            self.stamina_down()
            print(f"{self.name} eats the {flavor} fries... [Effects applied based on flavor]\n")

        elif action == "fish":
            self.life_up()
            self.health_up()
            self.stamina_down()
            print(f"{self.name} catches a fish! +Life, +Health, -Stamina")
            self.fish_event()

        elif action == "fly":
            self.life_down()
            self.stamina_down()
            self.skill_up()
            print(f"{self.name} flies a long distance... -Life, -Stamina, +Skill")
            self.fly_event()

        elif action == "walk":
            self.life_down()
            self.stamina_down()
            print(f"{self.name} explores the city... -Life, -Stamina")
            self.city_event()

        elif action == "idle":
            self.stamina_up()
            print(f"{self.name} does nothing. Peaceful. +Stamina")

        elif action == "end":
            print("🕓 Ending the day early...")
            self.actions_today = self.MAX_ACTIONS_PER_DAY
        else:
            print("❌ Invalid action.")
            return

        self.check_status()

    # special events
    def fish_event(self):
        if random.random() < 0.3:
            print("🍔 SpongeBob appears and gives you a Krabby Patty! +1 Health")
            self.health_up()

    def fly_event(self):
        if random.random() < 0.3:
            print("👽 You meet an alien seagull! It trains you. +2 Skill")
            self.skill_up()
            self.skill_up()

    def city_event(self):
        if random.random() < 0.3:
            print("🚗 CAR ACCIDENT! You got hit while walking. -2 Life")
            self.life_down()
            self.life_down()

    # check stat values after action
    def check_status(self):
        for attr, label in [("life", "Life"), ("stamina", "Stamina"), ("health", "Health")]:
            value = getattr(self, attr)
            if value == 0:
                print(f"💀 {label} dropped to 0. {self.name} has perished.")
                render_game_end()
                exit()
            elif value == 3:
                print(f"⚠️ {label} is getting low!")
            elif value == 10:
                print(f"🏆 Maxed out {label}!")

        if self.skill == 10:
            print("🌟 You're the most skilled seagull on the beach!")

    # stat changes
    def life_up(self):     self.life = min(self.life + 1, self.MAX)
    def life_down(self):   self.life = max(self.life - 1, self.MIN)
    def stamina_up(self):  self.stamina = min(self.stamina + 1, self.MAX)
    def stamina_down(self):self.stamina = max(self.stamina - 1, self.MIN)
    def health_up(self):   self.health = min(self.health + 1, self.MAX)
    def health_down(self): self.health = max(self.health - 1, self.MIN)
    def skill_up(self):    self.skill = min(self.skill + 1, self.MAX)

    # show status bars
    def display_state(self):
        print(f"\n===== DAY {self.day} =====")
        print(f"Seagull Name: {self.name}")
        self.display_bar(self.life, "Life")
        self.display_bar(self.stamina, "Stamina")
        self.display_bar(self.health, "Health")
        self.display_bar(self.skill, "Skill")
        print(f"Actions today: {self.actions_today}/{self.MAX_ACTIONS_PER_DAY}")
        print("=========================\n")

    @staticmethod
    def display_bar(value: int, label: str):
        filled = '█' * value
        empty = '░' * (10 - value)
        print(f"{label:>8}: {filled}{empty} {value * 10}%")
