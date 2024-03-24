"""Task 2: Comprehensions (lists and sets).
The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:
§ Create a normal and comprehensive list that will display the codes.
§ Create a normal and comprehensive list that will add the codes together for auditing purpose.
§ Create a normal and comprehensive list that will display only codes that are tracked by odd
numbers.
§ Create a set to display the list of codes"""

#The libraries is using the codes 14, 15, 16, 17, 18, 19, 20 to all programming related books:

codes = [14, 15, 16, 17, 18, 19, 20]

#Create a normal list that will display the codes.

Ncodes = []

for c in codes:
    Ncodes.append(c)

print("A normal list that display the codes: ", Ncodes)

#comprehensive list that will display the codes.

Ccodes = [c for c in codes]
print("\nA comprehensive list that display the codes: ", Ccodes)

#Create a normal and comprehensive list that will add the codes together for auditing purpose.

addNcodes = []
sumN = 0

for cC in codes:
    sumN = sumN + cC

addNcodes.append(sumN)

print("\nNormal list that add the codes together for auditing purpose: ", addNcodes)

#Create a normal and comprehensive list that will add the codes together for auditing purpose.

sumC = 0

addCcodes = [sumC := sumC + ccComp for ccComp in codes]
print("Comprehensive list that add the codes together for auditing purpose: ",addNcodes)

#Create a normal list that will display only codes that are tracked by odd numbers.

oddCodesC = []

for oC in codes:
    if oC %2 !=0:
        oddCodesC.append(oC)

print("\nA normal list that display only the code that are tracked by odd numbers: ",oddCodesC)

#comprehensive list that will display only codes that are tracked by odd numbers.

oddCodesC = [oC for oC in codes if oC%2 !=0]
print("\nA comprehensive list that display only codes that are tracked by odd numbers: ", oddCodesC)

#Create a set to display the list of codes

setList = set(codes)
print("\nA set to display the list of codes", setList)