import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import Protobuf as pb
import Car_pb2


class TestProtobuf(unittest.TestCase):
    def test_simple(self):
        Car = pb.create('Car.proto')
        car = Car(type=Car.BodyType.sedan, year=2000,
                  previousOwner=Car.Owner('Viktoria', 'Tarasova', 12345), a=3.14)
        car.to_file('car.bin')

        car2 = Car_pb2.Car(model='ford', type=0, year=2000, a=3.14)

        owner = car2.previousOwner
        owner.name = 'Viktoria'
        owner.lastName = 'Tarasova'
        owner.driverLicense = 12345

        a = car2.SerializeToString()

        with open('car.bin', 'rb') as f:
            data = f.read()
            self.assertEqual(data, a)

    def test_bin_comp1(self):
        Car = pb.create('Car.proto')
        car2 = Car_pb2.Car(model='ford', type=0, year=2000, a=3.14)

        owner = car2.previousOwner
        owner.name = 'Viktoria'
        owner.lastName = 'Tarasova'
        owner.driverLicense = 12345

        a = car2.SerializeToString()

        car1 = Car.from_bytes(a)
        self.assertEqual(car1.model, car2.model)
        self.assertEqual(car1.year, car2.year)
        self.assertEqual(car1.a, car2.a)
        self.assertEqual(car1.type, Car.BodyType(car2.type))
        self.assertEqual(car1.previousOwner.name, car2.previousOwner.name)
        self.assertEqual(car1.previousOwner.lastName, car2.previousOwner.lastName)
        self.assertEqual(car1.previousOwner.driverLicense, car2.previousOwner.driverLicense)

    def test_bin_comp2(self):
        Car = pb.create('Car.proto')
        car1 = Car(type=Car.BodyType.sedan, year=2000,
                   previousOwner=Car.Owner('Viktoria', 'Tarasova', 12345), a=3.14)
        car1.to_file('car2.bin')

        car2 = Car_pb2.Car()
        with open('car2.bin', 'rb') as f:
            data = f.read()

        car2.ParseFromString(data)

        self.assertEqual(car1.model, car2.model)
        self.assertEqual(car1.year, car2.year)
        self.assertEqual(car1.type, Car.BodyType(car2.type))
        self.assertEqual(car1.previousOwner.name, car2.previousOwner.name)
        self.assertEqual(car1.previousOwner.lastName, car2.previousOwner.lastName)
        self.assertEqual(car1.previousOwner.driverLicense, car2.previousOwner.driverLicense)
        self.assertTrue(abs(car1.a - car2.a) < 1e-6)
