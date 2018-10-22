########## propagate lowest set bit
# e.g. 0b01010000 -> 0b01011111
def propagate_lowest_set_bit(x):
    # x - 1 has all the bits lower than the lowest-set bit set to 1
    # x | (x - 1) sets all bits lower than lowest-set bit in x to 1
    return 0 if x == 0 else x | (x - 1)


def propagate_lowest_set_bit_test():
    # unit test for propagate_lowest_set_bit()
    print("Starting propagate_lowest_set_bit_test()...")
    # test cases
    tests = []
    tests.append({"args": [0b01010000], "expected": 0b01011111})
    tests.append({"args": [0b00000000], "expected": 0b00000000})
    tests.append({"args": [0b10000000], "expected": 0b11111111})
    tests.append({"args": [0b00000001], "expected": 0b00000001})
    tests.append({"args": [0b11111111], "expected": 0b11111111})
    tests.append({"args": [0b00100000], "expected": 0b00111111})
    # execute test cases
    for i, test in enumerate(tests):
        print("Running test %d: " % i, end="")
        args = test["args"]
        expected = test["expected"]
        ret = propagate_lowest_set_bit(*args)
        print(
            "Pass"
            if ret == expected
            else "Fail. Expected %s, got %s"
            % (format(expected, "#010b"), format(ret, "#010b"))
        )
    print()


propagate_lowest_set_bit_test()

########## weight of binary number
# the weight of binary number is defined as the number of 1 bit in the binary representation
# of the number
def weight_binary_number(x):
    if x == 0:
        return 0
    weight = 0
    while x:
        x &= x - 1
        weight += 1
    return weight


def weight_binary_number_test():
    # unit test for weight_binary_number()
    print("Starting weight_binary_number_test()...")
    # test cases
    tests = []
    tests.append({"args": [0b01010000], "expected": 2})
    tests.append({"args": [0b00000000], "expected": 0})
    tests.append({"args": [0b10000000], "expected": 1})
    tests.append({"args": [0b00000001], "expected": 1})
    tests.append({"args": [0b11111111], "expected": 8})
    tests.append({"args": [0b00101101], "expected": 4})
    # execute test cases
    for i, test in enumerate(tests):
        print("Running test %d: " % i, end="")
        args = test["args"]
        expected = test["expected"]
        ret = weight_binary_number(*args)
        print(
            "Pass" if ret == expected else "Fail. Expected %d, got %d" % (expected, ret)
        )
    print()


weight_binary_number_test()