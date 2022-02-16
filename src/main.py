from resources import Character, Goblin
import random

def fight(fighter:Character, enemies: list):

    while not len(enemies) == 0:

        fighter_target = random.choice(enemies)
        fighter_target.take_damage(fighter.attack())
        if fighter_target.get_health() == 0:
            print("Target has died!")
            enemies.remove(fighter_target)
            if len(enemies) == 0: break

    print(f"fight is over! {fighter.name} won!")

def new_fight(players: list, enemies: list):
    participants = players + enemies #slår ihop alla deltagare till en lista
    random.shuffle(participants)

    for char in participants:
        #check if goblin or character
        if char in players:
            target = random.choice(enemies)
            
        else:
            target = random.choice(players)

        target.take_damage(char.attack())
        if target.get_health() == 0:
            print(f"{char.get_name()} has killed {target.get_name()}")
            if(type(target) == Goblin):
                enemies.remove(target)
            else:
                players.remove(target)
            
            participants.remove(target)
        else:
            print(f"{target.get_name()} was attacked by {char.get_name()} ")
            print(f"{target.get_name()} has {target.get_health()} HP left.")



def main():
    enemies = []
    players = []
    nick = Character("Nick", 16, 4, 1)
    emy = Character("Emy", 25, 5, 2)
    maxi = Character("Maxi", 1, 10, 0)
    players.append(nick)
    players.append(emy)
    players.append(maxi)

    enemies.append(Goblin(1))
    enemies.append(Goblin(2))
    enemies.append(Goblin(3))
    enemies.append(Goblin(4))

    # fight(players, enemies)
    while len(enemies) != 0 and len(players) != 0:
        new_fight(players, enemies)
    if len(enemies) == 0:
        print("The Players won!")
    elif len(players) == 0:
        print("The Goblins won!")


if __name__ == "__main__":
    main()