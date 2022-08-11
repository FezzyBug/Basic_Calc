import sys

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. " \
        "You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

global_M = 0.0
global_single_count = 0


def numeric(num1, operator, num2):
    if '+' in operator:
        answer = num1 + num2
    elif '-' in operator:
        answer = num1 - num2
    elif '*' in operator:
        answer = num1 * num2
    elif '/' in operator:
        answer = num1 / num2
    return answer


def store_mem(choice, final):
    if choice == "y":
        return final
    else:
        return 0


def lazy_check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if (x == 1 or y == 1) and oper in "*":
        msg = msg + msg_7
    if (x == 0 or y == 0) and oper in "*-+":
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


def is_one_digit(num):
    if num.is_integer():
        if -10 < num < 10:
            return True
    else:
        return False


def silly_digit(count, num):
    if count == 1:
        print(msg_10)
    if count == 2:
        print(msg_11)
    if count == 3:
        print(msg_12)
    if count == 4:
        global_M = final



while True:
    print(msg_0)
    try:
        x, oper, y = input().split()

        if y in "M":
            y = global_M
        if x in "M":
            x = global_M

        lazy_check(float(x), float(y), oper)
        final = numeric(float(x), oper, float(y))
        print(final)

    except ValueError:
        print(msg_1)
        continue

    except ZeroDivisionError:
        print(msg_3)
        continue

    except:
        print(msg_2)

    else:
        print(msg_4)
        while True:
            choice = input()
            if choice in 'yn':
                if choice == 'y' and is_one_digit(final) and global_single_count < 3:
                        global_single_count += 1
                        silly_digit(global_single_count, final)
                        continue
                elif choice == 'y':
                    global_M = final
                    break
                else:
                    break

        print(msg_5)
        choice = input()
        if choice in 'yn':
            if choice == 'y':
                global_single_count = 0;
                pass
            else:
                sys.exit()


