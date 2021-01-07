import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import Protobuf as pb


class TestProtobuf(unittest.TestCase):
    def test_simple(self):
        A = pb.create(os.path.join('tests files', 'simple.proto'))
        a = A(1)
        self.assertEqual(a.A, 1)

    def test_simple_without_spaces(self):
        A = pb.create(
            os.path.join('tests files', 'simple_without_spaces.proto'))
        a = A(1)
        self.assertEqual(a.A, 1)

    def test_simple_without_spaces_extremal(self):
        A = pb.create(
            os.path.join('tests files', 'simple_without_spaces_2.proto'))
        a = A(1)
        self.assertEqual(a.A, 1)

    def test_simple_2(self):
        A = pb.create(os.path.join('tests files', 'simple_2.proto'))
        a = A(1, 2)
        self.assertEqual(a.A, 1)
        self.assertEqual(a.B, 2)

    def test_3_attributes(self):
        A = pb.create(os.path.join('tests files', 'class_3_attributes.proto'))
        a = A(1, True, 'hello')
        self.assertEqual(a.A, 1)
        self.assertEqual(a.B, True)
        self.assertEqual(a.C, 'hello')

    def test_with_enum(self):
        A = pb.create(os.path.join('tests files', 'class_with_enum.proto'))
        a = A(1, True, 'hello', A.D.a)
        self.assertEqual(a.A, 1)
        self.assertEqual(a.B, True)
        self.assertEqual(a.C, 'hello')
        self.assertEqual(a.d, A.D.a)

    def test_with_class(self):
        A = pb.create(os.path.join('tests files', 'class_with_class.proto'))
        a = A(1, True, 'hello', A.D(1, 2))
        self.assertEqual(a.A, 1)
        self.assertEqual(a.B, True)
        self.assertEqual(a.C, 'hello')
        self.assertEqual(a.d.a, 1)
        self.assertEqual(a.d.b, 2)

    def test_nested_classes(self):
        A = pb.create(os.path.join('tests files', 'more_nested_classes.proto'))
        a = A(1, True, 'hello', A.D(1, 2, A.D.E(3)))
        self.assertEqual(a.A, 1)
        self.assertEqual(a.B, True)
        self.assertEqual(a.C, 'hello')
        self.assertEqual(a.d.a, 1)
        self.assertEqual(a.d.b, 2)
        self.assertEqual(a.d.e.x, 3)

    def test_simple_wrong_arguments(self):
        A = pb.create(os.path.join('tests files', 'simple.proto'))
        self.assertRaises(AttributeError, A, 1, 2)
        self.assertRaises(AttributeError, A)


if __name__ == '__main__':
    unittest.main()
