import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import Protobuf as pb
from protobuf.ProtobufSyntaxError import ProtobufSyntaxError


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
        a = A(1, '2')
        self.assertEqual(a.A, 1)
        self.assertEqual(a.B, '2')

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
        a = A(1, True, 'hello', A.D(1, '2'))
        self.assertEqual(a.A, 1)
        self.assertEqual(a.B, True)
        self.assertEqual(a.C, 'hello')
        self.assertEqual(a.d.a, 1)
        self.assertEqual(a.d.b, '2')

    def test_nested_classes(self):
        A = pb.create(os.path.join('tests files', 'more_nested_classes.proto'))
        a = A(A=1, B=True, C='hello', d=A.D(1, '2', A.D.E(3)))
        self.assertEqual(a.A, 1)
        self.assertEqual(a.B, True)
        self.assertEqual(a.C, 'hello')
        self.assertEqual(a.d.a, 1)
        self.assertEqual(a.d.b, '2')
        self.assertEqual(a.d.e.x, 3)

    def test_simple_wrong_arguments(self):
        A = pb.create(os.path.join('tests files', 'simple.proto'))
        self.assertRaises(TypeError, A, 1, 2)
        self.assertRaises(TypeError, A)

    def test_fails(self):
        self.assertRaises(ProtobufSyntaxError, pb.create,
                          os.path.join('tests files', 'fail_simple_int.proto'))
        self.assertRaises(ProtobufSyntaxError, pb.create,
                          os.path.join('tests files', 'fail_simple_str.proto'))
        self.assertRaises(ProtobufSyntaxError, pb.create,
                          os.path.join('tests files', 'fail_message.proto'))
        self.assertRaises(ProtobufSyntaxError, pb.create,
                          os.path.join('tests files', 'fail_message_2.proto'))
        self.assertRaises(ProtobufSyntaxError, pb.create,
                          os.path.join('tests files', 'fail_priority.proto'))
        self.assertRaises(ProtobufSyntaxError, pb.create,
                          os.path.join('tests files', 'fail_enum.proto'))
        self.assertRaises(ProtobufSyntaxError, pb.create,
                          os.path.join('tests files', 'fail_default.proto'))
        self.assertRaises(ProtobufSyntaxError, pb.create,
                          os.path.join('tests files', 'fail_default_2.proto'))
        self.assertRaises(ProtobufSyntaxError, pb.create,
                          os.path.join('tests files', 'fail_type.proto'))


if __name__ == '__main__':
    unittest.main()
