# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='tutorial',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rexample.proto\x12\x08tutorial\"z\n\tConstants\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"@\n\nJosephType\x12\x0e\n\nSEUNGMYUNG\x10\x00\x12\n\n\x06JOSEPH\x10\x01\x12\n\n\x06JUNGHO\x10\x02\x12\n\n\x06KUNGYU\x10\x04\x62\x06proto3'
)



_CONSTANTS_PHONETYPE = _descriptor.EnumDescriptor(
  name='PhoneType',
  full_name='tutorial.Constants.PhoneType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOBILE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOME', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WORK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=40,
  serialized_end=83,
)
_sym_db.RegisterEnumDescriptor(_CONSTANTS_PHONETYPE)

_CONSTANTS_JOSEPHTYPE = _descriptor.EnumDescriptor(
  name='JosephType',
  full_name='tutorial.Constants.JosephType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SEUNGMYUNG', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JOSEPH', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JUNGHO', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KUNGYU', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=85,
  serialized_end=149,
)
_sym_db.RegisterEnumDescriptor(_CONSTANTS_JOSEPHTYPE)


_CONSTANTS = _descriptor.Descriptor(
  name='Constants',
  full_name='tutorial.Constants',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CONSTANTS_PHONETYPE,
    _CONSTANTS_JOSEPHTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=149,
)

_CONSTANTS_PHONETYPE.containing_type = _CONSTANTS
_CONSTANTS_JOSEPHTYPE.containing_type = _CONSTANTS
DESCRIPTOR.message_types_by_name['Constants'] = _CONSTANTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Constants = _reflection.GeneratedProtocolMessageType('Constants', (_message.Message,), {
  'DESCRIPTOR' : _CONSTANTS,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Constants)
  })
_sym_db.RegisterMessage(Constants)


# @@protoc_insertion_point(module_scope)
