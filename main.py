from class1 import Seagull

def create_seagull() -> Seagull:
    name = input("You are a strong seagull living near Manly Beach.\nWhat's your name? ")
    return Seagull(name)

def main():
    seagull = create_seagull()
    while True:
        seagull.display_state()

        if not seagull.can_act():
            print("💤 You've used all actions today. Ending the day...")
            print_day_summary(seagull)
            seagull.next_day()
            continue

        print("What do you want to do today?")
        print("1. Eat chips")
        print("2. Fish")
        print("3. Long-distance flight")
        print("4. City walk")
        print("5. Poolside idling")
        print("0. End the day early")

        choice = input("Choose an action: ").strip().lower()

        if choice == "1":
            seagull.act("chips")
        elif choice == "2":
            seagull.act("fish")
        elif choice == "3":
            seagull.act("fly")
        elif choice == "4":
            seagull.act("walk")
        elif choice == "5":
            seagull.act("idle")
        elif choice == "0":
            seagull.act("end")
        elif choice == "end":  # 隐藏指令
            print("🔒 You chose to end the game manually.")
            print("🕊️ Goodbye, brave seagull.")
            break
        else:
            print("❌ Invalid input.")

def print_day_summary(seagull: Seagull):
    print("\n📊 Daily Summary:")
    for action, count in seagull.stats_today.items():
        if count > 0:
            print(f" - {action.capitalize()}: {count} time(s)")
    print()

if __name__ == "__main__":
    main()

