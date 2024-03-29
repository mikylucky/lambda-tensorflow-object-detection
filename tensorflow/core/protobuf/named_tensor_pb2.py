# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/named_tensor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/named_tensor.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n+tensorflow/core/protobuf/named_tensor.proto\x12\ntensorflow\x1a&tensorflow/core/framework/tensor.proto\"I\n\x10NamedTensorProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\'\n\x06tensor\x18\x02 \x01(\x0b\x32\x17.tensorflow.TensorProtoBp\n\x18org.tensorflow.frameworkB\x11NamedTensorProtosP\x01Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR,])




_NAMEDTENSORPROTO = _descriptor.Descriptor(
  name='NamedTensorProto',
  full_name='tensorflow.NamedTensorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.NamedTensorProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor', full_name='tensorflow.NamedTensorProto.tensor', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=99,
  serialized_end=172,
)

_NAMEDTENSORPROTO.fields_by_name['tensor'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
DESCRIPTOR.message_types_by_name['NamedTensorProto'] = _NAMEDTENSORPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NamedTensorProto = _reflection.GeneratedProtocolMessageType('NamedTensorProto', (_message.Message,), dict(
  DESCRIPTOR = _NAMEDTENSORPROTO,
  __module__ = 'tensorflow.core.protobuf.named_tensor_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.NamedTensorProto)
  ))
_sym_db.RegisterMessage(NamedTensorProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\021NamedTensorProtosP\001Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\370\001\001'))
# @@protoc_insertion_point(module_scope)
