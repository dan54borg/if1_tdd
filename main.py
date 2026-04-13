def is_prime(input_value):
    if input_value < 2:
        return False
    for i in range(2, input_value):
        if input_value % i == 0:
            return False
    return True
