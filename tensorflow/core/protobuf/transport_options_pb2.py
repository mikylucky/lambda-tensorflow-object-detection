# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/transport_options.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/transport_options.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n0tensorflow/core/protobuf/transport_options.proto\x12\ntensorflow\"*\n\x10RecvBufRespExtra\x12\x16\n\x0etensor_content\x18\x01 \x01(\x0c\x62\x06proto3')
)




_RECVBUFRESPEXTRA = _descriptor.Descriptor(
  name='RecvBufRespExtra',
  full_name='tensorflow.RecvBufRespExtra',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_content', full_name='tensorflow.RecvBufRespExtra.tensor_content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=64,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['RecvBufRespExtra'] = _RECVBUFRESPEXTRA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecvBufRespExtra = _reflection.GeneratedProtocolMessageType('RecvBufRespExtra', (_message.Message,), dict(
  DESCRIPTOR = _RECVBUFRESPEXTRA,
  __module__ = 'tensorflow.core.protobuf.transport_options_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.RecvBufRespExtra)
  ))
_sym_db.RegisterMessage(RecvBufRespExtra)


# @@protoc_insertion_point(module_scope)
