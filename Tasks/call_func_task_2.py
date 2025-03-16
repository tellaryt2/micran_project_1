def func(a, b, c, true_a=None, true_b=None, true_c=None):
    if true_a is not None:
        return a == true_a
    elif true_b is not None:
        return b == true_b
    elif true_c is not None:
        return c == true_c
    else:
        return False

def find_true_value(true_a=None, true_b=None, true_c=None):
    iteration_count = 0
    true_value = None
    found = False

    for a in range(1, 11):
        if found:
            break
        for b in range(1, 13):
            if found:
                break
            for c in range(1, 6):
                iteration_count += 1
                if func(a, b, c, true_a, true_b, true_c):
                    true_value = (a, b, c)
                    found = True
                    break

    return iteration_count, true_value


