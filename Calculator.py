def addition(p,q):
    return p+q
def substraction(p,q):
    return p-q
def multiply(p,q):
    return p*q
def division(p,q):
    if q==0:
        return "!!..cannot divide by zero."
    else:
        return p/q
print("please select your option: ")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

while True:
    select=int(input("options are (1/2/3/4): "))
    if select not in (1,2,3,4):
        print("please enter a valid input..!!")
    else:
        a=float(input("Enter first value : "))
        b=float(input("Enter second value : "))
        if select==1:
            print(f"Result = {addition(a,b)}")
        elif select==2:
            print(f"Result = {substraction(a,b)}")
        elif select==3:
            print(f"Result = {multiply(a,b)}")
        elif select==4:
            print(f"Result = {division(a,b)}")
    repeat=input("DO you want to repeat (Y/N) : ").upper()
    if repeat=="N":
        print("Thank you..Have a nice day..! ")
        break


        
        