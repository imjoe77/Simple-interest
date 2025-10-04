# Simple Interest Program

# Input values
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest (%): "))
time = float(input("Enter the Time (in years): "))

# Formula: SI = (P * R * T) / 100
simple_interest = (principal * rate * time) / 100

#Compound interest
compound_interest = principal * (1 + rate/100) ** time - principal

# Output
print("Simple Interest is:", simple_interest)
