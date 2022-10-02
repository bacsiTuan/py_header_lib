# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ping.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ping.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nping.proto\"\x1e\n\x0bPingRequest\x12\x0f\n\x07request\x18\x01 \x01(\t\"\x1c\n\tPingReply\x12\x0f\n\x07message\x18\x01 \x01(\t2+\n\x07\x41PIPing\x12 \n\x04Ping\x12\x0c.PingRequest\x1a\n.PingReplyb\x06proto3'
)




_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request', full_name='PingRequest.request', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=44,
)


_PINGREPLY = _descriptor.Descriptor(
  name='PingReply',
  full_name='PingReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='PingReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=74,
)

DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingReply'] = _PINGREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'ping_pb2'
  # @@protoc_insertion_point(class_scope:PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

PingReply = _reflection.GeneratedProtocolMessageType('PingReply', (_message.Message,), {
  'DESCRIPTOR' : _PINGREPLY,
  '__module__' : 'ping_pb2'
  # @@protoc_insertion_point(class_scope:PingReply)
  })
_sym_db.RegisterMessage(PingReply)



_APIPING = _descriptor.ServiceDescriptor(
  name='APIPing',
  full_name='APIPing',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=76,
  serialized_end=119,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='APIPing.Ping',
    index=0,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_APIPING)

DESCRIPTOR.services_by_name['APIPing'] = _APIPING

# @@protoc_insertion_point(module_scope)