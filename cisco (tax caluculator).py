# citizens income tax calculator
income = float(input("Enter the annual income: "))
# income<85528,tax=18% of incm-556thalers
if income < 85528:
    tax = (0.18 * income) - 556
    if tax < 0:
        print("The tax is:", 0, "thalers")
        exit()
    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")

# income>=85528,tax=32% of surplusincm over 85528+14839thalers
else:
    income >= 85528
    tax = (0.32 * (income - 85528)) + 14839
    tax = round(tax, 0)
    print("The tax is:", tax, "thalers")


