test_num = 0
while True:
    test_num += 1

    n = input()
    n = int(n)
    if n == 0:
        break

    print("Teste " + str(test_num))

    ingressos_input = input().split()
    for i in range(n):
        j = ingressos_input[i]
        j = int(j)
        if i + 1 == j:
            print(j)

    print("")
