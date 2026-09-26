pace=int(input("Enter the pace of the footballer: "))
if(pace==99):
    print("The footballer is goated like messi and ronaldo")
elif(pace>=90):
    print("The footballer is a striker")
elif(pace>=75 and pace<=89):
    print("The footballer is a midfielder")
elif(pace>=60 and pace<=74):
    print("The footballer is a defender") 
else:
    print("The footballer is a goalkeeper")