# n = 5
# answer = []
# if n > 0:
#     for i in range(n):
#         inarr = []
#         answer.append(inarr)

#     print(answer)

#     num = 0
#     for i in range(n):
#         if i == 0:
#             for w in range(1,n +1):
#                 num = w
#                 answer[i].append(w)
#         else:
#             num += 1 
#             answer[i].append(num)

#     last_item = answer[-1]
#     index = -1
#     for i in range(n-1):
#         num += 1
#         answer[-1].insert(index-1, num)
#         index -= 1


#     data = answer[-n + 1:-1]
#     data.reverse()
#     for i in range(len(data)):
#         for c in range(n-1):
#             num += 1
#             data[i].insert(c, num)
            
#     data.reverse()
#     answer[-n + 1:-1] = data
#     print(answer)
# else:
#     print(None)


class Car:
    def __init__(self, brand, color, no_of_tyres):
        self.brand = brand
        self.color = color
        self.no_of_tyres = no_of_tyres
        
    def move(self):
        return f'{self.no_of_tyres} tyres is rolling..., {self.brand} is moving'
    
    def stop(self):
        return f'{self.no_of_tyres} tyres has stoped!, {self.brand} has stoped'
    


ferrari = Car(brand='ferrari', color='red', no_of_tyres='4')
print(ferrari.brand)
print(ferrari.move())
ferrari.brand = 'ferrari newest model'
ferrari.typeOfCar = 'sportCar'
print(ferrari.move())
print(ferrari.typeOfCar)

class SportCar(Car):
    def __init__(self, brand, color, no_of_tyres, no_of_doors):
        super().__init__(brand, color, no_of_tyres)
        self.no_of_doors = no_of_doors
    

bugattiVeron = SportCar('bugatti', color='black', no_of_tyres=4, no_of_doors=2)
    
print(bugattiVeron.move())