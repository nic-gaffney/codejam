from time import sleep

# INTRO
print('Welcome to perspectives. A text based stealth game developed by amay428 and gaffclant.')
sleep(2)
print('You have made it into the soviet factory. Next to you is your partner, Cory. He is from Oaklahoma, and has a deep country accent.')
sleep(2)
print('You are in the entrance room of the factory. There is a hallway leading into the main room of the factory.')
sleep(2)
print('Both of you hold nothing but silenced pistols and combat knifes. And of course, some general tools that ca help on a stealth mission like this.')
sleep(2)
print('You look back down at your dogtag. You read it back to yourself.')
sleep(2)

# CHOOSE YOUR NAME
name = input('What is your name?\nInput: ')
print(f'Cory: {name}! Quit spacing out! We got a mission, and we only have so much time before they find the bodies outside!')
sleep(2)
print(f'{name}: Right... the mission...')
sleep(2)
print(f'Cory: So how are we going to get past the couple of of guards they have in that hallway?')
sleep(2)

# FIRST DECISION
while done = False
    choice1 = input('How are you going to sneak past the guards?\nA: Disquise as the dead guards outside.\nB: Take em out\nC: Toss a coin and lead them away\nD: Try to sneak past normally\nInput: ')

    if choice1.lower() == 'a':
        done = True
        print(f"{name}: We should take those guards outfits. We'll blend right in.")
        sleep(2)
        print("Cory: What if they ask us questions? I don't know any russian!")
        sleep(2)
        print(f"{name}: Damnit! Neither do I. We will just have to hope it all works out.")
        sleep(2)
        print("Cory: Ok...")
        sleep(2)
        print("After you both get dressed, you confidently walk through the hallway. But then the guards stop you")
        sleep(2)
        print('Guard: Почему ты оставил свой пост?')
        sleep(2)
        print('Cory looks at you. You look back. Neither of you know what to do, and if you try to tell Cory what to do, they will hear you speak english and you will surley die.')
        sleep(2)
        # DECISION 2A
    elif choice1.lower() == 'b':
        print(f'{name}: I say we take out those commie bastards! We can each take out one with our gun.')
        sleep(2)
        print('Cory: Great idea! I take the left, you take the right.')
        sleep(2)
        print(f'{name}: 3... 2... 1... NOW!')
        sleep(4)
        print('You both go around the corner shoot your respective guard in the middle of the forehead before they can even blink.')
        sleep(2)
        print('As you drag the bodies away, you get a strange feeling... this mission was going really well so far. TOO well. The entrance you took was way too obvious, and those guards were perfectly lined up for a shot.')
        sleep(3)
        print(f"Then you realise.\nYou jump away from the corpse and scream\n{name}CORY GET AWAY! ITS A TR-")
        sleep(2)
        print('You were too late. The bombs went off and blew you across the room. It was a setup. The intel, the guards, it was all a setup. And now Cory paid the price.')
        sleep(2)
        print("YOU LOST.\nThe mission is a setup. Try to play the least obvious moves.")
    elif choice1.lower() == 'c':
        done = True
        print()
    elif choice1.lower() == 'd':
        done = True
        print()
    else:
        print('Please enter a valid choice')
