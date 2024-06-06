#Coding practice
print("Welcome to the Game made by Nadid & Tazwar")

playing = input("would you like to play? : ")

if playing.lower() == "no":
    print("OK, Please exit")
    quit()

print("Well to the game, Get Ready for the first question")
score = 0
#
answer = input("Question 1 - What is the full form of CR7? ans: ")
if answer.lower() == "cristiano ronaldo 7":
    print("Correct")
    score +=1
else:
    print("Incorrect")

answer = input("Question 2 - What is the full form of LM10? ans: ")
if answer.lower() == "lionel messi 10":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Question 3 - 22 x 30 = ? ans: ")
if answer.lower() == "660":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Question 4 - Who is Bangladesh cricket's greatest captain? ans: ")
if answer.lower() == "mashrafe mortaza":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Question 5 - What is the greatest coding institution of Bangladesh? ans: ")
if answer.lower() == "bsprc":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("Thank you for playing, you got " + str(score) + " questions right")
print("Thank you for playing, you got " + str(score/4*100) + "% questions right")
