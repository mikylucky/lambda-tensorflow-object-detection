# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/example/example_parser_configuration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.framework import tensor_shape_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2
from tensorflow.core.framework import tensor_pb2 as tensorflow_dot_core_dot_framework_dot_tensor__pb2
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/example/example_parser_configuration.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n:tensorflow/core/example/example_parser_configuration.proto\x12\ntensorflow\x1a,tensorflow/core/framework/tensor_shape.proto\x1a&tensorflow/core/framework/tensor.proto\x1a%tensorflow/core/framework/types.proto\"\xa3\x01\n\x12VarLenFeatureProto\x12#\n\x05\x64type\x18\x01 \x01(\x0e\x32\x14.tensorflow.DataType\x12!\n\x19values_output_tensor_name\x18\x02 \x01(\t\x12\"\n\x1aindices_output_tensor_name\x18\x03 \x01(\t\x12!\n\x19shapes_output_tensor_name\x18\x04 \x01(\t\"\xbb\x01\n\x14\x46ixedLenFeatureProto\x12#\n\x05\x64type\x18\x01 \x01(\x0e\x32\x14.tensorflow.DataType\x12+\n\x05shape\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12.\n\rdefault_value\x18\x03 \x01(\x0b\x32\x17.tensorflow.TensorProto\x12!\n\x19values_output_tensor_name\x18\x04 \x01(\t\"\x9a\x01\n\x14\x46\x65\x61tureConfiguration\x12=\n\x11\x66ixed_len_feature\x18\x01 \x01(\x0b\x32 .tensorflow.FixedLenFeatureProtoH\x00\x12\x39\n\x0fvar_len_feature\x18\x02 \x01(\x0b\x32\x1e.tensorflow.VarLenFeatureProtoH\x00\x42\x08\n\x06\x63onfig\"\xbe\x01\n\x1a\x45xampleParserConfiguration\x12K\n\x0b\x66\x65\x61ture_map\x18\x01 \x03(\x0b\x32\x36.tensorflow.ExampleParserConfiguration.FeatureMapEntry\x1aS\n\x0f\x46\x65\x61tureMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12/\n\x05value\x18\x02 \x01(\x0b\x32 .tensorflow.FeatureConfiguration:\x02\x38\x01\x42|\n\x16org.tensorflow.exampleB ExampleParserConfigurationProtosP\x01Z;github.com/tensorflow/tensorflow/tensorflow/go/core/example\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_tensor__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])




_VARLENFEATUREPROTO = _descriptor.Descriptor(
  name='VarLenFeatureProto',
  full_name='tensorflow.VarLenFeatureProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorflow.VarLenFeatureProto.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values_output_tensor_name', full_name='tensorflow.VarLenFeatureProto.values_output_tensor_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indices_output_tensor_name', full_name='tensorflow.VarLenFeatureProto.indices_output_tensor_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shapes_output_tensor_name', full_name='tensorflow.VarLenFeatureProto.shapes_output_tensor_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=200,
  serialized_end=363,
)


_FIXEDLENFEATUREPROTO = _descriptor.Descriptor(
  name='FixedLenFeatureProto',
  full_name='tensorflow.FixedLenFeatureProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorflow.FixedLenFeatureProto.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shape', full_name='tensorflow.FixedLenFeatureProto.shape', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_value', full_name='tensorflow.FixedLenFeatureProto.default_value', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='values_output_tensor_name', full_name='tensorflow.FixedLenFeatureProto.values_output_tensor_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=366,
  serialized_end=553,
)


