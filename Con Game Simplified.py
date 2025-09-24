print("Welcome to the conditions program")  
print("But converted into Game using conditions😏")

Your_Name = input("What's your name? ")
print(f"Hello, {Your_Name}")
Your_Friend = input("What's your friend's name? ")
print(f"Hello, {Your_Friend}")

x = int(input(f"{Your_Name} Pick a number between 1-10: "))
y = int(input(f"{Your_Friend} Pick a number between 1-10: "))

if x == 69 :
    print(f"{Your_Name} won \nno matter what because {Your_Name} chose the best number in the universe 😏")

elif x<1:
    print(f"Be in your limits, {Your_Name}")
elif y<1:
    print(f"Be in your limits, {Your_Friend}")
elif x>10:
    print(f"Hey {Your_Name}, you are trying to cheat 🤨 you have to choose between 1-10") 
    print(f"{Your_Friend} wins by default")
elif y>10:
    print(f"Hey {Your_Friend}, you are trying to cheat 🤨 you have to choose between 1-10") 
    print(f"{Your_Name} wins by default")
elif x < y:
    print("x is less than y")
    print(f"{Your_Friend} wins")
    print(f"Congratulations {Your_Friend} 🎉\nYou have beaten the creator in his own game !")
elif x > y:
    print(f"{Your_Name} has chosen a greater number than {Your_Friend}")
    print(f"{Your_Name} wins")  
else:
    print("x is equal to y\nIt's a tie")
