print("sales report")

print()

year = int(input(f"The year the sales are for "))

#creates space
print()

#loop function

    # display question an allow user to enter info
jan = int(input(f"please enter the sales for January £"))
feb = int(input(f"please enter the sales for Febuary £"))
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

#minimum sales for the year
minimum = float(min(jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec))
print(f"minimum sales for {year} £ {minimum}")

#maximum sales for the year
maximum = float(max(jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec))
print(f"maximum sales for {year} £ {maximum}")


f = open("sales.txt", "wt")
f.write("\n")
f.write("sales report")
f.write("\n")
f.write("--------------")
f.write("\n")
f.write("\n")
f.write(f"sales report is for the year {year}")
f.write("\n")
f.write("\n")
f.write(f"sales for january was £{jan}")
f.write("\n")
f.write(f"sales for february was £{feb}")
f.write("\n")
f.write(f"sales for march was £{mar}")
f.write("\n")
f.write(f"sales for april was £{apr}")
f.write("\n")
f.write(f"sales for may was £{may}")
f.write("\n")
f.write(f"sales for june was £{jun}")
f.write("\n")
f.write(f"sales for july was £{jul}")
f.write("\n")
f.write(f"sales for august was £{aug}")
f.write("\n")
f.write(f"sales for september was £{sep}")
f.write("\n")
f.write(f"sales for october was £{octo}")
f.write("\n")
f.write(f"sales for november was £{nov}")
f.write("\n")
f.write(f"sales for december was £{dec}")
f.write("\n")
f.write("\n")
f.write("summary")
f.write("\n")
f.write("---------")
f.write("\n")
f.write("\n")
f.write(f"The total sales for {year} are £{yearly_total}")
f.write("\n")
f.write(f"The average monthly sales for {year} are £{year_average}")
f.write("\n")
f.write(f"The month number with the maximum sales was £{maximum}")
f.write("\n")
f.write(f"The month number with the minimum sales was £{minimum}")

f.close()
    
