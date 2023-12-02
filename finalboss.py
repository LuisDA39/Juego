import random
import string
import time

boss_health = 700
player_health = 100
damage_count = 0
phase = 1

print("Type swiftly and input the correct combination to unleash an attack on the boss.")
time.sleep(1.5)
while boss_health > 0 and player_health > 0:
    k = phase + 2
    damage = 0
    combination = ''.join(random.choices(string.ascii_lowercase, k=k))
    print(f"\nYour combination is: {combination}")

    time.sleep(0.5)

    start_time = time.time()
    user_input = input("Enter the combination: ")
    end_time = time.time()

    if user_input != combination:
        damage = random.randint(7, 10)
        player_health -= damage
        print(f"\nIncorrect combination. You lost {damage} health points")

    elif end_time - start_time > 4:
        damage = random.randint(7, 10)
        player_health -= damage
        print(f"\nToo slow. You lost {damage} health points")

    else:
        damage = random.randint(15, 30)
        damage_count += damage
        print(f"\nWell done! {damage} damage points to the boss")
        boss_health -= damage

    if boss_health < 0:
        boss_health = 0

    print("\n>Boss Health:", boss_health)
    print(">Player Health:", player_health)

    if damage_count > 70 and boss_health > 0:
        event_num = random.randint(1, 4)

        if event_num == 1:
            print("Boss is about to unleash a special attack. Get ready, type the combination backward!")
            time.sleep(1.5)
            damage = 0
            combination = ''.join(random.choices(string.ascii_lowercase, k=k))
            print(f"\nYour combination is: {combination}")
            time.sleep(0.5)
            start_time = time.time()
            user_input = input(" (!) Enter the combination in reverse order: ")
            end_time = time.time()

            if user_input != combination[::-1]:
                print("\nIncorrect combination")
                damage = random.randint(10, 20)
                print(f"Special attack! {damage} points less")

            elif end_time - start_time > 5:
                print("\nToo slow")
                damage = random.randint(10, 20)
                print(f"Special attack! {damage} points less")

            else:
                print("\nAttack dodged")

            player_health -= damage

        if event_num == 2:
            print("The boss has released his minions. Defeat them by entering the sum of the digits in the code.")
            time.sleep(2)

            damage = 0
            for i in range(3):
                start_time = time.time()
                num = random.randint(100, 999)
                print(f"\nYour number is: {num}")
                time.sleep(0.5)
                user_input = input(" (!) Enter the sum of the digits of the number: ")
                end_time = time.time()

                if int(user_input) != sum(int(digit) for digit in str(num)):
                    print("\nIncorrect sum")
                    damage += random.randint(6, 10)
                    print(f"An ally is launching an attack against you! {damage} damage points to you")

                elif end_time - start_time > 6:
                    print("\nToo slow")
                    damage += random.randint(6, 15)
                    print(f"Special attack! {damage} points less")

                else:
                    print(f"\nYou defeted an ally {3 - i} left")

            player_health -= damage

        if event_num == 3:
            print("You've found a medkit. Quickly press the designated key to heal yourself.")
            time.sleep(1.5)
            damage = 0
            random_letter = random.choice(string.ascii_lowercase)

            print(f"\n (!) Press '{random_letter}' 10 times in less than 5 seconds to heal.")
            time.sleep(0.5)
            start_time = time.time()
            user_input = input()
            end_time = time.time()

            if user_input.count(random_letter) < 10:
                print("\nYou haven't healed properly")
                damage = random.randint(10, 20)
                print(f"Damage! You lost {damage} health points")
                player_health -= damage

            elif end_time - start_time > 5:
                print("\nYou took too long.")
                damage = random.randint(10, 20)
                print(f"Damage! You lost {damage} health points")
                player_health -= damage

            else:
                heal = random.randint(5, 10)
                print(f"\nYou've healed! You gained {heal} health points")
                player_health += heal
                if player_health > 100:
                    player_health = 100

        if event_num == 4:
            print("The boss is gearing up for a special attack. Guess the correct number to minimize the damage.")
            time.sleep(1.5)
            start_time = time.time()
            secret_number = random.randint(1, 20)
            attempts = 0

            print("\nGuess a number between 1 and 20.")
            time.sleep(0.5)

            while True:
                user_input = input("\n(!) Please enter a number: ")
                end_time = time.time()

                if not user_input.isdigit():
                    print("Enter a valid number.")
                    continue

                number = int(user_input)
                attempts += 1

                if number < secret_number:
                    print("Too low! Try again.")
                elif number > secret_number:
                    print("Too high! Try again.")
                else:
                    if end_time - start_time > 10:
                        print(f"\nCorrect, but you took too long! The boss dealt a critical hit to you.")
                        damage = random.randint(10, 15)
                        print(f"Damage! You lost {damage} health points")
                        player_health -= damage
                    else:
                        print(f"\nCorrect! You guessed the number and managed to shield yourself from the attack.")
                        player_health -= attempts
                    break

        damage_count = 0

    if player_health <= 0:
        print("\nYou lost.")
        player_health = 0
        break

    if boss_health <= 0:
        print("\nYou won!")
        break

    if 500 > boss_health > 250:
        phase = 2

    if boss_health < 250:
        phase = 3

