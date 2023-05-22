def main():
    menu = make_menu()
    print(menu)
    choice = input("Input: ").upper()
    while choice != "Q":
        if choice == "G":
            get_score = get_valid_score()
        elif choice == "P":
            grade = check_score(get_score)
        elif choice == "S":
            show = show_stars(get_score)
        else:
            print("Invalid Choice")
        print(menu)
        choice = input("Input: ").upper()
    print("Thank you")

def make_menu():
    MENU = """(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""
    return MENU

def get_valid_score():
    score = int(input("Your score is: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Your score is: "))
    print("Your score is valid")
    return score

def check_score(i):
    if i > 90:
        print("Excellent")
    elif i > 50:
        print("Passable")
    else:
        print("Bad")
    return i

def show_stars(number_of_stars):
    for i in range(number_of_stars):
        print("*",end="")
    return i

main()
