import random
import string


def passwored_checker(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append('-your password must be long')

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append('-you need at least one number')

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append('-one character must be lower')

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append('-one character upper must')

    special_character = "!@#$%^&*()-_=+"
    if any(char in special_character for char in password):
        score += 1
    else:
        suggestions.append('-password need one special character')

    # Determine strength
    if score <= 1:
        strength = "Very Weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, suggestions, strength


def generate_password():
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        "!@#$%^&*()-_=+"
    )
    password = ''
    for i in range(12):
        password += random.choice(characters)
    return password


def show_result(score, suggestions, strength):
    print('score is :', score, ' / 5')
    print('strength id : ', strength)

    if suggestions:
        print('suggestions : -')
        for i in suggestions:
            print(i)
    else:
        print('there is no suggestion')


while True:
    print('_____Add your choice___')
    print('1 : check password')
    print('2 : generate password')
    print('3 : exit')

    try:
        choice = int(input('enter your choice number : '))
    except ValueError:
        print('enter valid choice number 1-3')
        continue

    if choice == 1:
        password = input('enter your password: ')
        score, suggestions, strength = passwored_checker(password)
        show_result(score, suggestions, strength)

    elif choice == 2:
        password = generate_password()
        print('generated password is : ', password)
        score, suggestions, strength = passwored_checker(password)
        show_result(score, suggestions, strength)

    elif choice == 3:
        print('program exit')
        break

    else:
        print('invalid choice')