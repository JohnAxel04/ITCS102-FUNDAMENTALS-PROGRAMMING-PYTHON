loan = eval(input("Put the amount you will loan: "))
period = eval(input("Put the loan duration: "))

period *= 12
monthly = loan / period
balance = loan
interest = 0

print("Payment Schedule")
print("Month\t|Monthly Payment\t|Interest\t|Principal\t|Remaining Load\t|")

for i in range(1,period + 1,1):
    balance -= monthly
    interest = balance * 0.00256
    month = interest + monthly
    print(f"{i}\t  {month:.2f}\t\t\t  {interest:.2f}\t\t  {monthly:.2f}\t\t  {balance:.2f}",end="")
    print()