class Mazda_RX7:
    name = 'Mazda RX 7'
    Description = 'This is the car Han Lue had in Tokyo drift'
    Speed = 'This cars top speed is 257 km/h'

    def description(self):
        desc = 'This car is really scarce and worth upto $40,000'

        return desc
    
class Toyota_MK4:
    name2 = 'Toyota MK IV'
    Description2 = 'This car is one of the best in street racing and was seen on Tokyo Drift'
    Speed = 'This cars top speed is 250 km/h'

    def description2(self):
        descr = 'This car is really rare and can go upto $100,000'
        print(descr)
        return descr
    

print("Please select one of the cars below", flush= True)  
print(Mazda_RX7.name , Toyota_MK4.name2,flush=True)
Users_selected_car = input("What car do you want to know about? : ")

if Users_selected_car == Mazda_RX7.name:
    print(Mazda_RX7.name,Mazda_RX7.Speed,Mazda_RX7.Description) 

elif Users_selected_car == Toyota_MK4.name2:
    print(Toyota_MK4.name2,
          Toyota_MK4.Speed,
          Toyota_MK4.Description2,
          Toyota_MK4.description2)

else: print('Select one of the cars given above')