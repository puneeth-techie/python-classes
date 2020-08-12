def list_creation():
    y = []
    x = int(input('Enter 1 to continue or any to escape'))

    if x == 1:
        n = int(input('Enter the number of items you want in your list'))
        for i in range(1, n+1):
            value = input('Enter {} value to add it in list'.format(i))
            if value.isnumeric() == True:
                y.append(int(value))
            else:
                y.append(value)
        print('Here is youe list: ', y)
    else:
        print('Sorry..!')


list_creation()
