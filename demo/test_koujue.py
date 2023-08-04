def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            out=i*j
            if out%2!=0:
                print(f"{j} * {i} = {i * j}\t", end="")
        print()


if __name__ == "__main__":
    # for i in range(1, 10):
    #     print(i)
    multiplication_table()
