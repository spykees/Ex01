secret = "Shark"
guess = ""
limit = 3
guess_count = 0
out_of_guesses = False

while guess != secret and not(out_of_guesses):
    if guess_count < limit:
        guess = input("Enter your world: ")
        guess_count += 1

        if guess_count < limit:
            reminder = limit - guess_count
            print(f"Nope ! You ave {reminder} try!")

    else:
        out_of_guesses = True

if out_of_guesses:
    print("You loose ! ")
else:
    print("You win !")