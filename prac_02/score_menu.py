MENU="""(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""
MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0

def main():
    print(MENU)
    choice = ""

    while choice != "Q":
        choice = input("Choose one of the following option ").upper()
        if choice == "G":
            score = get_valid_input("Enter score:", MAXIMUM_SCORE, MINIMUM_SCORE)

        elif choice == "P":
            print(determine_grade(score))

        elif choice == "S":
            print(show_stars(score))

        else:
            print("Invalid choice")
        print(MENU)
    print("Farewell")


def get_valid_input(prompt, high, low):
    "Prompts the user to input a number within a range"
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid score")
        number = int(input(prompt))
    return number


def determine_grade(score):
    """Determine the status based on a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Generates a string of */ asterisk based on the input score"""
    stars="*" * score
    return stars


main()