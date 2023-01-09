# display progam title
print("sale report")

print()

year = int(input(f"The year the sales are for "))

#creates space
print()

#loop function

    # display question an allow user to enter info
jan = int(input(f"please enter the sales for January £"))
feb = int(input(f"please enter the sales for February £"))
mar = int(input(f"please enter the sales for March £"))
apr = int(input(f"please enter the sales for April £"))
may = int(input(f"please enter the sales for May £"))
jun = int(input(f"please enter the sales for June £"))
jul = int(input(f"please enter the sales for July £"))
aug = int(input(f"please enter the sales for August £"))
sep = int(input(f"please enter the sales for September £"))
octo = int(input(f"please enter the sales for October £"))
nov = int(input(f"please enter the sales for November £"))
dec = int(input(f"please enter the sales for December £"))

print()

yearly_total = float(jan + feb + mar + apr + may + jun + jul + aug + sep + octo + nov + dec)

year_average = float(yearly_total/12)

print(f"total sales for {year} are £{yearly_total} ")
print(f"average sales for {year} are £{year_average} ")