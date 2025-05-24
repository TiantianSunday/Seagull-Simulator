import random

# show table with fries flavor
def render_table(flavor: str):
    print("\n🌴 You approach a beachside table...\n")
    print("        🪑         🪑         🪑")
    print("     ┌───────────────────────┐")
    print(f"     │   🍟  {flavor:^15}   │")
    print("     └───────────────────────┘")
    print("        🪑         🪑         🪑")
    print("     🌊    ☀️    🪸    🌊    ☀️\n")

# show random seagull with quote
def render_seagull_meme():
    ascii_gull = r"""
       __      
 \__( o)>     
   \___)      
     ||_       
    """
    quotes = [
        "Not all fries are worth dying for.",
        "I dove, I pecked, I conquered.",
        "Calories don't count if they fall from the sky.",
        "One man's trash is a seagull’s buffet.",
        "Even SpongeBob respects me now.",
        "I used to be a bird like you, then I took an arrow to the wing",
        "I once stole chips from a tourist... legendary.",
    ]
    print(ascii_gull)
    print(f"🗨️  {random.choice(quotes)}\n")

# show game welcome message
def render_intro():
    print("\nWelcome to Seagull Simulator!")
    print("You are a seagull living near Manly Beach.")
    print("Survive 12 days by choosing actions wisely.")
    print("Each day, you may act up to 3 times.")
    print("Keep your Life, Stamina, and Health above 0.")
    print("Your goal: Become the most legendary seagull on the beach.\n")
    print("Available actions:")
    print("  1 - Eat chips      (🍟)")
    print("  2 - Fish           (🎣)")
    print("  3 - Long flight    (✈️)")
    print("  4 - City walk      (🚶)")
    print("  5 - Chill at the pool   (💤)")
    print("  0 - End the day early\n")
    print("Type 'end' anytime to exit the game manually.\n")

# show game ending message
def render_game_end():
    print("\n" * 3)
    print("Thanks for playing Seagull Simulator.")
    print("May your wings stay strong and your chips stay crispy.")
    print("\n" * 3)
