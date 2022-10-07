def hello():
    print("Greetings")

def pack(x,y,z):
    return[x,y,z]

def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_lunch)):
            if i == 0:
                print(f"First I eat {my_lunch[0]}")
            else:
                print(f"Next I eat {my_lunch[i]}")

hello()
print(pack("x","y","z"))
eat_lunch([])
eat_lunch(["nuggets", "salad", "carrots", "almonds"])