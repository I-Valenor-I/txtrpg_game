from timeit import repeat


print("Welcome to the dungeon!")

a1 = input("You see a two paths. Do you want to go left or right? ").lower()
power = 0

if a1 == "left":
    print("As you walk you begin to feel like someone is watching you. As you turn a corner you see from the corner of your eye something jump out at you, but you never see what it was as it bites through your neck killing you instantly!")

elif a1 == "right":
    power += 4
    print("You walk till you reach a dead end and find a sword in it's sheath sitting in the corner. You take it and just having it makes you feel safer as you turn around to return to the coridor where you awakend and go left.")
    a2 = input("You can go left or right. ").lower()

    if a2 == "left":
        a3 = input("You can go left, right, or forward. ").lower()

        if a3 == "right":
            print("You fall in through a trapdoor in the floor that leads to a bunch of spikes that pierce you. \nGAME OVER")

        elif a3 == "forward":
            power += 3
            print("you find a chest with a chestplate in it. you take it whilst thinking that 'now I am not completly without defenses.' and return to the coridor you came from.")
            a4 = input("You can go left or right. ").lower()

            if a4 == "left" and power == 7:
                a5 = input("You can go left, right or forward. ").lower()

                if a5 == "right":
                    pass

                elif a5 == "left":
                    print("You chance upon a dragon waking up. It sees you and kills you instantly")

                elif a5 == "forward":
                    print("You walk forward for awhile when you suddenly start to hear a rumbling sound. You turn around just to witnes your demize to a rolling boulder.")

            elif a4 == "right":
                print("You were made into a porkupine by an arrow trap. \nGAME OVER")

        elif a3 == "left":
            print("As you walk you begin to feel like someone is watching you. As you turn a corner you see from the corner of your eye something jump out at you, but you never see what it was as it bites through your neck killing you instantly!")

        else:
            print("You sit and wait for better times. \n\n\nAfter waiting for a week you die of thirst.\nGAME OVER")

    elif a2 == "right":
        print("You were made into a porkupine by an arrow trap. \nGAME OVER")

    else:
        print("You sit and wait for better times. \n\n\nAfter waiting for a week you die of thirst.\nGAME OVER")

else:
    print("You sit and wait for better times. \n\n\nAfter waiting for a week you die of thirst.\nGAME OVER")
