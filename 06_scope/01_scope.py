# ============================================================
# 1. GLOBAL SCOPE
# ============================================================

# x is created outside the function,
# so x has GLOBAL scope.
x = 100

def fun(y):
    # We can access the global variable x inside the function.
    # y is a local variable because it belongs to this function.
    z = x + y

    # z is also a local variable.
    return z

print(fun(5))   # 100 + 5 = 105


# ============================================================
# 2. LOCAL / FUNCTIONAL SCOPE
# ============================================================

# a is a global variable.
a = 90

def f1():
    # This a is a NEW local variable.
    # It exists only inside f1().
    a = 5
    print(a)

f1()            # Output: 5

# The global a is still 90 because the local a
# inside f1() does not change the global a.
print(a)        # Output: 90


# ============================================================
# 3. USING global KEYWORD
# ============================================================

# n1 is a global variable.
n1 = 100

def f2():
    # The global keyword tells Python that we want to use
    # the GLOBAL variable n1, not create a new local variable.
    global n1

    # This changes the global n1 from 100 to 10.
    n1 = 10

    return n1

f2()

# Since f2() changed the global n1,
# its value is now 10.
print(n1)       # Output: 10


# ============================================================
# 4. NESTED FUNCTION / CLOSURE
# ============================================================

# p is a global variable.
p = 90

def fun1():

    # This is a LOCAL variable of fun1().
    # It is different from the global p.
    p = 10

    def fun2():
        # fun2() does not have its own p.
        # So Python looks in the enclosing function fun1()
        # and finds p = 10.
        print(p)

    # Return the function fun2 itself.
    return fun2


# fun1() returns fun2.
# The returned function is stored in result.
result = fun1()

# Calling result() actually calls fun2().
# fun2() remembers the value p = 10 from fun1().
result()        # Output: 10


# ============================================================
# 5. CLOSURE WITH FUNCTION ARGUMENT
# ============================================================

def chaicoder(num):

    # num is a local variable of chaicoder().
    # Its value will be remembered by the inner function.
    
    def actual(x):

        # actual() uses num from the outer function.
        # This is called a CLOSURE.
        return x ** num

    # Return the inner function.
    return actual


# chaicoder(2) creates a function that calculates x².
f = chaicoder(2)

# chaicoder(3) creates a function that calculates x³.
g = chaicoder(3)


# f remembers num = 2
# Therefore, f(2) = 2² = 4
print(f(2))     # Output: 4

# g remembers num = 3
# Therefore, g(3) = 3³ = 27
print(g(3))     # Output: 27