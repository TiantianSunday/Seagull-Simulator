# Seagull Simulator - Gameplay Guide

## Objective

Survive for 12 days as a seagull near Manly Beach. Each day, you can perform **up to 3 actions**. Your survival depends on four key attributes:

- ❤️ **Life** (0-10): Drops with dangerous actions. Hits 0 = game over.
- 💉 **Health** (0-10): Represents internal condition. Drops with unhealthy food or accidents.
- 💪 **Stamina** (0-10): Used for most actions. Rest to regain. Refilled +2 every new day.
- 🧠 **Skill** (0-10): Trained by flying. Maxing it gives glory, not survival.

You **lose the game** if Life, Health, or Stamina drop to **0**.

---

## Action Summary

| Action            | Life     | Health   | Stamina  | Skill   | Random Event                |
|-------------------|----------|----------|----------|---------|-----------------------------|
| Eat chips         | +1~2     | -1~-2    | -1       |         | No                         |
| Fish              | +1       | +1       | -1       |         | 🍔 30%: Krabby Patty +1 HP |
| Long-distance fly | -1       |          | -1       | +1      | 👽 30%: +2 Skill            |
| City walk         | -1       |          | -1       |         | 🚗 30%: Car hit -2 Life    |
| Chill at pool     |          |          | +1       |         | No                         |
| End the day       | -        | -        | -        | -       | No                         |

> Eat Chips uses a random flavor system with 3 types of fries. Each has different effects.

---

## Chip Flavors & Effects 🍟 

| Flavor           | Life | Health | Stamina | Notes                          |
|------------------|------|--------|---------|--------------------------------|
| Original         | +1   | -1     | -1      | Standard fries                 |
| Sichuan Chili    | +1   | -2     | -1      | Spicy and unhealthy            |
| Beef Gravy       | +2   | -1     | -1      | Delicious but greasy           |

Fries are served randomly using a Table class, and their effects are applied immediately.

---

## Random Events (30% Chance)

| Trigger Action | Event                        | Effect                |
|----------------|------------------------------|-----------------------|
| Fish           | 🍔 SpongeBob gives you food   | +1 Health             |
| Fly            | 👽 Alien seagull trains you   | +2 Skill              |
| City Walk      | 🚗 Car accident               | -2 Life               |

Events only occur when you perform the linked action.

---

## Threshold Warnings

- Attribute reaches **3** → ⚠️ "Getting low" warning appears
- Attribute reaches **10** → 🏆 "Maxed out!" message
- Skill reaches 10 → 🌟 Legendary seagull message
- Any Life, Health or Stamina reaches **0** → 💀 Game Over

---

## Daily Cycle

- 3 actions max per day
- End day manually with action `0` or automatically when all 3 used
- At the start of each new day:
  - +2 Stamina recovered (up to max 10)
  - Random seagull meme shown

---

## 🕹️ Hidden Commands

- Type `end` any time to quit the game manually

---

Live wild. Eat fries. Fear no car.
