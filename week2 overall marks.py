print ("mark calculator")
print()

first_mark = int(input('Input the first mark-> '))
first_weighting = int(input('Input the weight of the first mark-> '))
print()

second_mark = int(input('Input the second mark-> '))
second_weighting = int(input('Input the weight of the second mark-> '))
print()

third_mark = int(input('Input the third mark-> '))
third_weighting = int(input('Input the weight of the third mark-> '))
print()

print("The overall mark for the marks and weight input is: ")
print()
weighted_mark1 = (first_mark * first_weighting)
weighted_mark2 = (second_mark * second_weighting)
weighted_mark3 = (third_mark * third_weighting)
overall_mark = float(weighted_mark1 + weighted_mark2 + weighted_mark3)
print(f"mark1 = {first_mark}%")
print(f"weight1 = {first_weighting}%")
print(f"weighted mark = {first_mark} x {first_weighting} = {weighted_mark1}%")
print()
print(f"mark1 = {second_mark}%")
print(f"weight2 = {second_weighting}%")
print(f"weighted mark = {second_mark} x {second_weighting} = {weighted_mark2}%")
print()
print(f"mark1 = {third_mark}%")
print(f"weight3 = {third_weighting}%")
print(f"weighted mark = {third_mark} x {third_weighting} = {weighted_mark3}%")
print()
print(f"overall mark = ({weighted_mark1}% + {weighted_mark2}% + {weighted_mark3}%) = {overall_mark}%")