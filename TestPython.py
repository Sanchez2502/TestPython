import json
# LOAD FILE
file = open("Cars.txt","r")
Cars = json.load(file)
file.close()

car=input("Enter car's name: ")
for i in range(10000):
    if Cars.get(car)==None:
        price=input("Enter car's price because we haven't this car: ")
        value=input("Enter value USD, EUR or GBP: ")
        if value=="USD":
            print(car+" "+price+" "+value)
            Cars.update({car:price+" "+value})
            break
        elif value == "EUR":
            print(car+" "+str(int(price)*1.1)+" USD")
            Cars.update({car:str(int(price)*1.1)+" USD"})
            break
        elif value == "GBP":
            print(car+" "+str(int(price)*1.23)+" USD")
            Cars.update({car:str(int(price)*1.23)+" USD"})
            break
        else :
            print("Error value. Please re-enter")
    else:
        print(Cars.get(car))
        break
# SAVE FILE
file = open("Cars.txt","w")
json.dump(Cars,file)
file.close()
