def trinity_choose():
    print("Choose one of trinity number system: Symmetric or Asymmetric")
    trinity = input()
    if trinity == "Symmetric":
        print("Chosen Symmetric")

    elif trinity == "Asymmetric":
        print("Chosen Asymmetric")
    else:
        print("Somethng goes wrong")
        trinity_choose()


def input_check():
    num_sys = input()
    if num_sys == '2':
        return True
    if num_sys == '3':
        trinity_choose()
    if num_sys == '8':
        return True
    if num_sys == '10':
        return True
    if num_sys == '16':
        return True

    else:
        return False


def output_check(num_sys):
    if num_sys == "2" or "3" or "8" or "10" or "16":
        return 1
    else:
        return 0


def second_step():
    print("Now choose the output number system")
    print("2, 3, 8, 10 or 16")
    output_num_sys = input()
    if output_check(output_num_sys):
        print("Yo, nice")
    else:
        print("There's some problem with number system you put, try again")


def first_step():
    print("Hello user! Lets make some deal on that numbers")
    print("Choose the number system first")
    print("2, 3, 8, 10 or 16")
    if not input_check():
        print("There's some problem with number system you put, try again")
    else:
        second_step()


def repeat():
    first_step()


repeat()
