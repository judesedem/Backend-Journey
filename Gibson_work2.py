   

import random

player_name = input("Enter name: ")
health = 100
gold = 50
inventory = ["sword"]
active_effects = []

def battle_monster():
    monster = ["Goblin", "Orc", "Skeleton", "Ogre"]
    sel_bat_monster = random.choice(monster)
    monster_health = random.randint(20, 40)
    return sel_bat_monster, monster_health

def open_chest():
    global inventory
    items = ["potion", "shield", "amulet"]
    reward = random.choice(items)
    inventory.append(reward)
    print(f"You found a {reward} in the chest!")

def use_item():
    global health, inventory, active_effects
    if not inventory:
        print("No items in inventory!")
    else:
        print(f"Inventory: {inventory}")
        item_prompt = input("Enter an item from the inventory: ").lower()
        if item_prompt == "potion" and "potion" in inventory:
            health += 20
            inventory.remove("potion")
            print("You used a potion! +20 health.")
        elif item_prompt == "shield" and "shield" in inventory:
            active_effects.append("shield")
            inventory.remove("shield")
            print("Shield equipped! Incoming damage halved once.")
        elif item_prompt == "amulet" and "amulet" in inventory:
            active_effects.append("amulet")
            inventory.remove("amulet")
            print("Amulet equipped! +5 damage next attack.")
        else:
            print("Invalid choice or item not in inventory.")
    return health

# Main loop
while health > 0:
    event = ["monster", "chest", "nothing"]
    current_event = random.choice(event)

    if current_event == "monster":
        sel_monster, monster_health = battle_monster()
        print(f"A {sel_monster} appeared with {monster_health} HP!")
        
        # Battle loop
        while monster_health > 0 and health > 0:
            choice = input("Enter choice (attack, run, or use item): ").lower()
            
            if choice == "attack":
                damage = random.randint(5, 15)
                if "amulet" in active_effects:
                    damage += 5
                    active_effects.remove("amulet")
                monster_health -= damage
                print(f"You hit the {sel_monster} for {damage} damage!")
                
                if monster_health > 0:
                    monster_damage = random.randint(5, 12)
                    if "shield" in active_effects:
                        monster_damage //= 2
                        active_effects.remove("shield")
                    health -= monster_damage
                    print(f"The {sel_monster} hit you for {monster_damage} damage!")
            
            elif choice == "use item":
                use_item()
            
            elif choice == "run":
                print("You ran away!")
                break
            
            if health <= 0:
                print("GAME OVER")
                break

        else:
            if monster_health <= 0:
                reward = random.randint(10, 30)
                gold += reward
                print(f"You defeated the {sel_monster} and found {reward} gold!")
                print(f"Current health: {health}, Gold: {gold}, Inventory: {inventory}")

    elif current_event == "chest":
        open_chest()
    else:
        print("The room is empty...")

    choice = input("Enter 'continue' to proceed, 'use item' to use inventory, or 'quit' to exit: ").lower()
    if choice == "use item":
        use_item()
    elif choice == "quit":
        print(f"You leave the dungeon with {gold} gold and {inventory}.")
        break


              

     








    





            

            

        


      