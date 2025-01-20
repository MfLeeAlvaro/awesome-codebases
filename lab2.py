import random

# "Simple is better than complex." - One of the Python Zen rules

def main():
    try:
        # Define the array of weapons
        weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]
        
        # Roll the dice (1-6)
        weaponRoll = random.randint(1, 6)
        print(f"You rolled: {weaponRoll}")
        
        # Add weaponRoll to hero's combat strength
        hero_combat_strength = 10  # Example starting combat strength
        hero_combat_strength += weaponRoll
        print(f"Hero's combat strength: {hero_combat_strength}")
        
        # Use weaponRoll as an index to determine the weapon
        hero_weapon = weapons[weaponRoll - 1]
        print(f"Hero's weapon: {hero_weapon}")
        
        # Define conditions based on weaponRoll
        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend.")
        elif weaponRoll <= 4:
            print("Your weapon is meh.")
        else:
            print("Nice weapon, friend!")
        
        # Additional condition for Fist
        if hero_weapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")
    
    except IndexError:
        print("Error: Weapon roll is out of range. Please check the dice roll logic.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
