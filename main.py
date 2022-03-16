answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]
#-----------------------------------------------------------------------------------------------------------------------
print("""
Welcome to the game.

You are shoveling snow that is on your driveway when you see a man standing in the middle of the road

Get him off the road. (Yes / No)
""")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\nthe man walks ominously towards you. run inside? (Yes / No)\n")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("\nYou got away from the murderer")

    elif ans2 in answer_no:
        print("\nYou were stabbed 28 times. rip bozo")

    else:
        print("\nPlease input YES/Y/yes/y or NO/N/no/n")

elif ans1 in answer_no:
    print("\nA white truck is speeding towards him. you have mere seconds to push him away. will you push him?\n")

    ans3 = input(">>")

    if ans3 in answer_yes:
        print("\nYou saved the man but died in the process. GAME OVER")

    elif ans3 in answer_no:
        print("\nYou watched as the man was run over. you avoided death at the price of another person's life. I think...idk lol idk how to word things")

    else:
        print("\nPlease input YES/Y/yes/y or NO/N/no/n")

else:
    print("\nPlease input YES/Y/yes/y or NO/N/no/n")