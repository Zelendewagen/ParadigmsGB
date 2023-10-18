def multiply_table(n):
    if n == 0:
        return
    else:
        for i in range(1, 10):
            print(f"{n} * {i} = {n * i}")
        print()
        multiply_table(n - 1)


multiply_table(15)
