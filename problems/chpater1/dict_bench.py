if __name__=="__main__":
    import random
    import string
    import time

    values = []
    for i in range(10):
        values.append("".join(random.choices(string.ascii_letters + string.digits, k=10)))

    n = 500000
    print(f"Construct {n=} dicts with these random values: {values=}")
    print("---")


    begin_dict = time.time_ns()
    for i in range(n):
        dict(
            a0=values[0],
            a1=values[1],
            a2=values[2],
            a3=values[3],
            a4=values[4],
            a5=values[5],
            a6=values[6],
            a7=values[7],
            a8=values[8],
            a9=values[9],
        )
    constructor_timing = time.time_ns() - begin_dict
    print(f"{'dict constructor:':>20} {constructor_timing / 10 ** 6:.1f}ms")

    begin_dict = time.time_ns()
    for i in range(n):
        {
            "a0": values[0],
            "a1": values[1],
            "a2": values[2],
            "a3": values[3],
            "a4": values[4],
            "a5": values[5],
            "a6": values[6],
            "a7": values[7],
            "a8": values[8],
            "a9": values[9],
        }
    literal_timing = time.time_ns() - begin_dict
    print(f"{'literal dict:':>20} {literal_timing / 10 ** 6:.1f}ms")
    percentage_difference = (constructor_timing - literal_timing) / constructor_timing * 100
    print("---")
    print(f"A literal dict is {percentage_difference:.2f}% faster")