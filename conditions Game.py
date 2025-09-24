print("Welcome to the conditions program\nBut converted into Game use conditions😏")  
print("There is a basic rule you have to choose number between 1 to 10")
Your_Name = input("What's your name? ")
print(f"Hello, {Your_Name}\nLet's say you are x for a moment")
Your_Friend = input("What's your friend's name? ")
print(f"Hello, {Your_Friend}\nFor a moment let's say you are y")
"""instead x and y use Your_Name and Your_Friend"""
x = int(input("Pick a number between 1-10: "))
y = int(input("Pick a number between 1-10: "))
if x>10:
    print(f"Hey {Your_Name}, you are trying to cheat you have to choose between 1-10") 
    print(f"{Your_Friend} wins by default")
elif y>10:
    print(f"Hey {Your_Friend}, you are trying to cheat you have to choose between 1-10") 
    print(f"{Your_Name} wins by default")
elif x < y:
    print("x is less than y")
    print(f"{Your_Friend} wins")
elif x > y:
    print("x is greater than y")
    print(f"{Your_Name} wins")       
else:
    print("x is equal to y\nIt's a tie")
