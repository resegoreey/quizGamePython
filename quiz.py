print("Welcome to my quiz game!")

play = input("Are you ready to play?: ")

if play.lower() != "yes":
    quit()

print("Cool! Let's start")

score = 0

answer = input("Who is the first black president of South Africa? ")
if answer.lower() == "nelson mandela":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital city of South Africa? ")
if answer.lower() == "pretoria":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which popular music genre originates in South Africa? ")
if answer.lower() == "amapiano":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which city in South Africa is known as the Diamond city? ")
if answer.lower() == "kimberley":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " answers correct!")
print("You got " + str(score / 4 * 100) + "%")