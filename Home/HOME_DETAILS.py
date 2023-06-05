with open(r"C:\Users\QSP\PycharmProjects\access_details\access-log.txt",'r') as fp:
    result = fp.readlines()
    print(result)


if __name__ == '__main__':
    for i in range(0, 5):
        print(result[i])

    print("--all__")


