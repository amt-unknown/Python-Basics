def hello():
    print("Hello, world!")

def pack(arg_1, arg_2, arg_3):
    return[arg_1, arg_2, arg_3]

def eat_lunch(food_list):

    print("First I eat: " + food_list[0])

    counter = 1 
    while counter < len(food_list):
        print("Then I eat: " + food_list[counter])
        counter += 1
    print("My lunchbox is empty!")
        



todays_lunch = ["Sandwich", "Apple", "Cashews"]

hello()
print(pack(1,2,3,))
eat_lunch(todays_lunch)