import random
import string


def gen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.punctuation
    s4 = string.digits

    passlen = int(input("Enter the password length\n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)

    pwd = ("".join(s[0:passlen]))
    print(pwd)


gen()
