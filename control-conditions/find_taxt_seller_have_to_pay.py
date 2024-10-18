unitPrice = int(input("Enter unit price:"))
items = int(input("Enter items:"))

if unitPrice < 10000 or items < 10 : 
    print("Invalid unit price must less than 1000 and  items bust be less than 10?😔😒")
else : 
    totalPrice = unitPrice * items
    if totalPrice >= 400000 :
        tax = (totalPrice * 7) / 100
        print("Total price ✅ is: {totalPrice} and tax is: {tax}".format(totalPrice=totalPrice, tax=tax))
    elif totalPrice >= 200000 and totalPrice < 400000 :
        tax = (totalPrice * 9) / 100
        print ("Total price ✅ is: {totalPrice} and tax is: {tax}".format(totalPrice=totalPrice, tax=tax))
    else :
        tax = (totalPrice * 13) / 100
        print("Total price ✅ is: {totalPrice} and tax is: {tax}".format(totalPrice=totalPrice, tax=tax))