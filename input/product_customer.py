p_name = input("Enter product name:")
p_price = int(input("Product price (ayo waraguye product):"))

c_need = int(input("Product customer need:"))

seeling_price = int(input("Product seeling price ( ayo ugurijije product ):"))

payed_amount = c_need * seeling_price
print("Customer paid amount: ", payed_amount)

profit_amount = p_price * c_need


profit_before = payed_amount - profit_amount

print("profit: ", profit_before)

mom = payed_amount / 2;
mom_pay = (mom * 0.5) / 100
print("MOM pay amount profit: ", mom_pay)


tax = ((profit_before  - mom_pay) * 13) / 100
print("Tax amount for profit :" , tax)

p = profit_before - tax

print("Total profit ✅:" , p) 



