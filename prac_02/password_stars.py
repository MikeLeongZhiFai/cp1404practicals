MIN_LENGTH_OF_PASSWORD = 10

def main():
    password = get_password()
    print_stars(password)

def get_password():
    """This function gets an input from the user, making sure it meets the minimum length requirement"""
    password=input("Enter a password( Please key in at least" + str(MIN_LENGTH_OF_PASSWORD)+ "characters):")
    while len(password) < MIN_LENGTH_OF_PASSWORD:
        print("Password is too short. Try again")
        password = input("Enter a password( Please key in at least" + str(MIN_LENGTH_OF_PASSWORD) + "characters):")
    return password

def print_stars(password):
    """This function prints the number of stars corresponding to the length of password"""
    stars=""
    for i in range(len(password)):
        stars += "*"
    print(stars)

main()