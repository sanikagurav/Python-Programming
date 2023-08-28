#pizz order
size = input("What size pizza you want(S/M/L)")
bill = 0

if size == 's' or size == 'S':
    bill += 100
    print("Small pizza price is 100 Rs.")
elif size == 'm' or size == 'M':
    bill += 200
    print("Mediam pizza price is 200 Rs.")
elif size == 'l' or size == 'L':
    bill += 300
    print("Large pizza price is 300 Rs.")
    
add_pepperoni = input("Do you want to add pepperoni(Y/N)? : ")
if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 's' or size == 'S':
        bill +=30
    else:
        bill +=50
        
extra_cheese = input("Do you want to add extra ccheese(Y/N)? : ")
if extra_cheese == 'y' or extra_cheese == 'Y':
    bill +=20
    
print(f"Your final bill is {bill}")
        
