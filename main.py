def input_check(num_sys):
    if num_sys == "2" or "3" or "8" or "10" or "16":
        return 1
    else:
        return 0


def output_check(num_sys):
    if num_sys == "2" or "3" or "8" or "10" or "16":
        return 1
    else:
        return 0


def first_step():
    print("Hello user! Lets make some deal on that numbers")
    print("Choose the number system first")
    print("2, 3, 8, 10 or 16")
    input_num_sys = input()

    if input_check(input_num_sys) == 1:

        print("Now choose the output number system")
        print("2, 3, 8, 10 or 16")
        output_num_sys = input()
        if output_check(output_num_sys) == 1:
            print("Yo, nice")
        else:
            print("There's some problem with number system you put, try again")
    else:
        print("There's some problem with number system you put, try again")
