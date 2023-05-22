def main():
    score = float(input("Enter score: "))
    grade = check_score(score)

def check_score(i):
    if i > 90:
        print("Excellent")
    elif i > 50:
        print("Passable")
    else:
        print("Bad")
    return i

main()