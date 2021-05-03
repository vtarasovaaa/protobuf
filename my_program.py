import Protobuf as pb
import Car_pb2

Car = pb.create('Car.proto')
car = Car(type=Car.BodyType.sedan, year=2000,
          previousOwner=Car.Owner('Viktoria', 'Tarasova', 12345), a=3.14)
car.to_file('car.bin')
car1 = Car.from_file('car.bin')

car2 = Car_pb2.Car(model='ford', type=0, year=2000, a=3.14)

owner = car2.previousOwner
owner.name = 'Viktoria'
owner.lastName = 'Tarasova'
owner.driverLicense = 12345

a = car2.SerializeToString()
print(a)

with open('car.bin', 'rb') as f:
    data = f.read()
    print(data)
    for e in range(len(data)):
        print(f'{data[e]}  {a[e]}')
