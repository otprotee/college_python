N = 1
M = 1
Fibonacci = []
ChoiceNum = 0
ChoiceMethod = 1
if int(ChoiceMethod) == 1:
    ChoiceNum = 1000000000
    while len(Fibonacci) != int(ChoiceNum):
        Fibonacci.append(N)
        Fibonacci.append(M)
        N += M
        M += N
    print(Fibonacci)
