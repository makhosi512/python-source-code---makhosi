# display progam title
print("sale report")

print()

year = int(input(f"The year the sales are for "))

#creates space
print()


yearly_total = 0
#list store for sales
sales_list = []
# loop function
for months in range(1,13):
    # display question an allow user to enter info
    sales = int(input(f"please enter the sales for month {months}> £"))
    
    #storing figures in list
    sales_list.append(sales)
    
    #calculation for total sales
    yearly_total = float(yearly_total + sales)
    
    #calculation for average sales
    average_monthly = float(yearly_total / months)

    
print()
#diplays message contain 'year' and 'total'
print(f"total sales for {year} are £{yearly_total} ")

#displays message containing 'year' and 'monthy average'
print(f"the average monthly sales for {year} are £{average_monthly} ")

#creates space
print()
#minimum sales for the year
print(f"minimum sales for {year} £" ,min(sales_list))
#maximum sales for the year
print(f"maximum sales for {year} £" ,max(sales_list))

print()

#message detailing list of sales for the year
print(f"list of sales for {year} ")

#displays stored sales
for sales in sales_list:
    print(f"{sales}")
    



    
    

    
    
    
    