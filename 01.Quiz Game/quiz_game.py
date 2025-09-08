print("welcome to my computer quiz!")

playing = input ("Do you want to play ? ")

if playing != "yes":
    quit()

print("Okay! Let's Play:)")
score= 0

answer = input ("What does CPU stand for ? ")

if answer.lower() == "central processing unit":
    print('correct')
    score += 1
else:
    print("Incorrect !")


answer = input ("What does GPU stand for ? ")
if answer == "graphics processing unit":
    print('correct')
else:
    print("Incorrect !")


answer = input ("What does  PSU stands for ? ")
if answer.lower() == "power supply":
    print('correct')
    score += 1
else:
    print("Incorrect !")

answer = input("What does  RAM stands for ? ")
if answer.lower() == "random access memory":
    print('correct')
    score += 1
else:
    print("Incorrect !")


print( "You got" + str (score) + " questions correct!")
print ("You got" + str((score/4)*100)+"%.")