_FEATURECONFIGURATION = _descriptor.Descriptor(
  name='FeatureConfiguration',
  full_name='tensorflow.FeatureConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fixed_len_feature', full_name='tensorflow.FeatureConfiguration.fixed_len_feature', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='var_len_feature', full_name='tensorflow.FeatureConfiguration.var_len_feature', index=1,
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
    _descriptor.OneofDescriptor(
      name='config', full_name='tensorflow.FeatureConfiguration.config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=556,
  serialized_end=710,
)


_EXAMPLEPARSERCONFIGURATION_FEATUREMAPENTRY = _descriptor.Descriptor(
  name='FeatureMapEntry',
  full_name='tensorflow.ExampleParserConfiguration.FeatureMapEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.ExampleParserConfiguration.FeatureMapEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.ExampleParserConfiguration.FeatureMapEntry.value', index=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=820,
  serialized_end=903,
)

_EXAMPLEPARSERCONFIGURATION = _descriptor.Descriptor(
  name='ExampleParserConfiguration',
  full_name='tensorflow.ExampleParserConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feature_map', full_name='tensorflow.ExampleParserConfiguration.feature_map', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_EXAMPLEPARSERCONFIGURATION_FEATUREMAPENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=903,
)

_VARLENFEATUREPROTO.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_FIXEDLENFEATUREPROTO.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_FIXEDLENFEATUREPROTO.fields_by_name['shape'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_FIXEDLENFEATUREPROTO.fields_by_name['default_value'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__pb2._TENSORPROTO
_FEATURECONFIGURATION.fields_by_name['fixed_len_feature'].message_type = _FIXEDLENFEATUREPROTO
_FEATURECONFIGURATION.fields_by_name['var_len_feature'].message_type = _VARLENFEATUREPROTO
_FEATURECONFIGURATION.oneofs_by_name['config'].fields.append(
  _FEATURECONFIGURATION.fields_by_name['fixed_len_feature'])
_FEATURECONFIGURATION.fields_by_name['fixed_len_feature'].containing_oneof = _FEATURECONFIGURATION.oneofs_by_name['config']
_FEATURECONFIGURATION.oneofs_by_name['config'].fields.append(
  _FEATURECONFIGURATION.fields_by_name['var_len_feature'])
_FEATURECONFIGURATION.fields_by_name['var_len_feature'].containing_oneof = _FEATURECONFIGURATION.oneofs_by_name['config']
_EXAMPLEPARSERCONFIGURATION_FEATUREMAPENTRY.fields_by_name['value'].message_type = _FEATURECONFIGURATION
_EXAMPLEPARSERCONFIGURATION_FEATUREMAPENTRY.containing_type = _EXAMPLEPARSERCONFIGURATION
_EXAMPLEPARSERCONFIGURATION.fields_by_name['feature_map'].message_type = _EXAMPLEPARSERCONFIGURATION_FEATUREMAPENTRY
DESCRIPTOR.message_types_by_name['VarLenFeatureProto'] = _VARLENFEATUREPROTO
DESCRIPTOR.message_types_by_name['FixedLenFeatureProto'] = _FIXEDLENFEATUREPROTO
DESCRIPTOR.message_types_by_name['FeatureConfiguration'] = _FEATURECONFIGURATION
DESCRIPTOR.message_types_by_name['ExampleParserConfiguration'] = _EXAMPLEPARSERCONFIGURATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VarLenFeatureProto = _reflection.GeneratedProtocolMessageType('VarLenFeatureProto', (_message.Message,), dict(
  DESCRIPTOR = _VARLENFEATUREPROTO,
  __module__ = 'tensorflow.core.example.example_parser_configuration_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.VarLenFeatureProto)
  ))
_sym_db.RegisterMessage(VarLenFeatureProto)

FixedLenFeatureProto = _reflection.GeneratedProtocolMessageType('FixedLenFeatureProto', (_message.Message,), dict(
  DESCRIPTOR = _FIXEDLENFEATUREPROTO,
  __module__ = 'tensorflow.core.example.example_parser_configuration_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.FixedLenFeatureProto)
  ))
_sym_db.RegisterMessage(FixedLenFeatureProto)

FeatureConfiguration = _reflection.GeneratedProtocolMessageType('FeatureConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _FEATURECONFIGURATION,
  __module__ = 'tensorflow.core.example.example_parser_configuration_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.FeatureConfiguration)
  ))
_sym_db.RegisterMessage(FeatureConfiguration)

ExampleParserConfiguration = _reflection.GeneratedProtocolMessageType('ExampleParserConfiguration', (_message.Message,), dict(

  FeatureMapEntry = _reflection.GeneratedProtocolMessageType('FeatureMapEntry', (_message.Message,), dict(
    DESCRIPTOR = _EXAMPLEPARSERCONFIGURATION_FEATUREMAPENTRY,
    __module__ = 'tensorflow.core.example.example_parser_configuration_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.ExampleParserConfiguration.FeatureMapEntry)
    ))
  ,
  DESCRIPTOR = _EXAMPLEPARSERCONFIGURATION,
  __module__ = 'tensorflow.core.example.example_parser_configuration_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ExampleParserConfiguration)
  ))
_sym_db.RegisterMessage(ExampleParserConfiguration)
_sym_db.RegisterMessage(ExampleParserConfiguration.FeatureMapEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026org.tensorflow.exampleB ExampleParserConfigurationProtosP\001Z;github.com/tensorflow/tensorflow/tensorflow/go/core/example\370\001\001'))
_EXAMPLEPARSERCONFIGURATION_FEATUREMAPENTRY.has_options = True
_EXAMPLEPARSERCONFIGURATION_FEATUREMAPENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
