import random
rock = "🗿"
paper = "📃"
scisors = "✂️"


print("""
         If you want to exit type off!
         If you want to exit type 0ff!
         If you want to exit type off!
         If you want to exit type off!""")
         
print("Welcome")
while True:
    user = input("Enter your choice rock(r), paper(p), or scisors(s) ").lower()
    if user == "off":
        exit()
    computer_choice = random.choice(['r', 'p', 's'])
    
    if user == 'r':
        print(rock)
    elif user == 'p':
        print(paper)
    elif user == 's':
        print(scisors)
    elif user != 'r' or 's' or 'p':
        print("try again")
        continue
    print()
    print("↑ Your choice ↑")
    print("--------------------")
    print("↓ Computer chooses ↓")
    print("")
    if computer_choice == 'r':
        print(rock)
    elif computer_choice == 'p':
        print(paper)
    elif computer_choice == 's':
        print(scisors)
    
    if user == computer_choice:
        print("")
        print("It's a tie!")
        print("")
    elif (user == 'r' and computer_choice == 's') or\
         (user == 's' and computer_choice == 'p') or\
         (user == 'p' and computer_choice == 'r'):
         print("")
         print("You win!")
         print("")
    else:
        print("")
        print("Computer wins hhihiih = 110101010101010💻💻 !")
        print("")
    if user == "off":
        break


    

 
