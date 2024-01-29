print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! Let's Play :)")
score = 0

answer = input("A person making sure that rules are followed in a chat room or forum has which name? ")
if answer.lower() == 'moderator':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What do the initials “PDF” stand for in the context of document files? ")
if answer.lower() == 'portable document format':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does the acronym “USB” stand for? ")
if answer.lower() == 'universal serial bus':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What programming language is commonly used for building dynamic web pages? ")
if answer.lower() == 'javascript':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("In computing, what does the acronym “ISP” stand for? ")
if answer.lower() == 'internet service provider':
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print('You got ' + str(score) + ' questions correct!')
print('You scored ' + str((score / 5) * 100) + '%')