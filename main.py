def application():
    try:
        a = input("Enter the name:")
        if(len(a)>=5):
            print(a)
        else:
            raise Exception
        b = int(input("Enter the age:"))
        c = input("Enter the gender:")
        d = int(input("Enter the salary:"))
        e = input("Enter the state:")
        f = input("Enter the city:")
        if(len(f)>4):
            print(f)
        else:
            print("Enter the valid city name")
        print(b)
        print(c)
        print(d)
        print(e)
    except:
        print("Enter the valid name")
