# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Car.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Car.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tCar.proto\"\xfe\x01\n\x03\x43\x61r\x12\x13\n\x05model\x18\x01 \x02(\t:\x04\x66ord\x12\"\n\x04type\x18\x02 \x02(\x0e\x32\r.Car.BodyType:\x05sedan\x12\r\n\x05\x63olor\x18\x03 \x01(\t\x12\x12\n\x04year\x18\x04 \x02(\x05:\x04\x32\x30\x30\x30\x12!\n\rpreviousOwner\x18\x05 \x02(\x0b\x32\n.Car.Owner\x12\t\n\x01\x61\x18\x06 \x02(\x02\x1a>\n\x05Owner\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08lastName\x18\x02 \x02(\t\x12\x15\n\rdriverLicense\x18\x03 \x02(\x03\"-\n\x08\x42odyType\x12\t\n\x05sedan\x10\x00\x12\r\n\thatchback\x10\x01\x12\x07\n\x03SUV\x10\x02'
)



_CAR_BODYTYPE = _descriptor.EnumDescriptor(
  name='BodyType',
  full_name='Car.BodyType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='sedan', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='hatchback', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUV', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=223,
  serialized_end=268,
)
_sym_db.RegisterEnumDescriptor(_CAR_BODYTYPE)


_CAR_OWNER = _descriptor.Descriptor(
  name='Owner',
  full_name='Car.Owner',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Car.Owner.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lastName', full_name='Car.Owner.lastName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='driverLicense', full_name='Car.Owner.driverLicense', index=2,
      number=3, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=159,
  serialized_end=221,
)

_CAR = _descriptor.Descriptor(
  name='Car',
  full_name='Car',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='Car.model', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=b"ford".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='Car.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='color', full_name='Car.color', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='Car.year', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=2000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previousOwner', full_name='Car.previousOwner', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='a', full_name='Car.a', index=5,
      number=6, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CAR_OWNER, ],
  enum_types=[
    _CAR_BODYTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=268,
)

_CAR_OWNER.containing_type = _CAR
_CAR.fields_by_name['type'].enum_type = _CAR_BODYTYPE
_CAR.fields_by_name['previousOwner'].message_type = _CAR_OWNER
_CAR_BODYTYPE.containing_type = _CAR
DESCRIPTOR.message_types_by_name['Car'] = _CAR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Car = _reflection.GeneratedProtocolMessageType('Car', (_message.Message,), {

  'Owner' : _reflection.GeneratedProtocolMessageType('Owner', (_message.Message,), {
    'DESCRIPTOR' : _CAR_OWNER,
    '__module__' : 'Car_pb2'
    # @@protoc_insertion_point(class_scope:Car.Owner)
    })
  ,
  'DESCRIPTOR' : _CAR,
  '__module__' : 'Car_pb2'
  # @@protoc_insertion_point(class_scope:Car)
  })
_sym_db.RegisterMessage(Car)
_sym_db.RegisterMessage(Car.Owner)


# @@protoc_insertion_point(module_scope)
