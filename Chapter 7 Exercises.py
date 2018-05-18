"""
Exercise 7.1.
Copy the loop from Section 7.5 and encapsulate it in a function called mysqrt
that takes a as a parameter, chooses a reasonable value of x, and returns an
estimate of the square root of a.
To test it, write a function named test_square_root that prints a table like this:
a   mysqrt(a)      math.sqrt(a)   diff
-   ---------      ------------   ----
1.0 1.0            1.0            0.0
2.0 1.41421356237  1.41421356237  2.22044604925e-16
3.0 1.73205080757  1.73205080757  0.0
4.0 2.0            2.0            0.0
5.0 2.2360679775   2.2360679775   0.0
6.0 2.44948974278  2.44948974278  0.0
7.0 2.64575131106  2.64575131106  0.0
8.0 2.82842712475  2.82842712475  4.4408920985e-16
9.0 3.0            3.0            0.0
The first column is a number, a;
the second column is the square root of a computed with mysqrt;
the third column is the square root computed by math.sqrt;
the fourth column is the absolute value of the difference between the two estimates.
"""

import math


def mysqrt(a):
    x = a/2
    epsilon = 0.0000001
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return x
            break
        x = y

def test_square_root():
    print("a    mysqrt(a)              math.sqrt(a)              diff")
    print("-    ---------              ------------              ----")
    for i in range(0, 9):
        for j in range(0, 4):
            if j == 0:
                print(float(i+1), end="")
            elif j == 1:
                print('{0: .18f}'.format(mysqrt(i+1))," ", end="")
            elif j == 2:
                print('{0: .18f}'.format(math.sqrt(i+1)),"      ", end="")
            elif j == 3:
                print(abs(mysqrt(i+1) - math.sqrt(i+1)))
        print("\r")


test_square_root()



"""
Exercise 7.2.
The built-in function eval takes a string and evaluates it using the Python interpreter.
For example:
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<class 'float'>
Write a function called eval_loop that iteratively prompts the user, takes the resulting input and
evaluates it using eval, and prints the result.
It should continue until the user enters 'done', and then return the value of the last expression it
evaluated..
"""

def eval_loop():
    result=0
    while True:
        s = input('>>>')
        print("here",type(s))
        if s == 'done':
            break
        result = eval(s)
        print(result)
    print(result)


eval_loop()


"""
Exercise 7.3.
The mathematician Srinivasa Ramanujan found an infinite series that can be used to
generate a numerical approximation of 1/p: (some expression)
Write a function called estimate_pi that uses this formula to compute and return an estimate of
p. It should use a while loop to compute terms of the summation until the last term is smaller than
1e-15 (which is Python notation for 10􀀀15). You can check the result by comparing it to math.pi.
"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def estimate_pi():
    k = 0
    sum = 0
    c = 2 * math.sqrt(2)/9801
    while True:
        a = factorial(4*k) * (1103 + 26390 * k)
        b = factorial(k) ** 4 * 396 ** (4*k)
        term = c * a/b
        sum = sum + term
        k = k + 1
        if term < 1e-15:
            break
    return 1/sum


print(estimate_pi())

