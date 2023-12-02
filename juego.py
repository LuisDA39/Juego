import os
import random
import time
import pygame


class Videogame:
    def __init__(self):
        self.health = 2  # limitar la vida, no puede llegar a mas de 100 pts
        self.inventory = []  # crear el inventario
        self.max_cap = 1
        self.current_space = 0
        self.player_position = [1, 9]
        self.map = [
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 1, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 0, 0, 0, 0]
        ]
        self.visited = []
        self.car_first_visit = True

    def play_music(self, file_path):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        # falta: alargar la duracion de las canciones

    def print_slow(self, text):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.0005)
        print()

    def path_A(self):
        print("")
        self.print_slow("      Tony successfully cuts the rope; however, the problem is not over yet, he is wretched and even more distressed.")
        self.print_slow("      He takes another look, he sees a window on the right side of the room, his despair makes him about only three options ")
        print("                Break the window  [Break]")
        print("                Kick the door  [Kick]")
        print("                Use the spring on the door lock   [Spring]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['break', 'kick', 'spring']):
                if op == 'break':
                    self.print_slow("processing...")
                    self.path_C()
                    break
                if op == 'kick':
                    self.print_slow("processing...")
                    self.path_D()
                    break
                if op == 'spring':
                    self.print_slow("processing...")
                    self.path_E()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_B(self):
        print("")
        self.print_slow("      Tony attempts to sever the rope, but a misjudged move results in a perilous gash across his hand, blood trickling as ")
        self.print_slow("      he collapses from the injury. Health depletes by 25 points... ")
        self.print_slow("      Unfortunately, The Keeper caught wind of his attempts to break free. Swiftly, the rope was replaced with unyielding")
        self.print_slow("      plastic straps, binding Tony to the chair before The Keeper departed.")
        self.health -= 25
        print("                Patiently wait until The Keeper dozes off [Wait]")
        print("                Attempt to get free by breaking the chair [Attemp]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['wait', 'attemp']):
                if op == 'wait':
                    self.print_slow("processing...")
                    self.path_F()
                    break
                if op == 'attemp':
                    self.print_slow("processing...")
                    self.path_G()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_C(self):
        print("")
        self.print_slow("      Tony breaks the window, unluckily for him, there was a grill outside the window, The Keeper listened to all the ")
        self.print_slow("      noise he made, he is coming…  ")
        print("                Use the stick to strike the Keeper [Strike]")
        print("                Make a run for it [Run]")
        print("                Let yourself be caught [caught]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['strike', 'run', 'caught']):
                if op == 'strike':
                    self.print_slow("processing...")
                    self.path_H()
                    break
                if op == 'run':
                    self.print_slow("processing...")
                    self.path_I()
                    break
                if op == 'caught':
                    self.print_slow("processing...")
                    self.path_J()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_D(self):
        print("")
        self.print_slow("      Tony kicks repeatedly the door, he’s making way too much noise, he wasn’t able to break it, The Keeper is coming…  ")
        print("                Use the stick to strike the Keeper [Strike]")
        print("                Make a run for it [Run]")
        print("                Let yourself be caught [Caught]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['strike', 'run', 'caught']):
                if op == 'strike':
                    self.print_slow("processing...")
                    self.path_H()
                    break
                if op == 'run':
                    self.print_slow("processing...")
                    self.path_I()
                    break
                if op == 'caught':
                    self.print_slow("processing...")
                    self.path_J()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_E(self):
        print("")
        self.print_slow("      Tony molded the spring on a perfect shape and used it to open the door, Tony is free, he runs as fast as he can")
        self.print_slow("      and gets out the cabin, everything around is forest...")
        print("")
        self.unlock_map()
        self.move_player()

    def path_F(self):
        print("")
        self.print_slow("      Enduring a tense six-hour wait until the cabin fell silent, Tony seized his chance, What’s next for Tony? ")
        print("                break free from the chair [chair]")
        print("                keep waiting [wait]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['chair', 'wait']):
                if op == 'chair':
                    self.print_slow("processing...")
                    self.path_K()
                    break
                if op == 'wait':
                    self.print_slow("processing...")
                    self.path_L()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_G(self):
        print("")
        self.print_slow("      As Tony breaks free from the chair, the Keeper, alerted by the commotion, moves swiftly to recapture him... ")
        print("                Use the stick to strike the Keeper [Strike]")
        print("                Make a run for it [Run]")
        print("                Let yourself be caught [Caught]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['strike', 'run', 'caught']):
                if op == 'strike':
                    self.print_slow("processing...")
                    self.path_H()
                    break
                if op == 'run':
                    self.print_slow("processing...")
                    self.path_I()
                    break
                if op == 'caught':
                    self.print_slow("processing...")
                    self.path_J()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_H(self):
        print("")
        self.print_slow("      Tony wields the stick, delivering a forceful blow to The Keeper before launching into a relentless barrage ")
        self.print_slow("      of kicks and punches until the antagonist succumbs, collapsing to the ground. With swift determination,")
        self.print_slow("      Tony seizes the chance to make his escape, bolting from the cabin in a desperate rush for freedom.")
        print("")
        self.unlock_map()
        self.move_player()

    def path_I(self):
        print("")
        self.print_slow("      In a fit of frustration, he unleashed an attack of rage, furiously kicked the mattress and a hidden void beneath")
        self.print_slow("      the floor revealed itself, Without hesitation, he reached into the hollow and unearthed a rusted clasp-knife. He")
        self.print_slow("      He took it and use it to break the handle, lamentably the clasp-knife was too old and broke in the process.  He")
        self.print_slow("      didn’t look back and got to be free, however this isn’t over…")
        print("")
        self.unlock_map()
        self.move_player()

    def path_J(self):
        pass
    #completar historia

    def path_K(self):
        print("")
        self.print_slow("      With determination, he launched a daring attempt, successfully breaking free from the chair, nailing the")
        self.print_slow("      escape and skillfully shattered the door lock, consumed by desperation to flee. Without a glance back,")
        self.print_slow("      he sprinted into the unknown, bursting out into the dense forest beyond. ")
        print("")
        self.unlock_map()
        self.move_player()

    def path_L(self):
        print("")
        self.print_slow("      Tony drifted into an uneasy slumber, yet this time, his dreams took a terrifying turn. A malevolent ")
        self.print_slow("      creature invaded his subconscious, unleashing a harrowing nightmare. Relentlessly pursued, he was finally  ")
        self.print_slow("      ensnared, the creature threatening to devour his very soul. It provoked him an intense fever within the ")
        self.print_slow("      dream jolted him awake, but not before his health plummeted by 50 points. A critical choice is up ahead:")
        self.health -= 50
        print("                Continue trying to escape  [Continue]")
        print("                Give up [Give up]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['continue', 'give up']):
                if op == 'continue':
                    self.print_slow("processing...")
                    self.path_M()
                    break
                if op == 'give up':
                    self.print_slow("processing...")
                    self.path_N()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_M(self):
        print("")
        self.print_slow("      As dawn breaks, the Keeper appears, his presence ominous in the eerie morning light. With a haunting ")
        self.print_slow("      smile, he extends an unsettling invitation a choice between a sandwich or a plate of hash browns. The")
        self.print_slow("      keeper unties him from the chair, but he is still tied. The air thickens with a sense of foreboding as")
        self.print_slow("      Tony weighs his options, unaware of the hidden intentions lurking behind this seemingly simple offer.")
        print("                Eat the sandwich  [Sandwich]")
        print("                Eat the hash browns [Hash browns]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['sandwich', 'hash browns']):
                if op == 'sandwich':
                    self.print_slow("processing...")
                    self.path_O()
                    break
                if op == 'hash browns':
                    self.print_slow("processing...")
                    self.path_P()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_N(self):
        print("")
        self.print_slow("      Tony couldn’t fight anymore with the nightmares. His valiant struggle for air ended as the suffocating  ")
        self.print_slow("      embrace of the thought silenced his fight, and his consciousness slipped away into the abyss.")
        self.print_slow("      loading . . .")
        self.Game_Over()
        return

    def path_O(self):
        print("")
        self.print_slow("      Tragically, Tony succumbed to the poisoned sandwich, the unsuspecting meal sealing his fate. As the")
        self.print_slow("      toxin took hold, his strength waned, and the world faded into darkness. His valiant efforts were in ")
        self.print_slow("      vain, lost to the sinister ploy hidden within the innocent offering.")
        self.Game_Over()
        return

    def path_P(self):
        print("")
        self.print_slow("      Despite the unsettling aura surrounding the hash browns, Tony, driven by fear yet clinging to a glimmer")
        self.print_slow("      of hope, consumed them. Each bite laden with trepidation, his heart raced with every swallow, unsure of")
        self.print_slow("      the consequences but determined to face whatever lay ahead.")
        print("                Take advantage of the situation and attack the keeper  [Advantage]")
        print("                do nothing  [Nothing]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['advantage', 'nothing']):
                if op == 'advantage':
                    self.print_slow("processing...")
                    self.path_Q()
                    break
                if op == 'nothing':
                    self.print_slow("processing...")
                    self.path_R()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_Q(self):
        print("")
        self.print_slow("      Tony, fueled by desperation, hurls the dish at The Keeper, initiating a fierce assault of kicks and punches ")
        self.print_slow("      until the assailant collapses. Seizing the opportunity, Tony bolts in a rush, fleeing from the cabin's clutches")
        self.print_slow("      in a bid for freedom.")
        print("")
        self.unlock_map()
        self.move_player()

    def path_R(self):
        print("")
        self.print_slow("      Tony's pulse quickens as the keeper's warning echoes in his mind. With time slipping away, he frantically")
        self.print_slow("      scans the room, seeking an escape route. Determined, he scours for hidden clues. The impending nightfall looms,")
        self.print_slow("      urging him to find freedom before it consumes him in eternal sleep.Tony has to find a way out before the ")
        self.print_slow("      night hits again, what should he do? ")
        print("                Get The Keepr’s attention back  [Attention]")
        print("                Find another way out  [Find]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['attention', 'find']):
                if op == 'attention':
                    self.print_slow("processing...")
                    self.path_S()
                    break
                if op == 'find':
                    self.print_slow("processing...")
                    self.path_T()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def path_S(self):
        print("")
        self.print_slow("      Tony started yelling until the keeper visited him one more time, Tony asked him about the truth,")
        self.print_slow("      why was he there, why him?, The keeper just laughed at him and told him he was part of his  ")
        self.print_slow("      masters plan, his master was hungry and he was his next meal, a sudden wave of dizziness gripped ")
        self.print_slow("      Tony, the resurgence of a fever igniting within him. The creature slithered back into his ")
        self.print_slow("      consciousness, leeching on his memories until they dwindled to nothingness, leaving Tony's mind ")
        self.print_slow("      a blank canvas, devoid of his once vibrant past ")
        self.Game_Over()
        return

    def path_T(self):
        print("")
        self.print_slow("      In a fit of frustration, he unleashed an attack of rage, furiously kicked the mattress and a hidden void beneath")
        self.print_slow("      the floor revealed itself, Without hesitation, he reached into the hollow and unearthed a rusted clasp-knife. He")
        self.print_slow("      He took it and use it to break the handle, lamentably the clasp-knife was too old and broke in the process.  He")
        self.print_slow("      didn’t look back and got to be free, however this isn’t over…")
        print("")
        self.unlock_map()
        self.move_player()

    def easter_egg1(self):
        file_path = r'Rasputin.mpeg'
        self.play_music(file_path)
        print("""

                    -%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    -%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    -%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#:::-#%%%=:::+%%:::::::::::+%@%=:::::::::-%@@#-:::::::::+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    -%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*   .+%%%-   :#%            +@+           :#@-           -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    -%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*    +%%%-   :#%    =**#.   =%+   :*##+   .*@:   -###-   :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    -%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*    +%%%-   :#%    +%%%.   =%+   :#@@*   .*@:   -%@@=   :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    -##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*    +%%%-   :#%    +%%%.   =%*    =%@%*==+#@-    *@@%+==+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    -########%%%%%%%%%%%%%%%%%%%%%%%%%%*    +%%%-   :#%    =***.   =%%#:    =%@@@@@@%+.   .+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    -****#######%%%%%%%%%%%%%%%%%%%%%%%*    +%%%-   :#%    :      .=%%%%#-    -#@@@@@@@*:    +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    -++******######%%%%%%%%%%%%%%%%%%%%*    +%%%-   :#%    =.   -**%%%%%%%#-    -#@@@@@@@*:   .=%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :++++++++***######%%%%%%%%%%%%%%%%%*    +%%%-   :#%    +#   .*%%%#===*%%%-   :#@+===#@@#:   -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :=++++++++++**######%%%%%%%%%%%%%%%*    +%%%-   :##    +%+   :%%%+   :*%%*   .*@:   -%@@=   :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :========+++++***#######%%%%%%%%%%%*    +###-   :##    +%%:   =%%+   :*%%*   .*@:   :%%%=   :%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :==========+=++++***###########%%%%*            :##    +%%#    *%*           :*%-           -%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :======-=====++++++****###########%%+:.........:+%%-..:+%%%*:..-#%*:........:=%%%=:........:+%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :======-======++++++++****########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :====----========++++++++***########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :===-------=========++++++++****#####%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :===--------==========+++++++++***######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :==----------===========++++++++++**########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :==-----------=====-=======+++++++++***#########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :==--------------===========++++++++*******#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :=---------------==============+++++++++******#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :==-------------------============+++++++++******#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                    :=---------------------=============+++++++++++***########%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@
                    :=-------------------------==========++++++++++++*****######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*=-===-=+*#%%@@@@@@@@@@@@@@@@@@@@
                    =@%*=----------------------============+++++++++++******######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*--::-=+=-::-*%@@@@@@@@@@@@@@@@@@@@
                    =@@@@+---------------------===============+++++++++++*****######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*---=+##+-::=*%@@@@@@@@@@@@@@@@@@@@
                    =@@@@@-----------------------==================+++++++******####%%%@@@@%%%%%%%%%%%%%%%%%%%%%%%%#++*#*#*-::-=*%@@@@@@@@@@@@@@@@@@@@
                    =@@@@@-----------------------===================+++++++++****##%@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%++*%#=::--=*%@@@@@@@@@@@@@@@@@@@@
                    =@@@@@------------------------=-=================+++++++++**#%@@@@@@%%%@@@@@@@@%%%%%%%%%%%%%%%%%*=++=-:----=+#@@@@@@@@@@@@@@@@@@@@
                    =@@@@@=------------------------=-==================+++++++*%@@#*+++******#%@@@@@%%%%%%%%%%%%%%%%*=----===---=*%@@@@@@@@@@@@@@@@@@@
                    =@@@@@+---------------::::---=-===+=----===+======+==+++++*@%*=--=*%%#***###@@@@@@%%%%%%%%%%%%%%%#**++=-:::::-+%@@@@@@@@@@@@@@@@@@
                    :=@@@@=--------------::::-=====*++**-=====++=========+++++++=+*++=+*++**++###%@@@@@@%%%%%%%%%%%%%%%%#*=-::.:::-*%@@@@@@@@@@@@@@@@*
                    :+@@@@=:::::---------::::-=++=*%#*##+=+++=========+====++*****+*+--::::-=+*###@@@@@@@@%%%%%%%%%%%%%%%%*=--=+*#%@@@@@@@@@@@@@@@@@@*
                    =@@@@@-::::::::------:::::::-++++****++=================++++------::::--=+*###@@@@@@@@@%%%%%%%%%%%%%%%%#%%%%%@@@@@@@@@@@@@@@@@@@@@
                    =@@@@@-:::::::::---::::---=+++******+==================+=-==++==-:::-=-==+**##@@@@@@@@@%%%%%%%%%%%%%%%@@@@@#+===+%@@@@@@@@@@@@@@@@
                    =@@@@%-:::::::::-:::::---+########*+===--==============+=+*==-----:-=----=+**#%%#%%@@@@@%%%%%%%%%%%%%%%@@#=:::--=+%@@@@@@@@@@@@@@@
                    =@@@@%:::::::::::::::::-+###+=============-===========++==::::::::-==----=+*###*****+#@@%%%%%%%%%%%%%%%@%=-:::---=*%@@@@@@@@@@@@@@
                    =@@@@#::::::::::::::::-=#%#=----=========================--::----=++=====+*#%#+=*+=+*#@@###%%%%%%%%%%%%%%+--::---==*%@@@@@@@@@@@@@
                    =@@@@*:::::::::::::::-=#%#+------=========================+*######********#%%%%%%#%%@@@%######%%%%%%%%%%%*=-::----=+#%@@@@@@@@@@@@
                    =@@@@*::::::::--::---=*%%+------========================*%%%%%%%%%%%%%%%%%%%**#%@@@@@@%#########%%%%%%%%%*=-------==+#%@@@@@@@@@@@
                    =@@@@+:::::::--:::-==*#%+--------========================*%@%%%%%#######******#%@@@@@@###########%%%%%%%%#=--:-----=+*%@@@@@@@@@@@
                    =@@@@+:::::::--::--=*#%*---------==========-==============+#%%#**+++++++++++*#%%@@@@@#############%%%%%%%#+--------==+#%@@@@@@@@@@
                    =@@@@=:::::---::--=*###-------------===-==================+++**==-====+====+*#%@@@@#**####*########%%%%%%#+=-------==+*#%@@@@@@@@@
                    =@@@%-:::::--::--=+*#%+------------====-===================++++===========++*#%@@%***#################%%%#*=-------==+*#%@@@@@@@@@
                    =@@@*:::::==----=+*#%%--------------=-=--=================+++++===--===-==+**#%%%#****#################%##*==------==++*#%@@@@@@@@
                    =@@@=:-:-==----==+*#%%----------------=--=================++++++--------==++*#%########################%###+==-----==++*#%@@@@@@@@
                    =@@%-----==----=+*##%@%+-----------------==-==============+++=====---:--===++*#***#########################+===---===++**%%@@@@@@@
                    =@@#----===--==+*##%%@@%+-----------------=---======+**+==+**+------:::---====+*########################%%%*=========++**#%%%@@@@@
                    =@@#+========++**##%%@@@#---------------===++**######%%%%*####+-:::::::-::--+*#%%##########################*+========++**#%%%%@@@@
                    =@@@@@#=====++**###%@@@@%%%#**+=====+++*#############%###########*+++++++*####%############################*++++++==+++**##%%%%%@@
                    =@@@@@+=++++++**##%%%%%%***#########################%#######################################################*++++++++++**##%%%%%%%
                    -@@@@#++++++++**##*+===*##################################################################################*+**++++++++++*#%%%%%%%%
                    =@@@@+====+++++++===---=###################***+++==========++++***###################################%###*=++++++++++++**#%%%%%%%%
                    -@@@#++====++===========*###%%#%%%#%#%#+-::::-------::::::::::::::::-=*#########################%##%%%###*++++++++**###%%%@@%%%%%%
                    -@@@@%%#*+***************#%%%%%%%%%%#%#-=---::::::::::::::::::::::::::=*###**##################%%##%%%%#%########%%%@@@@@@@%%%%%%%
                    -@@@@@@@@@%%%%%%%%%%%%%##%%%%%%%%%%%%%%%=:::::::::::::::::::........:-####**=*##%%############%%%%%%%@@%%@%@@@@@@@@@@@@%%%%%%%%%%%
                    -@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%#*:::::::::..................:*########%%###############%%%%@@@@%%@@@@@@@@@@@@@%%%%%%%%%%%%
                    -@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@%####-::::::...................:-######%%#################%%%%%@@@@@%@@@@@@@@@@@@%%%%%%%%%%%%%
                    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%@@@@%####=::::::::................::+#########################%%%%@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%
                    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%####+:::::::::::::::::::::::::-####****++++++*****#######%%%@@@@%%%%@@@@@@@@@@@%%%%%%%%%%%%%%
                    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@%####*:::::::::::::::::::::::::-:::::::::::::::::::-+####%%%@@@%######%@@@@@@@%%%%%%%%%%%%%%%%
                    -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#####::::::::::::::::::::::::--:::::::::::::::::::-#####%%@@@%########%%%%%%%%%%%%%%%%%%%%%%%
                    -#*+==============++*#@@@@@@@@@@@@@@%#####-::::::::::::::::::::::---::.........::::::::*####%%%@@@%#########%%%%%%%%%%%%%%%%%%%%%%
                    -%=------------------*@@@@@@@@@@@@@@%#####+:::::::::::::::::::::--=*::.........:::::::-#####%%%@@@%########%%%%%%%%%%%%%%%%%%%%%%%
                    =@*-::::::::::::----+@@@@@@@@@@@@@@@######*:::::::::::::::::::::--+#-::......:::::::::-####%%%%@@@%########%%%%%%%%%%%%%%%%%%%%%%%
                    =@#-:::::::::::-----%@@@@@@@@@@@@@@@#######-:::::::::::::::::::--=*#=::...:::::::::::-+####%%%%@@@######%##%%%%%%%%%%%%%%%%%%%%%%%
                    =@%-::::::::::-----+@@@@@@@@@@@@@@@@#######=::::::::::::::::::---=##*:::::::::::::::--*####%%%@@@@#########%%%#%%%%%%%%%%%%%%%%%%%


        """)

    def easter_egg2(self):
        file_path = r'stranger_things.mp3'
        self.play_music(file_path)
        print("""
                                                                             :=++**:                                      
                                                                          .-=*#%%%#+.                                     
                                                                     ..:-=*#%%%%%%%%=.                                    
                                                                   .:-=+#%#++#%#***#%*-.                                  
                                                                 .:-+######::*%%%=-#%%#=:                                 
                                                 ..::::..       .-+*%*-.-*%*.+%%%%+-+#%%*:                                
                                            ..:::--=========:   =+#%@%#-.*%%##%%%%-:-#%%#*.                               
                                          .::-=*#%##%%%######*.:*%%%%%%@%%%%%%%%%%++%%%%%#=                               
                                       .::=*##%%%*=-*%%%%%%%%%%=#%%*=-+%@%%%%%%%#%%*==#%%%* ::---------::::.              
                                    .:-=*%###+=*%*-..#%%%%%%%%%%%%#+..-@@%%%#%##%%%=.-+%%%#*++****++++===--:::.           
                                 .:-+*##*##%#-::-%#+:+%%%%%%%%%%%@%%#=*%%%%%%%##%%%:=*%%%%##%%%#####%*++###*+=-::.        
                                :=*%#%#=--#%%%#*+%%%%%%%%*++%@%@%%#*##*###%%%%%%#%%#%%%###%%%%%=:-+%*::-+%%#**#*=-::      
                               :*####%#=:.-%%%%%%%%%%%@%%*-.*@@%%########**##%%%%#%%%%###%%%%%#..:#%:-+#%%%--+*###*=-:.   
                                -##%##%#=..*%%%%%%%%@@@@@@@%%%#%%%##***+-.+**+-###%%%######%%%+.=%%%%%%%%%==+#%##++*#*=:. 
                                 -###%%%##+%%%%%%%%%%%%%@@@%%%#####+:.**=.=%#-:***+#%%%%%%%%%%*###%%%%##%#%#####=.:=*%%*=:
                                  =#%%#=--+%%%%%%%%%%%@@@%%%#*##**+*: +%@#@@@%*#=.:#%%%%%%%%*####%%####*##%#####..=#%%%%%*
                                   -*#%#**+*#%%%%%%%%%%@%%###=*#=:=#@+%@@@@@@@@@%.*###%%%%%%###%###****+****#%##=+=*##%%%#
                                    -+#%%#-..:=%%%%%%%%%#*###+*+*=-@@@@@@@@@@@@@@%%:-+%%%%%%#*#%%#*+#**+****##*+=-:=**####
                                     -+*##+-=+*###%@%%@%%%%%%#*#%@@@@@@@@@@@@@@@@@@+*%%%%%%%%*%%%##+#############********=
                                      :+*#%%%#=--=#%*-:*%%%#%%#%@@@@@@@@@@@@@@@@@@@@%%%%%%%%%#*%%%%%##%#%%#+==+*#*++**=:  
                                       .-+##%%=:::+:  :%%%%##%##%@@@@@@@@@@@@@@@@@@@%%%%%%%#%##%%%%#**###%*---+*****-     
                                          .-=+*+=++##%%%%#*%%###%%@@@@@@@@@@@@@@%%%##%%%%%%+. :+#%#%=--**%%%#****=:       
                                                -=+***%%%%%%#*-+*#%%%@@%@@@@@%#%%##*#%%%%%##*-::=*#*.::*#*****+:          
                                               :-+#+:..-%%%%%:-**#%%##*#%%####***+==+*=%#%%%%%##***--++##*=-:             
                                              .:-#%+:.:+%@@@@+*##%%%%+-*#**==**++=::-:-%%%###--+**+- ...                  
                                              .:=**#%#%%%%%%%%%%%%%%###%###*#%#**+=--*%%%###*++*#++=                      
                                              :-*-:..-+#%%%#####**#%%%%%##%%%%####+*%###*+++**#%%%*=.                     
                                             .:=%#*+***#%%%%#####***##%%%#%%######+=***+*+++**###*+=:                     
                                             .-*##%%%###%#########*##%%@@####++*######*#**++++*--=+=-                     
                                   ..:..  .=.:=*-:=#########*###*=--=*%@@%##=*#######******==+*###%+-                     
                                 :-=+***++##.:+#=-=######%#*###*+=--=*%%@##==+#%###******+*+++*%%##*=.                    
                               :==-=+**##### :+#**###%%%######*--**####%%**+**%%##*****+++++**+::-+*=:=-.                 
                             :=====--=+**##+.-=-..:-+%%#%*.:#*=-=*##***%%++++**=:=#*+++=+++***#**#%#=:#*+=:.              
                           :=++++++++=---+*=.-+#*#%%%#--*---#%####*+*#@@@@#==*+==*#**++++++++****###+:#**+-:              
                        .:=++*****+++*++=--:.-+#####*=-+##**###***#%%%%%@@%%*===*#**+-=*+++=**-.:.:++:***+++=:.           
                      .-=+=====++***+++**+=-.-+#***#***********#%%%%%%#%%@%%##+=--=++=+***+.+*#*++**+:*****+++=.          
                     .=----=====+++++++==++= :+*+++++******##%%%%%%%%%##%%%##*+***=--==*##+-=*####%*-:*####*+++=.         
                    .=-----------====++++-==-.-=++****#####*###%%%%%#***####**++#%%#*+=---===++**##*=:*####*#++=.         
                   .--------::.::-========-:---=+++**+****#######%%%*==+*####*+*##%%###*+**+=:--=+*+-:*######*+=.         
                   :=------::..::--===+=====::.-=++****++==+==**#####*=+****#*+*#####*+#%%%%%#*+=:--:=%######**-          
                  .-=------:::.:---========+--::-+*####***#****+++++*****++****+***++#%%%#########*+##%%%%%%#**-          
                  :==--------:----===++=====---:-+*##**++++++++***+==-==++****++++=+*###*********##**%%%%%%%###:          
                  :+===========++++++++++++-==--=*#**+************++++===-=*#*+++===++**+++++++++***++#%%%###*#.          
                  .++====+++++++*******#*+==--.:=**+++==+++++==============+##*+======++++++++++++++++#%@%%##**           
                  .+++++++****##**#####*++==-:.:=+===---==----====-----====+*#*+=====++++++++++++==+#%%%@%%#*+#-.         
                   =*++***##******####*+==---::.--==-------------------=====*#*++===+++++++++++==+*#@@@%%%##%+**+-        
                   :*+****++++++*####****+==--::.:::---------------=--=--===+*#*++==+++++++++=+++++%@@@%%%###+=##+.       
                    =****+++**##%#**##%@@@%%#**++==-::::-:------------=---===+#++===++++++++++++++*@@@@@%%%%#+++#%-       
                    :******###*+=-=+#%#%@%%####**++==--::-:::::-----------===+**=+++++++++++++++++*%@@@%%%%##*+=*#:       
                    .+++*##*+==-==+*#**%@%###*##*#*+=--::::::-------=======+++***++********++++*#*+%%@%%%%%%###=+#:       
                    :=++**====--=+*##.+%%####****++*+==--:::::----===++++******-=#*####%%%%####**++%%%%%%%%%%###+*=       
                    :=+**=-----==+##=  ==#*#**++*+===+++++==--==++**########*+---*#%%%###**+++++=+++##%@%%%%%%##%##:      
                   :-=*+===--===+*##    =##**#*+++==-:-===++*****+********++=---:=*###****+++++++==+*#%%%%%%%%%%###+:     
                   --=*====--=+++##:    +*******+===-::::::---=====++++++===------+++*++++++++*++++:+##%%%%%%%#%%%%%#     
                  .=-++=======++*#=     =*******+==--::::::::-----=========---:::-+**++=========++*. -##%@%%%%%%%%%%#+: 
        """)

    def End_Game(self):
        file_path = r'lavender.mp3'
        self.play_music(file_path)

        self.print_slow("      Tony calls his mom, 'Hi… Hi… mom?... are you there?' Tony’s mom answers with a broken voice, 'Honey, so ")
        self.print_slow("      good I can hear your voice. Where are you? What happened? …I…I miss you so much. ")
        print("")
        self.print_slow("      Tony answers, 'Mom, I’m in a place called the Soulless Forest. I woke up in a strange cabin. I managed to")
        self.print_slow("      escape, but I don’t know what to do. …I’m afraid, mom. I need you.' ")
        print("")
        self.print_slow("      The call is jamming, and an evil voice starts mumbling, 'What’s up, little guy?' (The Keeper is talking to")
        self.print_slow("      Tony) 'I’m going to find you. Where are you…? Where are you…? Tony, where are you…? Oh! I think I see you. '")
        print("")
        self.print_slow("      Tony starts running, dodging many trees on his way. He thinks he’s safe, but he’s not. He finds himself on ")
        self.print_slow("      a dead-end path. ")
        print("")
        print("""
                                          ███████╗██╗███╗   ██╗ █████╗ ██╗                  
                                          ██╔════╝██║████╗  ██║██╔══██╗██║                  
                                          █████╗  ██║██╔██╗ ██║███████║██║                  
                                          ██╔══╝  ██║██║╚██╗██║██╔══██║██║                  
                                          ██║     ██║██║ ╚████║██║  ██║███████╗             
                                          ╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝             
                                                  
                                    ██████╗  █████╗ ████████╗████████╗██╗     ███████╗
                                    ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝
                                    ██████╔╝███████║   ██║      ██║   ██║     █████╗  
                                    ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  
                                    ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗
                                    ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝
        """)

    # crear historia y minijuego final

    def Game_Over(self):
        file_path = r'C:\Users\lloyd\Downloads\Y2meta.app - Billie Eilish - lovely (with Khalid) Audio (128 kbps).mp3'
        self.play_music(file_path)
        print("""


                              ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
                             ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
                            ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
                            ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
                            ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
                             ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
                              ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
                            ░ ░   ░   ░   ▒   ░      ░      ░   
                                  ░       ░  ░       ░      ░  ░
                                    
                             ▒█████   ██▒   █▓▓█████  ██▀███    
                            ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒  
                            ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒  
                            ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄    
                            ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒  
                            ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░  
                              ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░  
                            ░ ░ ░ ▒       ░░     ░     ░░   ░   
                                ░ ░        ░     ░  ░   ░       
        
                     
        """)
        time.sleep(27)

    def Title(self):
        file_path = r'everything i wanted.mp3'
        self.play_music(file_path)

        print("""
                         
         
                          /=================================================================\
                                                                    
                          ||  ▄████████    ▄████████ ▀█████████▄   ▄█  ███▄▄▄▄              ||
                          || ███    ███   ███    ███   ███    ███ ███  ███▀▀▀██▄            ||
                          || ███    █▀    ███    ███   ███    ███ ███▌ ███   ███            ||
                          || ███          ███    ███  ▄███▄▄▄██▀  ███▌ ███   ███            ||
                          || ███        ▀███████████ ▀▀███▀▀▀██▄  ███▌ ███   ███            ||
                          || ███    █▄    ███    ███   ███    ██▄ ███  ███   ███            ||
                          || ███    ███   ███    ███   ███    ███ ███  ███   ███            ||
                          || ████████▀    ███    █▀  ▄█████████▀  █▀    ▀█   █▀             ||
                          ||                                                                ||
                          ||    ▄████████    ▄████████  ▄█    █▄     ▄████████    ▄████████ ||
                          ||   ███    ███   ███    ███ ███    ███   ███    ███   ███    ███ ||
                          ||   ███    █▀    ███    █▀  ███    ███   ███    █▀    ███    ███ ||
                          ||  ▄███▄▄▄      ▄███▄▄▄     ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ||
                          || ▀▀███▀▀▀     ▀▀███▀▀▀     ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ||
                          ||   ███          ███    █▄  ███    ███   ███    █▄  ▀███████████ ||
                          ||   ███          ███    ███ ███    ███   ███    ███   ███    ███ ||
                          ||   ███          ██████████  ▀██████▀    ██████████   ███    ███ ||
                          ||                                                     ███    ███ ||
                          ||                                                                ||
                          \=================================================================/
        """)

        print("""
                                                  █▀▀ ▀█▀ █▀█ █▀▄ ▀█▀
                                                  ▀▀█  █  █▀█ █▀▄  █
                                                  ▀▀▀  ▀  ▀ ▀ ▀ ▀  ▀                                         
        """)

        while True:
            start = input("Type Start: ")
            st = start.lower().strip()

            if any(keyword in st for keyword in ['start']):
                if st == 'start':
                    self.print_slow("loading...")
                    self.Instructions()
                    break
            else:
                self.print_slow("Looks like you're not too smart to type...\n")
                time.sleep(1)

    def Instructions(self):
        print("")
        print("""
                                    ▀█▀ █▀█ █▀▀ ▀█▀ █▀▄ █ █ █▀▀ ▀█▀ ▀█▀ █▀█ █▀█ █▀▀
                                     █  █ █ ▀▀█  █  █▀▄ █ █ █    █   █  █ █ █ █ ▀▀█
                                    ▀▀▀ ▀ ▀ ▀▀▀  ▀  ▀ ▀ ▀▀▀ ▀▀▀  ▀  ▀▀▀ ▀▀▀ ▀ ▀ ▀▀▀
         """)
        self.print_slow("        Hey there, friend! Welcome to this twisted tale—it's a mix of entertainment, horror, and sheer")
        self.print_slow("        confusion...hope you enjoy the ride, understand the road and take the best path. ")
        self.print_slow("        Your adventure starts with 100 points of health, if the game you want to continue palying ")
        self.print_slow("        recommended is your health mantaining. Bonne chance!")
        print("")
        self.print_slow("        When faced with choices, just type the suggested word to make your selection and discover the optimal")
        self.print_slow("        path ahead. Your options will show after a sequence, the suggested word will be betweeen brackets.")
        self.print_slow("        For exmaple: What do you like?")
        self.print_slow("        To eat pizza [pizza]")
        self.print_slow("        Playing Cabin Fever [playing]")
        self.print_slow("        word typed: playing ")
        print("")
        self.print_slow("        LET THE ADVENTURE BEGIN! ")

        print("")
        self.Start_game()

    def Start_game(self):
        print("""
               
                     ................................................................................
                     ........................=+*+++:.................................................
                     .......................*++**++#-................................................
                     .......................%*######*:...............................................
                     .......................+%*****+++**+++=-........................................
                     .......................******#*##**+++++**+++=-:................................
                     .....................:=*#**#*******+*******+++++**++==-.........................
                     ....................+#****###*******+++++=++****#**++++**+-.....................
                     ...................-#*#**#*++##***###*******++++++++**#***%=....................
                     ...................=##**#*++++##**#*###******##******++*++**+...................
                     ................=:+#**##*+++++*###*****#*+++==+++**+****#**###..................
                     ...............:*#***##**#*+******#*****##*****++++**+++++++***++=:.............
                     ...............=##**##+*#*===+**#=+*#***###*#*******************++**:...........
                     ..............=######++*#*===+#*#+++*##**#######################***+%...........
                     ............:#***##*+==+#***+***#====++##*##**##**************#######+-.........
                     ............:#*###%++==+****#**#+++++++**#*#***############*#*********#-........
                     .............%##%%*+++++++++++++++++=====+*##*#**********##############-........
                     ............++###%-============+++++=======+*##+**+******+++**+++*+#%%..........
                     ...........-#**#*%++++++++**++++++++=#*=+++*++****##*######*##**+*+#+:..........
                     ............*****#%+++++++*#*******#+#*+++++******##############*##*............
                     ...........=*+***#+======*##+=====+*+**=====++*++*###**#**######%#*#=...........
                     ..........#*+****#*======*##**+===+#+**++===+++***#####*######+++#*=:...........
                     .........-#*******%+++++=*##*****++#+**++*+**+#***######*#####***#..............
                     .........:+#++***#*===*##*********###**=====++****#######*####****+.............
                     ...........+***+*#*===+##*********###*++====+**++*#####*######++++#.............
                     .........:**+*+***%***+##*+++*+++++##*+++++++**++*####****####***#+.............
                     .........-#*****+#=====##*========+##**+**********###*****####***##+:...........
                     ........-+**++***%+++=+##*++++=====#%*+=====****+*####****####****####..........
                     ........##*****#*#%****###***+++++*##**++**###***+*##********+****####..........
                     ........:+##%####*%++*#***********###***#**+++#******++++*****#######*=-........
                     ........=#**#######%##*******######*****#++++**##*******#***#####*#%**++-.......
                     ........-=+**+#**%########***#####%##*+*#*+++++*###*+*##########%###+++=........
                     .........:--====%**********#######**#****#**#***###%######%#***+++==-:..........
                     .............:-=+*########%###****####%*****#######*++=+++======--:.............
                     .................:-==+++++**++========+*****++============---:..................
                     .......................:::----=================-----::::........................



        """)
        self.print_slow("      Tony wakes up on a foreign cabin, he doesn’t remember anything at all and finds out he is tied, there is a ")
        self.print_slow("      night stand near him, a glass highlights from it, Tony looks around, a spring is protruding from the mattress, ")
        self.print_slow("      he is desperate to get free. What should Tony do? ")
        print("                Break the glass and use a piece to cut the rope [Break]")
        print("                Use the spring to cut the rope [Cut]")

        while True:
            option = input("Type: ")
            op = option.lower().strip()

            if any(keyword in op for keyword in ['break', 'cut']):
                if op == 'break':
                    self.print_slow("processing...")
                    self.path_A()
                    break
                if op == 'cut':
                    self.print_slow("processing...")
                    self.path_B()
                    break
            else:
                print("Not the word we're looking for\n")
                time.sleep(1)

    def unlock_map(self):
        print("""
                     ▄▄·        ▐ ▄  ▄▄ • ▄▄▄   ▄▄▄· ▄▄▄▄▄▄• ▄▌▄▄▌   ▄▄▄· ▄▄▄▄▄▪         ▐ ▄ .▄▄ ·     ▄▄ 
                    ▐█ ▌▪▪     •█▌▐█▐█ ▀ ▪▀▄ █·▐█ ▀█ •██  █▪██▌██•  ▐█ ▀█ •██  ██ ▪     •█▌▐█▐█ ▀.     ██▌
                    ██ ▄▄ ▄█▀▄ ▐█▐▐▌▄█ ▀█▄▐▀▀▄ ▄█▀▀█  ▐█.▪█▌▐█▌██▪  ▄█▀▀█  ▐█.▪▐█· ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄    ▐█·
                    ▐███▌▐█▌.▐▌██▐█▌▐█▄▪▐█▐█•█▌▐█ ▪▐▌ ▐█▌·▐█▄█▌▐█▌▐▌▐█ ▪▐▌ ▐█▌·▐█▌▐█▌.▐▌██▐█▌▐█▄▪▐█    .▀ 
                    ·▀▀▀  ▀█▄▀▪▀▀ █▪·▀▀▀▀ .▀  ▀ ▀  ▀  ▀▀▀  ▀▀▀ .▀▀▀  ▀  ▀  ▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪ ▀▀▀▀      ▀ 
                    
        """)

        self.print_slow("      You've unlocked the next stage. Welcome to the Soulless Forest. Navigate by typing 'left,'right,' 'up,' or ")
        self.print_slow("      'down.' You now have an inventory to store items; it starts with a single slot, but maybe you can expand it.")
        self.print_slow("      'Suggestion: draw a map on which ever desired place because there won't be shown any map.")
        print("")
        self.print_slow("      Best of luck with the looming mysteries ahead. Survival is in your hands. ")
        print("")
        print("")

    def move_player(self):
        while True:
            x, y = self.player_position

            if self.health > 100:
                self.health = 100

            if self.player_position == [9, 4]:
                self.End_Game()
                self.print_slow("Starting . . .")

            if 0 < self.health <= 100:
                option = input("Type 'up', 'down', 'left', or 'right' to move ").lower().strip()

                if option in ['up', 'down', 'left', 'right']:
                    if option == 'up' and x > 0 and self.map[x - 1][y] != 1:
                        self.player_position = [x - 1, y]
                    elif option == 'down' and x < len(self.map) - 1 and self.map[x + 1][y] != 1:
                        self.player_position = [x + 1, y]
                    elif option == 'left' and y > 0 and self.map[x][y - 1] != 1:
                        self.player_position = [x, y - 1]
                    elif option == 'right' and y < len(self.map[0]) - 1 and self.map[x][y + 1] != 1:
                        self.player_position = [x, y + 1]
                    else:
                        print("Hold up! There's tree")
                        continue  # Continuar pidiendo input si el movimiento no es válido

                    # apples
                    apple_positions = [[1, 0], [3, 8], [7, 3], [9, 2], [9, 7]]
                    if any(pos == self.player_position for pos in apple_positions) and self.player_position not in self.visited:
                        print("""
                                    .................................................................
                                    ........................................*+=......................
                                    .......................................*@%-......................
                                    .......................:--=--:::------*%*........................
                                    ..................:-+**+=-:......:-=+##++===-....................
                                    .............:-=*#**+++=--::::-----+#*-::::-=++-:................
                                    ...........:=++++============+++++*@#++==-:::-+++=--.............
                                    .........:-+*#*+==-:..:-===--=++**%%#*+++===--=====+*=-..........
                                    ........:+#%%%#*==-::::-==----=+*%##*=-----:::::::-=++++=........
                                    .......:*%%%%%#+==---:::.....:::::--::::::.......:::-==+**-......
                                    ......:+%%%%%%%#*+===--::........................:::---=+**=.....
                                    .....:=*##%##%%%%%%#**++=-::::...............::::::----==+**-....
                                    ....:-+****####%%%%@%%%%%##*+==-----:::::------====------=+**....
                                    ....-++***#####%%%%@@@@@@@%%%%%%####*****++++**++++==--:--=+*-...
                                    ...:=++***#####%%%%%%@@@@@@@@@@@@@@@@%%%%%%###**++===-:::--+*+...
                                    ...:=+**#####%%%%%%%@@@@@@@@@@@@@@@@@@@@@@%%#***+++=--::::-+*+...
                                    ...:=++*######%#%%%%%@@@@@@@@@@@@@@@@@@@@%%##****++=--::::-+*+...
                                    ...:=++*##%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@%%####****+=-::::--+*+...
                                    ...:=++**###%%%%%%%%%%@@@@@@@@@@@@@@@@@@%%%####***+=-::::-=**:...
                                    ....-++***###%%%%%@@@@@@@@@@@@@@@@@@@@@@%%####***+=--::::-=*+....
                                    ....:=++***#####%%%%@@@@@@@@@@@@@@@@@@@@%####****+=-::::-=*#:....
                                    .....-++***########%%%%@@@@@@@@@@@@@@%%%%####***++=-::::-+#-.....
                                    ......-++***########%%%%%@@@@@@@@@%%%%%#####****+=--::--+*=......
                                    .......-+++**#########%%%%%%%%%%%%%%%%#####****+==-::--+*-.......
                                    ........-+++**########%%%%%%%%%%%%%%######****+==----=++:........
                                    .........:=++***#######%%%%%%%%%%%%#######**++==---==+=..........
                                    ...........-+***######%%%%%%%%%%#########**+++====+++-...........
                                    .............-+#####%%%%%%%%%%%%%#######***++++++++-.............
                                    ...............:=*%%%%%%%%%%%%%%%%%######*******+-...............
                                    ...................:-=+#@@@@@@%%%%%%%%%######+=:.................
                                    .........................:=*#%%##***+**+++=-.....................
                                    .................................................................

        
                        """)
                        self.print_slow("You've come across an apple. It restores 5 health points. Would you like to enjoy it now or come back for it later?")

                        while True:
                            if self.health < 100:
                                option = input('>').lower().strip()
                                if option in ['yes', 'eat', 'enjoy', 'no', 'later', 'now']:
                                    if option in ['yes', 'eat', 'enjoy', 'now']:
                                        self.print_slow("Delicious! You ate an apple, and your health increased by 5 points.")
                                        self.health += 5
                                        self.visited.append(self.player_position)
                                        if self.health > 100:
                                            self.health = 100
                                        break
                                    if option in ['no', 'later']:
                                        self.print_slow("Alright, maybe later.")
                                        break
                                else:
                                    self.print_slow("You cant do that right now.")
                            else:
                                self.print_slow("Seems like you don't need to restore health right now. You're all good! Feel free to come back later if needed.")
                                break

                    # screwdriver
                    if self.player_position == [2, 1] and self.player_position not in self.visited:
                        print("""
                                                                                                 
                                                                 
                                                                                  .=*#*.     
                                                                               :=**+++*%     
                                                                               #*+++++%.     
                                                                              **++*##%=      
                                                                            =*--#%%+-.       
                                                                          =*=-*##-           
                                                                        =#+-+##+             
                                                                      -*+==*#*.              
                                                                    -**==*#*:                
                                                                  -#*==**#-                  
                                                           .... :**==**#+                    
                                                         =%#%*#%*+=**##.                     
                                                        .@**@**%+***%-                       
                                                        +@#-=%%*###%+                        
                                                  :--=+#*#@%+-=#%###@                        
                                               =+***++++++*#%%*==+*%+                        
                                            .=*-:+#*++:+******%%++-.                         
                                           +*-:*#*++**#=-+###@*                              
                                        .=*--*#*+**+:-#*+=-*%#                               
                                      :++--*#*+**+::##*+**#*@:                               
                                    :*+-=##*++++::#%*+*#**%@#                                
                                  :**+=##*++++--*#*+*#**%@%-                                 
                                 :%#+##*+**+:-*#*+*#**%@%=                                   
                                 *###*+**+--##*+*#**@@@=                                     
                                 **++##*--*#*++**#@@%=                                       
                                 :#+%#==##*++++#@@%-                                         
                                  *#*%##*+*#+*@@@-                                           
                                   :+*##*+#@@@%-                                             
                                       .:--==:                                               
                                                                
                        """)
                        self.print_slow("      You have found a screwdriver, this tool is your key to unraveling mysteries, to unlock secrets. Its power lies ")
                        self.print_slow("      not in brute force,  but in finesse and precision.")
                        print("")

                        self.print_slow("Would you like to take the screwdriver with you?: ")
                        while True:
                            option = input('>').lower().strip()

                            if option in ['yes', 'no', 'take', 'leave']:
                                if option in ['yes', 'take']:
                                    if self.max_cap == self.current_space:
                                        self.print_slow("Sorry, you're already carrying too many things. You can't carry more items.")
                                        if self.max_cap == 1:
                                            self.print_slow("There must be a way to store more items.")
                                        break
                                    else:
                                        self.print_slow("You picked up the screwdriver. Maybe it will come in handy...")
                                        self.inventory.append('screwdriver')
                                        self.visited.append(self.player_position)
                                        self.current_space += 1
                                        break

                                if option in ['no', 'leave']:
                                    self.print_slow("Alright, maybe later.")
                                    break
                            else:
                                self.print_slow("You cant do that right now.")

                    # first easter egg (first part)
                    if self.player_position == [1, 8]:
                        print("""
                                    .%%..%%...%%%%...%%..%%...........%%%%....%%%%...%%..%%.
                                    ..%%%%...%%..%%..%%..%%..........%%..%%..%%..%%..%%%.%%.
                                    ...%%....%%..%%..%%..%%..........%%......%%%%%%..%%.%%%.
                                    ...%%....%%..%%..%%..%%..........%%..%%..%%..%%..%%..%%.
                                    ...%%.....%%%%....%%%%............%%%%...%%..%%..%%..%%.
                                    ........................................................
                                    .%%%%%%...%%%%...%%..%%...%%%%...%%..%%.                
                                    ...%%....%%..%%..%%..%%..%%..%%..%%..%%.                
                                    ...%%....%%..%%..%%..%%..%%......%%%%%%.                
                                    ...%%....%%..%%..%%..%%..%%..%%..%%..%%.                
                                    ...%%.....%%%%....%%%%....%%%%...%%..%%.                
                                    ........................................                
                                    .%%%%%...%%%%%%..%%..%%...%%%%...%%..%%..%%%%%..        
                                    .%%..%%..%%.......%%%%...%%..%%..%%%.%%..%%..%%.        
                                    .%%%%%...%%%%......%%....%%..%%..%%.%%%..%%..%%.        
                                    .%%..%%..%%........%%....%%..%%..%%..%%..%%..%%.        
                                    .%%%%%...%%%%%%....%%.....%%%%...%%..%%..%%%%%..        
                                    ................................................        
                                    .%%%%%%..%%..%%..%%%%%%.                                
                                    ...%%....%%..%%..%%.....                                
                                    ...%%....%%%%%%..%%%%...                                
                                    ...%%....%%..%%..%%.....                                
                                    ...%%....%%..%%..%%%%%%.                                
                                    ........................                                
                                    .%%%%%%...%%%%...%%%%%...%%%%%%..%%..%%.                
                                    .%%......%%..%%..%%..%%....%%....%%..%%.                
                                    .%%%%....%%%%%%..%%%%%.....%%....%%%%%%.                
                                    .%%......%%..%%..%%..%%....%%....%%..%%.                
                                    .%%%%%%..%%..%%..%%..%%....%%....%%..%%.                
                                    ........................................                                       
                        """)

                        print("")
                        self.print_slow("Type your guess or type 'Out' to not take the quest: ")
                        while True:
                            option = input().lower().strip()
                            if option == 'space':
                                self.player_position = [3, 0]
                                break
                            if option == 'out':
                                break
                            else:
                                print("Give it another thought\n")
                                time.sleep(1)

                    # first easter egg (second part)
                    if self.player_position == [3, 0]:
                        if self.player_position not in self.visited:
                            self.visited.append(self.player_position)
                            self.easter_egg1()
                            self.print_slow("      Oh there's something else I've got to tell you.")
                            self.print_slow("      Alexei Dimitrievski (The Keeper), once a brilliant scientist of the USSR, delved into mind control experiments")
                            self.print_slow("      gone away. His ambitious pursuit led to a catastrophic mishap when a machine designed to manipulate minds backfired.")
                            self.print_slow("      A being from a distant world seized the opportunity, intertwining its essence with The Keeper's consciousness.")
                            print("")
                            self.print_slow("      This entity, reliant on feeding off others' thoughts to sustain its existence, spurred The Keeper to abduct unsuspecting")
                            self.print_slow("      individuals. The captive souls become tormented victims, subjected to nightmarish fever dreams as the creature devours ")
                            self.print_slow("      their very thoughts.")
                            print("")
                            self.print_slow("      Driven by an insatiable hunger for intellect, The Keeper and the fused entity weave a dark tapestry of torment, trapping")
                            self.print_slow("      innocent minds within a labyrinth of nightmares, perpetuating their own survival at the cost of others' mental essence.")
                            print("")
                        else:
                            self.print_slow("      Seems like you know a lot. Go back where you came from.")

                        while True:
                            option = input("To exit, type 'exit':")
                            if option == 'exit':
                                self.player_position = [1, 8]
                                break
                            else:
                                self.print_slow("You cant do that right now.")

                    # second easter egg
                    if self.player_position == [9, 9]:
                        print("")
                        self.print_slow("      Complete the three riddles to unlock the secret:")
                        self.print_slow("      First riddle:")
                        self.print_slow("      This suspense/science fiction series takes place in a made-up town in Indiana in 1983. The name of this iconic")
                        self.print_slow("      place is similar to the name of a bird. The bird in question belongs to the family Accipitridae. They are mainly")
                        self.print_slow("      woodland birds that hunt during the day and have high visual acuity. They are known for their sharp talons and beak.")
                        self.print_slow("      Guess the name of the town:")
                        print("")

                        while True:
                            option = input("Type your guess: ").lower().strip()
                            if any(keyword in option for keyword in ['hawkins']):
                                print("")
                                self.print_slow("      Very nice! You have completed the first riddle.")
                                self.print_slow("      Second riddle:")
                                self.print_slow("      I am a shadow, a whisper in the night, I follow a number through her mind. I am the between worlds might.")
                                self.print_slow("      I control the hive, Who am I, that brings Hawkins and soon the world, in such pain?")
                                self.print_slow("      Guess its name:")
                                print("")
                                while True:
                                    option = input("Type your guess: ").lower().strip()
                                    if any(keyword in option for keyword in ['vecna']):
                                        print("")
                                        self.print_slow("      Oh! You're on fire, you have completed the second riddle.")
                                        self.print_slow("      Third riddle:")
                                        self.print_slow("      A outside-world creature based on a D&D character which hunts some of their preys in the middle of the")
                                        self.print_slow("      night, travels between worlds, its mouth opens like a flower, its weakness it’s a person called as a ")
                                        self.print_slow("      number and fire. Type the creature's name: ")
                                        print("")
                                        while True:
                                            option = input("Type your guess: ").lower().strip()
                                            if any(keyword in option for keyword in ['demogorgon']):
                                                self.print_slow("      Congratulations! You have completed all riddles.")
                                                self.visited.append(self.player_position)
                                                self.easter_egg2()
                                                break
                                            else:
                                                print("Not the word we're looking for.\n")
                                        break
                                    else:
                                        print("Not the word we're looking for.\n")
                                break
                            else:
                                print("Not the word we're looking for.\n")

                    if (self.player_position == [9, 8] and [9, 9] in self.visited) or (self.player_position == [1, 9] and [3, 0] in self.visited):
                        file_path = r'everything i wanted.mp3'
                        self.play_music(file_path)

                    # broke down car
                    if self.player_position == [0, 0]:
                        print("""
                                    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                    ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                    ::::::::::::::::::::::::::::::::::::::::==+**###%%%##***++==--::::::::::::::::::::::::::.:
                                    :::::::::::::::::::::::::::::::::::::::+---=+**#%%%%%%%%%%%%%%%#*=-::.:::...:......::...::
                                    :::::::::::::::::::::::::::::::::::::-+.......:-==+**#%%%%%@@%%%%%%+::::.::::.............
                                    ::::::::::::::::::::::::::::::::::::++.......::====++*++*###*#%%%%@@%+==-:::::::..........
                                    ::::::::::::::::::::::::::::::-==+*#*=-------=------+*++=+**+#%%%%@@@@#+++++=-::..........
                                    ::::::::::::::::::--==++**##%%%%%@@@@%*+***++=====++-=+++=+*+#%%%%%@@%#*+++===---::=:.....
                                    ::::::::::::-=+*%%##*#%@@%%%%#####*++====+**###%#****+*---=+=++===**+=*%#*+=--=+*#%#=.::::
                                    ::::::::=*#%@%%###%%%##%%%%%%###****#####%%%%%%%%%%%%####***+++*****#***%%%%%##***+*+:::::
                                    ::::::-:.#%%%@%%%**#%@@%%%##%%%%%%%@@@%%%%%%%%%%###*+****##%%@@@@@@@@%####*++*%@%%%%--::::
                                    ::::::: :#*#%+=+*#%%%%%%%%%@%%%%%%%%%%%%%#####*###%%@@@@@@@@@@@@@@@@@@@@@#++*-#@@#+-::::::
                                    :::::::-*%%%#+*##%%%%%%@@%#%%%@@%%%#****##%%%%%####%@@@@@@@@@@@@@@@@@*%@%*+**====------:::
                                    :::::--#%%#%#+=*#**###**-=%@%%#*++=+**#######%%@@@@@@@@@@@@@@@@@@@@@#+=#*###--*+===----:::
                                    :::::--+==%#**+*##%%%##-..*%%%%%*######%%%@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%=-:-++==---------
                                    ::::::-====+*+*#%@%###*-.:#@@@%@@@@@%*++==*@@@@@@@@@@@@@%%%%%%%%%#########*+=----------::-
                                    :-:::------===++++*#=+#%=#@@@@@@@@@%+*++##:*@@@%%%%%%%##%%##**+++===----------------------
                                    -:--:::---===+++++===+-#+@@@@@#*@@@+#=%*#*-*@@%%%%%###***++++==-----------:-:---------:::-
                                    -:--------====+++***=++---+===+#%%@=@*%#*=-%%%##**+++=======----------:::-------------::::
                                    -:---------===+=++++***######%%%*#@+=*=-:=##**++=+=====--------------:---------------:---:
                                    -::::::-------=======+=+++*****##*#@#*++**++++======-=----------:--::::------------------:
                                    ::::::::::---------=-==-=============================----------:::::::---:---------:------
                                    :::::::::::::::-::-:--------------------===-====-=----------------------:-----------------                    
                        """)

                        if self.car_first_visit:
                            self.print_slow("      Looks like you have found a Mercedes-Benz 190 SL from the 50s in a perfectly awful shape, it can’t even")
                            self.print_slow("      be ridden. ")
                            print("")
                            self.print_slow("      WOW! There’s a pack of cookies inside of the car, you can use them to gain +10 of health ")
                            print("""

                                                                   .::::-=+#%%%%%-                    
                                                                =#%@%%%%#**+===+@@                    
                                                             :*@#+=#####======*@+.                    
                                                           =%%*+====***+======+%@+                    
                                                         .*@*==================%@:                    
                                                        =@#+============+**+===*@##:                  
                                                       +@%%#==========+%###%*====#@-.:                
                                                      -@##%#+=========*%#####====+#%%@# -*= -%%+#@%.  
                                                     +@*===============+*##*+========+%%%*%%%*+***@+  
                                                    -@*==========================================+%%  
                                                    *@=====+**+==================+***==========+#%%@= 
                                                    +@====*%####=================###%+=========*%%%@@.
                                                    -@*===*%####==================**+============+*#@=
                                                    .@*====+***+===========++===========+*+======+*#@-
                                                    -@+==================+%##%========+%####====+**@% 
                                                    .@#==================+%##%+=======+%###%+===**%@: 
                                                     +@%%%+========+**+===+*#*=========+***+===+**@+  
                                                      =%#%*========%##%*=====================+***@%   
                                                       .#@+========+##*+==================+%%%##@+    
                                                         +@*====================+####+====+%%%@%:     
                                                          +@#+++================#####%=+++***@#.      
                                                           -#@%#*+==============+##%#****#%@%=        
                                                              -+%%#***####+++++++++***#%%+:           
                                                                 -*%%@@%%%****##%%%%@%+:              
                                                                      .-=*#%%#+-::::                  

                        """)
                            self.car_first_visit = False
                        else:
                            self.print_slow("Ah, that car again. It seems like it's not the first time you've come across it.")
                            print("")

                        if self.player_position not in self.visited:
                            self.print_slow("Oh, there are the cookies.")
                            self.print_slow("Would you like to try a cookie?")
                            while True:
                                if self.health < 100:
                                    option = input('>').lower().strip()
                                    if option in ['yes', 'eat', 'enjoy', 'no', 'later', 'cookie', 'try']:
                                        if option in ['yes', 'eat', 'enjoy', 'cookie', 'try']:
                                            self.print_slow("Delicious! You ate a cookie, and your health increased by 10 points.")
                                            self.health += 10
                                            self.visited.append(self.player_position)
                                            if self.health > 100:
                                                self.health = 100
                                            break
                                        if option in ['no', 'later']:
                                            self.print_slow("Alright, maybe later.")
                                            break
                                    else:
                                        self.print_slow("You cant do that right now.")
                                else:
                                    self.print_slow("Seems like you don't need to restore health right now. You're all good! Feel free to come back later if needed.")
                                    break

                    # Radio
                    if self.player_position == [2, 4] and self.player_position not in self.visited:
                        print("""
                                                  .:.                                               
                                               .:---  .::.....                                      
                                               :----  .::------::::::.....                          
                                               :---:         ....::::----:---::::.....              
                                               :----                     ....:::---------:.         
                                               :----:-=+++===--:::...               ..----.         
                                               -+**#####*##############***++==--:::...----.         
                                           :+###########*##****************#############***+++=-    
                                           *############*##*#+****########*#******************##-   
                                           *############*##*#....:::=%*==##*****####%%###******#-   
                                           *############*##**......:=%*::*#****#%%####%%%%###**#-   
                                           *############*##**+++++==+*+==*#***###******##%%#***#-   
                                           *############*##*####***********#*%#**********#%%#**#=   
                                           *############*##*###############*#+*********+++*%%#*#=   
                                           *############*##*##########******#=+*#@@@%#+++++#%#*#=   
                                           *############*##**##**************==#@%%##%%++++*%%*#=   
                                           *############*##*##############*#*--%@@%***%*====%%##=   
                                           *############*##*##########******#--*@@@@@@@*====%%##+   
                                           *############*##*#######*********#=--#@@@@@#==--*%#*#+   
                                           *############*##**#############**##----++=-::::-%##*#+   
                                           *############*###*+=++*#***==++***##-::::.....-%%#**#*   
                                           *################--::..+**--:..:***##+-::....+%##*#*#*   
                                           *################+=-:.:+*#==-:.:****##%#***#%%##****#*   
                                           *#################*******##**********#########*****##*   
                                           *#%%%%%%%%######*####****#####**********************#*   
                                           :#%%%%%%%%%%%%*#####################################*-   
                                                            
                        """)
                        self.print_slow("      You've found a radio. 'What’s up, Jimmy? Looks like a wonderful day, ain’t it?' – 'Oh! You bet, Mike.")
                        self.print_slow("      Wait!... the criminalistics department has brand new information. A 17-year-old teen has been missing for")
                        self.print_slow("      over 2 days; he responds to the name of Tony Byers…' – “. ")
                        self.print_slow("      Oh no! The radio has run out of battery.")
                        print("")
                        self.visited.append(self.player_position)

                    # Jacket
                    if self.player_position == [5, 2] and self.player_position not in self.visited:
                        print("""                                                              
                                                                                                                                            
                                                        -+********=.                                   
                                                      =*=+--=====*+#*:                                 
                                                     **-=*=======*=++%-                                
                                                    *+-==*=======*==++%=.                              
                                                   #+-===*=======*===++@=                              
                                                 .#=-====*=======*====++%-                             
                                                 %+=+++++#+++++++*++++***%:                            
                                                #+-=++***#+++++++#***++++*#:                           
                                              .%%%%%%@%%%%%%%%%%%%%%%@%%%%@#:                          
                                              .@%%%%%%@@%%%%%%%%%%%@%%%%%%@%:.                         
                                               .=@%%%%%%%@%%%%%%%%@%%%%%@%+::.                         
                                               =#++*#%@%%%@+++++%%%%@%#*+*#*.                          
                                             :#=-=====+*#%%@===%@%#*++=====*#-                         
                                            +#--=========+#@*:=@#++=========+##.                       
                                           **--============*%+%**============+##.                      
                                          ++--=============*+@*+*=============+#*.                     
                                         :#--===++=========*#*++*======++=====++#+.                    
                                        .%--===++#=========*%==+*=======+#=====++%-.                   
                                        %+--===++%=========*#==+*=======+%+=====+*@:                   
                                       =%--===++#*==##*====*#*++*===*#%=+*#=====++%+.                  
                                       %---===++@==*@%+====*#+++*===+%@#=+%======++%:                  
                                      -*--===++##=*@%#=====*#==+*====#%@*+##=====++#+:                 
                                      *=--===++@%%%#*======*#==+*=====*#%%%@+====+++#:.                
                                      %%##*+++#%*+=========*##*+*========+*##=++*#%%@:.                
                                      @%%%%%%%@============*#+++*=========++%%%%%%%%@-:                
                                      -*#%@%%%#============*#==+*=========++*@%%@%##+::                
                                        .::-=%+============*#==+*==========++@=-:::::..                
                                            :%+++++++++++++*#*++*++++++++++**%+:.                      
                                            -%+++++++++++++##****++++++++++++##:                       
                                            :================================::.                      
                                                                                   
                        """)
                        self.print_slow("      You have found Tony’s jacket, a note is inside of a pocket, he opens it and something is written on it “western")
                        self.print_slow("      avenue” and a phone number the last digit is unreadable, the number is “628 826 129*.")

                        self.print_slow("Would you like to take the Jacket with you?: ")
                        while True:
                            option = input('>').lower().strip()

                            if option in ['yes', 'no', 'take', 'leave']:
                                if option in ['yes', 'take']:
                                    if self.max_cap == self.current_space:
                                        self.print_slow("Sorry, you're already carrying too many things. You can't carry more items.")
                                        if self.max_cap == 1:
                                            self.print_slow("There must be a way to store more items.")
                                        break
                                    else:
                                        self.print_slow("You picked up the Jacket. Maybe it will come in handy...")
                                        self.inventory.append('jacket')
                                        self.visited.append(self.player_position)
                                        self.current_space += 1
                                        break

                                if option in ['no', 'leave']:
                                    self.print_slow("Alright, maybe later.")
                                    break
                            else:
                                self.print_slow("You cant do that right now.")
                        print("")

                    # street signals
                    if self.player_position == [5, 5]:
                        print("""
                                    =============----==========-===-------==========-----============
                                    ---=**##+======-====----=================----====-========--==---
                                    ----##+*#%%*+=-------==------==-=====-----==-----------------=---
                                    ====%#+++++*#%#*=----------=++------------------------------=====
                                    ====%#+++++++++#%%#+=------#%#+=------------::--------------=====
                                    ====%#+++++++++++++*##*+==%%%%#+-------------------------:--=====
                                    =--=%#+++++==========++*###*###%*:-------------------------------
                                    --::*%#*+++++=+==========++*#%##-::-------------------------::::-
                                    :::::=+*%%#*++++++===========++*##+=:::::-------------------:::::
                                    ::::------=*#%%#*+===============+*##*+-:-----------=+*##=---::::
                                    :::::::-------=+*#%#*++==============++###+=--=+*#%%@%%%%#=::::::
                                    :::::::-------::::-=+*#%#*+============++*#%%%@@%%%%%%%%%#+::::::
                                    ::-:::::----::::...::::-=*#%#*+====++*#%@@@@%%%%%%%%%%%%%#+-::-::
                                    :::::::::::::::..:::::::--:.=%*###%@@@@@%%%%%%%%%%%%%%%%%%*-:::::
                                    ::::::.:::::::....::::::-=+*%%@@%%%%%%%%%%%%%%%%%%%%%%%%%%*=:::::
                                    .:......:::::::::::=+*#%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=.....
                                    .............:-+*#%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*+-......
                                    ::......:-+*%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+=-:.........::
                                    ::::::.*@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*+=-:::.........::::::
                                    ::::::.#@%%%%%%%%%%%%%%%%%%%%%%%%%%#*+=-::.......::::::::::::::::
                                    :--::::%%%%%%%%%%%%%%%%%%%%#%###%#:::::::::::::::-:::::::::::----
                                    ------:%%%%%%%%%%%%%%%#**+=**#*+=---::---::-:::--:::-:::::-------
                                    :----::%%%%%%%%%#*+=-::::--#%%#*++::-----::::::--:::----:::------
                                    ------:*##*+==--:-::::::---*%##*==:------::::::-------::::-------
                                    -------::::----------------=%##+-----------------------:::-------
                                    ---::----------------------=%##+-=---------------------------:---
                                    -::::---------------------:=%##+--::-::---------------------::::-
                                    ::::--------------------:::-%##+-=:::::::--------------------::::
                                    ::::--:-----------------:::=%%#+-=:::::::-----------------:--::::
                                    :::::::--------------------=%%#+-=:::---------------------:::::::
                                    :::::::-----::::..::::-----=%%#+-=:-:------::::..::::-----:::::::
                                    ::--:::::---::::::.::::---:-%%#+==::..:---::::.::::::---::::::-::
                                    ::::::::::::::....:::::::::-%%%*=-....:::::::::....::::::::::::::
                                    :::::...::::::...::::::::::-%%%*==..::::::::::::...::::::...:::::
                                    ........::::.:::::::----:::=%%%*==:::::::----:::::::..:::........
                                    ...................:-------=%%%*+=-----------:...................
                                    :::::..........:::..:::::::=%%%*++:::::::::::..:::..........:::::
                                    :::::...........:...:......=%%%*+=...::.....:...............:::::
                                    :::::....:::::::...........=@%%*+=...............:::::::....:::::
                                    :--::::::::::::::::::::::::=@@%*++....::::::::::::::::::::::::--:
                                    ::-:::::::::::::::::.::::::+@@%#*+:::::::::::::::::::::::::::::::
                                    ::::.....::::::::::....::::+@@%#*+..::::::.....:::::::::.....::::
                        """)
                        if self.player_position not in self.visited:
                            self.print_slow("      Two paths lie before you. To the left, the 'Soulless Forest' hides secrets within its eerie ")
                            self.print_slow("      embrace. To the right, 'No Way Out' challenges your resolve. Choose your destiny wisely”")
                            self.visited.append(self.player_position)
                        print("")

                    # Mushroom
                    if self.player_position == [7, 7] and self.player_position not in self.visited:
                        print("""

                                                      :=+******#*+=:                  
                                                  .=*%%%#*-.     -#%%*-               
                                                -#%%##########*#######%%*:            
                                              =#=:-=+##############***##%%*-          
                                            =#=.      *#########-.      =##%#-        
                                          :#%#.       =########:         ###%%*.      
                                         +%%%%#+-:::-+#########*:     .-*#####%%-     
                                       .##%%%%##################################%*    
                                      :%=:#%%%#####**###################*=---=*##%#.  
                                     :%-.-#%%%%*:     .-*#############-        =##%#. 
                                    .%*+*%%%%%%.         *###########+         -###%# 
                                    *%%%%%%%%%%+:        *############-      :+#####%=
                                    %%%%%%%%%%%%#+=-::-+#################**#########%*
                                    *%+=---=+#%%%%%%%%#####*-.  .:-##############%%%%=
                                     **:......-*%%%%%%%%%%*.       .########%*=-::=%* 
                                      -**=:.....#%%%%%%%%%*:.......-%%%%%%%#-..:=#*-  
                                        .-*#*=--#%%%%%%%%%%#*====+*%%%%%%%%#+*#*-.    
                                            .:=+*#%%%%%%%%%%%%%%%%%%%%%%#*+=:.        
                                                .#+--==-------------:::+*             
                                                =*-----:::::::::::::::::*=            
                                               .#=-----:::::::::::::::::-#.           
                                               +*------::::::::::::::::::*+           
                                               #+-------:::::::::::::::::=#           
                                               #+--------::::::::::::::::=#           
                                               +*---------:::::::::::::::*+           
                                                *+------------:::::::---+*            
                                                .**=------------------=**.            
                                                  -**+=------------=+**-              
                                                    .-=++**++++**++=-.   
                        """)
                        self.print_slow("      Embark on a mind-blowing journey with the psychedelic mushroom that awaits your bravery, adventurer.  ")
                        self.print_slow("      This mushroom, a treasure of the unknown, immerses you in a world of pleasures, colors and surreal shapes.")
                        self.print_slow("      Its effects will transport you to impossible landscapes and immerse you in unparalleled visual ecstasy.")
                        self.print_slow("      But beware, intrepid seeker, for the line between reality and illusion fades.")
                        print("")

                        self.print_slow("Would you like to try the mushroom?")
                        while True:
                            option = input('>').lower().strip()
                            if option in ['yes', 'eat', 'enjoy', 'no', 'later', 'mushroom', 'try']:
                                if option in ['yes', 'eat', 'enjoy', 'mushroom', 'try']:
                                    self.print_slow("That")
                                    time.sleep(0.7)
                                    self.print_slow("Wasnt")
                                    time.sleep(0.7)
                                    self.print_slow("A good idea")
                                    time.sleep(0.7)
                                    self.print_slow("Your health has decreased by 10 points. Maybe you shouldn't eat strange things from the forest...")
                                    self.health -= 10
                                    self.visited.append(self.player_position)
                                    break
                                if option in ['no', 'later']:
                                    self.print_slow("Alright, maybe later.")
                                    break
                            else:
                                self.print_slow("You cant do that right now.")

                    # coins
                    if self.player_position == [5, 9] and self.player_position not in self.visited:
                        print("""
                                                       :*#%%%%%@@@@@@@%+                   
                                                  *#%%%#++===========++#%%%@@-             
                                             .**%%+=.........:=============++#%@@=         
                                           :**++::.......:=====================+*%@+.      
                                          **++.......:==**+++++++++++**+=========++%@=.    
                                        **++......==**++=-...:==========+**+=======++@@:   
                                        %%:.....==++=-.........:============+========#%:   
                                      ##++:...==**--......::::::=============+*+=====++@@: 
                                      %%:....:**++.......-*********#%#++=====++**======%%: 
                                      %%:...==**--.......-*+.....-=*%#++=======**======#%-.
                                    ##++...:**++.........-*+.:====+#%#++=======++**+===++%@
                                    %%==..==**==.........-*+.:====+#%#++=========+*+=====%@
                                    %%==..==**====.....:=+*+.:====+#%#++=========+*+=====%@
                                    @@======**===========+*+.:====+#%#++=========+*+=====%@
                                    @@======**===========+*+.:====+#%#++=========+*+=====%@
                                    @@======##===========+*+.:====+#%#++=========*#+=====%@
                                    @@======%%===========+*+.:====+#%#++=========#%+=====%@
                                    ##**====##++=========+*+.:===++#%#++++=====++##+===+*##
                                      %%====++##++=======+#*++****##%#+++++++++*#*+==++%%: 
                                      @@**====##**++=====+###########*+++++++**##*+++**%@: 
                                      ####++==++##**++++==+*********+++++++**##*+++++####. 
                                        @@**++++++##****++++++++++++++++***##*+++++**%@:   
                                        *#%#**+++++*##********************#*+++++**#%##.   
                                          *#%#**+++++++***###########***+++++++**#%##.     
                                           .##%%****++++++++++++++++++++++++***#%##-       
                                             .**++%%##****+++++++++++****###%*+**:         
                                                  ++++=+###############*==+++.                      
                                                     +++##############*==+           
                                                     
                        """)

                        self.print_slow("      Coins, the glittering treasures strewn across these lands. These shimmering tokens of wealth and fortune")
                        self.print_slow("      are scattered far and wide, waiting to be claimed by the intrepid souls who dare to explore every nook and")
                        self.print_slow("      cranny of this vast forest.")
                        print("")

                        self.print_slow("Would you like to take the coins with you?: ")
                        while True:
                            option = input('>').lower().strip()

                            if option in ['yes', 'no', 'take', 'leave']:
                                if option in ['yes', 'take']:
                                    if self.max_cap == self.current_space:
                                        self.print_slow("Sorry, you're already carrying too many things. You can't carry more items.")
                                        if self.max_cap == 1:
                                            self.print_slow("There must be a way to store more items.")
                                        break
                                    else:
                                        self.print_slow("You picked up the coins. They might come in handy later.")
                                        self.inventory.append('coins')
                                        self.current_space += 1
                                        self.visited.append(self.player_position)
                                        break

                                if option in ['no', 'leave']:
                                    self.print_slow("Alright, maybe later.")
                                    break
                            else:
                                self.print_slow("You cant do that right now.")
                        print("")

                    # Minigame
                    if self.player_position == [8, 5] and self.player_position not in self.visited:
                        file_path = r'C:\Users\lloyd\Downloads\Y2meta.app - Lobo aullando-efecto de sonido (128 kbps).mp3'
                        self.play_music(file_path)
                        print("""                                                                    
                                                                              ..                
                                                                           .=#%%#=              
                                                                        :=*#*#%%%%#.            
                                                                    .-+#%+.    :--+=            
                                                             .:-=*#%*--%+      .= .+            
                                                       :=+*#*+=-=%=.   #    .=*%%::=            
                                                    :*%#+---:-+=:.         =%%%%% +:            
                                                  -#%=..=#*=-+=           .%%=*%*:%=            
                                                .*%*  :=:                 -%+ :-=*%=            
                                           .-=*#%%-                       ..      :%:           
                                        .=#%#+: =:                             .-*#%:           
                                    .-+#%#+: :=*:                           .+#%%%#-            
                                   +%%#=:  :-+#-   .                      :*%%%%*:              
                                    :+#%%%%%%%* -**:                    .*%%%%*.                
                                       .:-%%%%#%%+                     :%%%%%=                  
                                         -%%%%%%%.:=**-               .:*%%%+                   
                                        -%%%%%%%%#%%#-+##=:- .         -%%%%.                   
                                      :*%%%#=#%%%%%%%%%%#%%%*=%=.      *%%%%.                   
                                   .-#%%*=: =%%+:%%%%%%%%%%%%%%%%+:    %%%%%=                   
                                  :=-:.   .+#=.  -%#=#%%%#%%%%+#%%%#=: %%%%%%:                  
                                         :=:      :#= =#%%+=+##-.-+*%%#%%%%+*%=.                
                                                   .*-  :=#%+.:=+-. .-*%%%%%+.:=.               
                                                     -:     ::.         -*%%%%+:                
                                                                :.        .-*%%%#=.             
                                                                 .=+=:.      :*%%%%+.           
                                                                    .=**=:     :*%%%%+.         
                                                                        -*%*=:   =%%%%%-        
                                                                           -*%#+- =%#:=#=       
                                                                             .=#%%*%%-  =:      
                                                                                .+%%%=          
                                                                                  .*%.          
                                                                                    .           
                                                                    
                        """)
                        time.sleep(5)
                        file_path = r'C:\Users\lloyd\Downloads\Y2meta.app - Star Wars - Battle of the Heroes Suite (128 kbps).mp3'
                        self.play_music(file_path)
                        self.visited.append(self.player_position) # Maybe aqui un ascii del lobo
                        self.print_slow("      Navigating through the forest, the tranquility shatters as a distant growl reveals a lurking wolf.")
                        self.print_slow("      Adrenaline surges, and you sprint through the trees. Amidst the chaos, you stumble upon a suitcase.")
                        self.print_slow("      Flipping it open, relief washes over as you spot a firearm. However, it's locked with a combination.")
                        self.print_slow("      With the wolf's howls closing in, your focus intensifies on deciphering the code—a crucial barrier between you and survival.")
                        print("")

                        self.print_slow("Swiftly now, decipher the 4-digit code—the wolf draws near. Your survival depends on a quick mind and a steady hand.\n")

                        secret_code = str(random.randint(1000, 9999))  # Genera un número aleatorio de 4 dígitos
                        attempts = 0
                        index = 0

                        while attempts < 10:
                            digit_guess = input(f"Guess the {index + 1}º digit of the secret code: ")
                            if len(digit_guess) != 1 or not digit_guess.isdigit():
                                print("No time to waste! Enter a valid 5-digit number quickly.")
                                continue
                            if digit_guess == secret_code[index]:
                                print("Correct!\n")
                                index += 1
                                if index == 4:
                                    print(f"Congratulations! You unlocked the suitcase in {attempts} attempts")
                                    break
                            else:
                                if digit_guess < secret_code[index]:
                                    print("The digit is greater. Keep going!")
                                else:
                                    print("The digit is smaller. Keep trying!")
                                attempts += 1

                                if attempts == 3:
                                    print("\nOh no! The wolf is getting closer.")
                                elif attempts == 5:
                                    print("\nThe wolf is almost upon you. Quick, decipher the code!")
                                elif attempts == 7:
                                    print("\nThe wolf is closing in. Hurry, decipher the code!")
                                elif attempts == 10:
                                    print("\nThe wolf attacks! You were too slow.")

                                print(f"You have {10 - attempts} attempts left.\n")

                        if attempts == 10:
                            self.print_slow("      Despite your efforts, the wolf catches up.")
                            self.print_slow("      You manage to escape, but the wolf leaves you severely injured.")
                            self.print_slow("      Unfortunately, you've lost 50 health points in the encounter.")
                            self.health -= 10
                        else:
                            self.print_slow("      You quickly grab the weapon, fend off the wolf, and escape unscathed. Well done!")

                    # phone booth
                    if self.player_position == [8, 0]:
                        print("""
                                     .::::::::::::::::::::::::::::::::::::::::::::::::::::::::. 
                                    .=:======================================================:-:
                                    .--+++++++++++++++++++++++++++++++++++++++++++++++++++++++.-
                                    .--++++++++++++++++++++++=:    :-  .++++++++++++++++++++++.-
                                    .--+++++++++++++++++++++:      .-   ++++++++++++++++++++++.-
                                    .--++++++++++++++++++++        .-   ++++++++++++++++++++++.-
                                    .--+++++++++++++++++++         .-   ++++++++++++++++++++++.-
                                    .--++++++++++++++++++          .-   ++++++++++++++++++++++.-
                                    .--+++++++++++++++++.       ...-=--=++++++++++++++++++++++.-
                                    .--++++++++++++++++-    .=++++++++++++++++++++++++++++++++.-
                                    .--++++++++++++++++.    :+++++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++=     :+++++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++:     :+++++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++.     :+++++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++.     :+++++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++.     :+++++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++.     :+++++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++-     :+++++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++=     :+++++++++++++++++++++++++++++++++.-
                                    .--++++++++++++++++     :+++++++++++++++++++++++++++++++++.-
                                    .--++++++++++++++++:    :+++++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++++     -=+++++++++++++++++++++++++++++++.-
                                    .--+++++++++++++++++-          .=::-++++++++++++++++++++++.-
                                    .--++++++++++++++++++:          =   ++++++++++++++++++++++.-
                                    .--+++++++++++++++++++.         =   ++++++++++++++++++++++.-
                                    .--++++++++++++++++++++.        =   ++++++++++++++++++++++.-
                                    .--+++++++++++++++++++++-       =   ++++++++++++++++++++++.-
                                    .--+++++++++++++++++++++++-....:=..:++++++++++++++++++++++.-
                                    .--++++++++++++++++++++++++++++++++++++++++++++++++++++++=.-
                                     --:::::::::::::::::::::::::::::::::::::::::::::::::::::::- 
                        """)

                        if all(item in self.inventory for item in ['screwdriver', 'jacket', 'coins']):
                            self.print_slow("oh me falta un numero")

                            secret_number = 8
                            attempts = 0

                            while True:
                                user_guess = input("Enter your guess: ")

                                attempts += 1

                                if int(user_guess) == secret_number:
                                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                                    break
                                else:
                                    print("Incorrect. Try again.")


                        # implemntar adivianr el ultimo numero (8 va a ser el numero)
                        # una vez compltadas esas acciones agregar una parte de historia en texto
                        # cuando se acabe de mostrar el texto te llevara a la batalla final en [9,4]



                    # backpack
                    if self.player_position == [5, 9] and self.player_position not in self.visited:
                        print("""
 
                                                     .=++++++++++-             
                                                  ..**-:-======:.-*-                    
                                             :=+++----===================+*=            
                                           -#*-.                        :*==*           
                                          -#.                          =#.  ==          
                                          #:                          -%%#: .#          
                                         .%                           *=###  *:         
                                         .#                           #--%%= =+         
                                         :#                           #-.%%+ .#         
                                         :*                           #- %%*  %         
                                         :#   :=+=:           =+=+.   *- %%%  %         
                                         .%:  *- -*          :#  +=   *- %%%. %         
                                         .#=++#: -#+++==++===*#  +*+++%. %%%. %.        
                                         :#  .#: -*          -#  +=  .%  %%%: %.        
                                         :*  -%: -#+===++++++*#  +%. .%  #%%==%         
                                         :*  -%:.=+          :#..*%  .%--##+-.%:        
                                         =*  -#=+=.           :==-%.  %-.     %@=       
                                         #*  -# .               : #.  %.     :*+@#-     
                                       =%%*  :#:::.... . . . . .: %.  #:     *%%@@@%*+= 
                                   :+#%@@@*   .--======+++++++++++-   *-    =*****+*%%- 
                                   +%*=-. #.                          *- .-=:           
                                           --=--------::::.........::-#+=-.             

                        """)
                        self.print_slow("      Ah, the humble yet invaluable backpack, a traveler's trusted companion in this grand odyssey. Crafted with")
                        self.print_slow("      durable materials and enchanted with the magic of storage, it is more than mere fabric and straps, use it ")
                        self.print_slow("      with wisdom, not everything can be stored inside of it. Your inventory has increased to 3 slots")
                        print("")
                        self.visited.append(self.player_position)
                        self.max_cap = 3

                    print("Actual position:", self.player_position)
                    print("")
                else:
                    print("Invalid input. Please try again.")
            else:
                self.Game_Over()
                exit(0)


vg = Videogame()
vg.Title()
