# display progam title
print("sale report")

print()

year = int(input(f"The year the sales are for "))

#creates space
print()

#loop function
largest = 0
smallest = 999
yearly_total = 0
for months in range(1,13):
    # display question an allow user to enter info
    sales = int(input(f"please enter the sales for month {months} "))
    
    yearly_total = float(yearly_total + sales)
    
    average_monthly = float(yearly_total / months)
    

    if (sales > largest):
        largest = sales
        
    if (sales < smallest):
        smallest = sales

    
print()

print(f"total sales for the {year} are {yearly_total} ")
print(f"the average monthly sales for {year} are {average_monthly} ")



print(f"minimum sales for {year} £ " ,float(smallest) )

print(f"maximum sales for {year} £ " ,float(largest) )