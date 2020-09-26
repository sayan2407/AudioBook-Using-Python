import pyttsx3


def audio(text):
    s = pyttsx3.init()
    s.say(text)
    s.runAndWait()


def num1(p):
    n = ""

    for i in p:
        if i == '+' or i == '-' or i == '*' or i == '/':
            break
        n += i
    return int(n)


def num2(p):
    n = ""
    b = 0
    for i in p:
        if i == '+' or i == '-' or i == '*' or i == '/':
            b = 1
            continue
        if b == 1:
            n += i

    return int(n)


def operator(p, n1, n2):
    for i in p:
        if i == '+' or i == '-' or i == '*' or i == '/':
            if i == '+':
                ans = n1 + n2
                audio("Answer is {0}: ".format(ans))
                print("Answer is {0}: ".format(ans))
            elif i == '-':
                ans = n1 - n2
                audio("Answer is : {0}".format(ans))
                print("Answer is : {0}".format(ans))
            elif i == '*':
                ans = n1 * n2
                audio("Answer is : {0}".format(ans))
                print("Answer is : {0}".format(ans))

            elif i == '/':
                ans = n1 / n2
                audio("Answer is : {0}".format(ans))
                print("Answer is : {0}".format(ans))
            else:
                audio("I did't get your sollution . sorry")


audio("Enter your problem")
p = input("Enter here : ")
n1 = num1(p)
n2 = num2(p)
print(n1)
print(n2)
operator(p, n1, n2)

# print(int(n))
