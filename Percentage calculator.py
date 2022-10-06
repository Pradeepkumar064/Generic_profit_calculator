def percentage(interest_rate, principle):
    i = 1
    while i <= 365:
        interest = (interest_rate * principle)/100
        principle = interest + principle
        print(principle)
        i += 1

# Taking input from users for both interest rate and principle
print("Type the expected Interest rate:")
Int_rate = float(input())
print("Enter the principle amount:")
Principle_amount = int(input())
percentage (Int_rate, Principle_amount)

