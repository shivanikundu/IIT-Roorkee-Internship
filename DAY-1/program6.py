#Simple interest calculator : P , R , T as input
#Input amount,rate and time from user
P = float(input("Enter Principal Amount(P): "))
R = float(input("Enter Rate of Interest(R): "))
T = float(input("Enter Time in Years(T): "))
#Calculate simple interest
SI = (P * R * T) / 100
#Display simple interest
print("Simple Interest is:", SI)