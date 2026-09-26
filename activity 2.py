
ac=int(input("enter the actual cost of the item: "))
sc=int(input("enter the selling price of the item: "))
profit=sc-ac
loss=ac-sc
if(sc>ac):
    print("The item is sold at a profit,profit amount is",profit)
elif(sc==ac):
    print("The item is sold at no profit no loss")
else:
    print("The item is sold at a loss,loss amount is",loss)
 