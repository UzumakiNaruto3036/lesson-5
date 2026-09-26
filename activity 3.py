grade=int(input("Enter your grade: "))
if(grade==100):
    print("You have an A+ grade and distinction")
elif(grade>=90):
    print("You have an A grade")
elif(grade>=80):
    print("You have a B grade")
elif(grade>=60):
    print("You have a C grade")
elif(grade>=50):
    print("You have a D grade")
else:
    print("You have failed the exam")