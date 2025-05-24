#  Seagull Simulator

**Let's go to the dock for some chips!**

## Game Description

*Seagull Simulator* lets you become a rebellious beachside seagull.  
Steal chips. Dodge cars. Meet SpongeBob. Try not to die.  
Survive 12 chaotic days near Manly Beach and become a seagull legend.

This is a **text-based terminal game** where each day you choose from several actions—  
like eating chips, fishing, flying, or idling—to manage your:

-  Life  
-  Stamina  
-  Health  
-  Skill  

Every choice matters. Random events may surprise you.  
Can you make it through all 12 days?

---

## Target Audience

- Beginner Python programmers  
- Casual gamers who enjoy funny, choice-based storytelling  
- Anyone who secretly wishes they were a seagull  

---

## How to Play

1. Download files or clone this repository:
   ```bash
   git clone https://github.com/TiantianSunday/seagull-simulator.git
   cd seagull-simulator
   ```

2. Run the game:
   ```bash
   python main.py
   ```

3. Choose actions using number keys:
   - `1` Eat chips 🍟  
   - `2` Fish 🎣  
   - `3` Long-distance flight ✈️  
   - `4` City walk 🚶  
   - `5` Chill at the pool 💤  
   - `0` End the day early  
   - Type `end` to quit manually  

---

## Code Structure

| File | Description |
|------|-------------|
| `main.py` | Main game loop and user input |
| `class_seagull.py` | Seagull class and action logic |
| `class_table.py` | Fries flavor logic |
| `art.py` | ASCII-style visuals and begin/end |

---

## Preview

```
===== DAY 3 =====
Seagull Name: Wingston
   Life:  █████░░░░░ 50%
 Stamina: ████░░░░░░ 40%
  Health: ██████░░░░ 60%
   Skill: ███████░░░ 70%
Actions today: 2/3
=========================

What do you want to do today?
1. Eat chips
2. Fish
3. Long-distance flight
4. City walk
5. Chill at the pool
0. End the day early
```

---

## Requirements

- Python 3.6+
- No external libraries required

---

*I once stole chips from a tourist... legendary.*
