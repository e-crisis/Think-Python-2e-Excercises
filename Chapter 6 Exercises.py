# fibonacci numbers using recursion

def fibonacci_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)


print(fibonacci_rec(4))
print("---------------------------------------------------")

# fibonacci numbers using iteration


def fibonacci_iter(n):
    first = 0
    second = 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(0, n+1):
                if i >= 2:
                    fib = first + second
                    first = second
                    second = fib
        return fib


print(fibonacci_iter(4))
print("---------------------------------------------------")

# Factorial using recursion


def factorial_recur(n):
    if not isinstance(n, int):
        """
        the built-in function isinstance to verify the type of the argument.
        This case handles non integers
        """
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:  # handles negative integers
        print('Factorial is not defined for negative integers.')
        return None
    if n == 0:
        return 1
    else:
        recurse = factorial_recur(n-1)
        result = n * recurse
        return result


print(factorial_recur(5))
print("---------------------------------------------------")

# factorial using iteration


def factorial_iter(n):
    result = n
    for i in range(1, n):
        result = result * (n-i)
    return result


print(factorial_iter(5))
print("---------------------------------------------------")

# Exercise 6.2

def ack(m,n):
    if m == 0:
        return n+1
    if m > 0 and  n == 0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))


print(ack(3,4))
print("---------------------------------------------------")


# Exercise 6.3 --- palindrome using recursion

def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome_rec(word):
    if len(word) <= 1:  # for 0 letter and 1 letter word are always palindrome
        return True
    if first(word) != last(word):
        return False
    return is_palindrome_rec(middle(word))


print(middle('op'))  # when length of word <= 2 then returns nothing
print(middle('o'))
print(middle(""))
print(is_palindrome_rec('allen'))
print(is_palindrome_rec('bob'))
print(is_palindrome_rec('otto'))
print(is_palindrome_rec('redivider'))
print("---------------------------------------------------")

# palindrome using iteration


def is_palindrome_iter(word):
    for i in range(0, int(len(word)/2)):
        if word[i] != word[-i-1]:
            return False
        return True


print(is_palindrome_iter("malayalam"))
print(is_palindrome_iter("noon"))
print(is_palindrome_iter("hello"))
print("---------------------------------------------------")

# Exercise 6.4


def is_power(a, b):
    if a == b:
        return True
    if a % b == 0:
        if is_power(a/b, b):
            return True
    return False


print(is_power(8,2))
print(is_power(7,8))
print(is_power(9,3))
print("---------------------------------------------------")


# Exercise 6.5

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


print(gcd(20,8))
print("---------------------THE END------------------------------")
