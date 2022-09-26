print("Welcome to my computer Quiz")
playing =input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
else:
    print("Okay ! Lets play :) ")

ans_correct=0
ans_incorrect=0

answer=input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct !")
    ans_correct+=1
else:
    print('Incorrect !')

answer=input("What is the full form of WAN? ")
if answer.lower() == "wide area network":
    print("Correct !")
    ans_correct+=1
else:
    print('Incorrect !')

answer=input('What is the full form of "MAN"?')
if answer.lower() == "metropolitan area network":
    print("Correct !")
    ans_correct+=1
else:
    print('Incorrect !')

answer=input('What is the full form of "ODBC"?')
if answer.lower() == "open data base connectivity":
    print("Correct !")
    ans_correct+=1
else:
    print('Incorrect !')

answer=input('What is the full form of "OOP"?')
if answer.lower() == "object oriented programming":
    print("Correct !")
    ans_correct+=1
else:
    print('Incorrect !')

answer=input('What is the full form of "PDF"?')
if answer.lower() == "portable document format":
    print("Correct !")
    ans_correct+=1
else:
    print('Incorrect !')

answer=input('What is the full form of "RTF"?')
if answer.lower() == "rich text format":
    print("Correct !")
    ans_correct+=1
else:
    print('Incorrect !')

answer=input('What is the full form of "SMS"?')
if answer.lower() == "short message service":
    print("Correct !")
    ans_correct+=1
else:
    print('Incorrect !')

print("Your Score is " + str(ans_correct))

