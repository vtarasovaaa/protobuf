import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
import Protobuf as pb


class TestProtobufFail(unittest.TestCase):
    def test_fails(self):
        self.assertRaises(SyntaxError, pb.create,
                          os.path.join('tests files', 'fail_simple_int.proto'))
        self.assertRaises(SyntaxError, pb.create,
                          os.path.join('tests files', 'fail_simple_str.proto'))
        self.assertRaises(SyntaxError, pb.create,
                          os.path.join('tests files', 'fail_message.proto'))
        self.assertRaises(SyntaxError, pb.create,
                          os.path.join('tests files', 'fail_message_2.proto'))
        self.assertRaises(SyntaxError, pb.create,
                          os.path.join('tests files', 'fail_priority.proto'))
        self.assertRaises(SyntaxError, pb.create,
                          os.path.join('tests files', 'fail_enum.proto'))
        self.assertRaises(SyntaxError, pb.create,
                          os.path.join('tests files', 'fail_default.proto'))
        self.assertRaises(SyntaxError, pb.create,
                          os.path.join('tests files', 'fail_default_2.proto'))
        self.assertRaises(SyntaxError, pb.create,
                          os.path.join('tests files', 'fail_type.proto'))
