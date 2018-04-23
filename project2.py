import math

# @author Jigar D. Prajapati
# @date April 22nd, 2018

#sample equations
def equation1():
    f = lambda x: x**3
    return f

def equation2():
    f = lambda x: (1+(4*x**2))**(0.5)
    return f

def equation3():
    f = lambda x: math.exp(-1*x**2)
    return f

def equation4():
    f = lambda x: (math.sin(x))/x
    return f

#midpoint rule
def midpoint(f, a, b, n): 
    h = float(b-a)/n #finding midpoint
    result = 0
    
    for _ in range(n):
        result += f((a + h/2.0)) #adding all the f(x)
        a += h
    result *= h #multiplying with the midpoint
    return result

#trapezoid rule
def trapezoid(f, a, b, n):
    h = (b-a)/float(n) #finding midpoint
    result = f(a) + f(b) #find the f(a) and f(b) 

    for i in range(1,n,1):
        result = result + (2*(f(a + i*h))) #finding 2*f(x)
    result *= (h/2.0) #multiplying with dx/2.0

    return result

#simpson's rule
def simpson(f, a, b, n):
    h = (b-a)/float(n)
    result = f(a) + f(b)

    for i in range(1,n,1):
        if(i%2 ==0):
            result = result + (2*(f(a + i*h)))
        else:
            result = result + (4*(f(a + i*h)))
    result *= (h/3.0)

    return result


#main input output function. User is asked to select from 4 equation. 
#Planning to ask for an equation from the user in the near future. (Currentl learning how to use sympy and other similar packages with Python)
def main():
    
    try:
        print("\n 1: x^3\n 2: (1+(4x^2))^(1/2)\n 3: e^(-x^2)\n 4: (sin(x))/x\n")
        response = input("Please select a sample equation from the above options\nEnter number or enter 'q' to quit: ")

        while(response != "q"):

            response = int(response)

            a = int(input("\nPlease enter 'a': "))
            b = int(input("\nPlease enter 'b': "))
            n = int(input("\nPlease enter 'n': "))

            if(0<response<5):

                print("\n%-4s %-15s %-15s %-15s\n" % ("n", "Midpoint Rule", "Trapezoid Rule", "Simpson's Rule"))

                for index in range(2,(n+1),2):
                    if(response == 1):
                        ansMid = midpoint(equation1(), a, b, index)
                        ansTrap = trapezoid(equation1(), a, b, index)
                        ansSim = simpson(equation1(),a,b,index)

                    elif(response == 2):
                        ansMid = midpoint(equation2(), a, b, index)
                        ansTrap = trapezoid(equation2(), a, b, index)
                        ansSim = simpson(equation2(),a,b,index)

                    elif(response == 3):
                        ansMid = midpoint(equation3(), a, b, index)
                        ansTrap = trapezoid(equation3(), a, b, index)
                        ansSim = simpson(equation3(),a,b,index)

                    elif(response == 4):
                        ansMid = midpoint(equation4(), a, b, index)
                        ansTrap = trapezoid(equation4(), a, b, index)
                        ansSim = simpson(equation4(),a,b,index)

                    print("%-4i %-15.4f %-15.4f %-15.4f\n" % (index, ansMid, ansTrap, ansSim))

            else:
                print("Wrong input")

            print("\n 1: x^3\n 2: (1+(4x^2))^(1/2)\n 3: e^(-x^2)\n 4: (sin(x))/x\n")
            response = input("Please select a sample equation from the above options\nEnter number or enter 'q' to quit: ")

    except ValueError:
        print("\nError: Invalid Input\n")
    

if __name__ == "__main__":
    main()