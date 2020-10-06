def f(x):
    return x**5 + 5*x**3 - 9


def df(x):
    return 5*x**4 + 15*x**2


def newtonRaphson(x0, e, N):
    step = 1
    flag = 1
    condition = True
    while condition:
        if df(x0) == 0.0:
            print('Divide by zero error!')
            break
        x1 = x0 - f(x0)/df(x0)
        x0 = x1
        step = step + 1
        if step > N:
            flag = 0
            break
        condition = abs(f(x1)) > e
    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


if __name__ == "__main__":
    x0 = float(input('Initial Guess: '))
    e = float(input('Error: '))
    N = int(input('Maximum Steps: '))
    newtonRaphson(x0, e, N)
