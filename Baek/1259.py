while True:
    n=input()
    if (n=='0'):
        break
    rev=n[::-1]

    if n ==rev:
        print("yes")
    else:
        print("no")