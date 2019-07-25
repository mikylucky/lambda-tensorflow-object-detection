# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/profiler/tfprof_output.proto

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
from tensorflow.core.framework import types_pb2 as tensorflow_dot_core_dot_framework_dot_types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/profiler/tfprof_output.proto',
  package='tensorflow.tfprof',
  syntax='proto3',
  serialized_pb=_b('\n,tensorflow/core/profiler/tfprof_output.proto\x12\x11tensorflow.tfprof\x1a,tensorflow/core/framework/tensor_shape.proto\x1a%tensorflow/core/framework/types.proto\"v\n\x11TFProfTensorProto\x12#\n\x05\x64type\x18\x01 \x01(\x0e\x32\x14.tensorflow.DataType\x12\x14\n\x0cvalue_double\x18\x02 \x03(\x01\x12\x13\n\x0bvalue_int64\x18\x03 \x03(\x03\x12\x11\n\tvalue_str\x18\x04 \x03(\t\"\x8e\x07\n\x0eGraphNodeProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x0ctensor_value\x18\x0f \x01(\x0b\x32$.tensorflow.tfprof.TFProfTensorProto\x12\x11\n\trun_count\x18\x15 \x01(\x03\x12\x13\n\x0b\x65xec_micros\x18\x02 \x01(\x03\x12\x1f\n\x17\x61\x63\x63\x65lerator_exec_micros\x18\x11 \x01(\x03\x12\x17\n\x0f\x63pu_exec_micros\x18\x12 \x01(\x03\x12\x17\n\x0frequested_bytes\x18\x03 \x01(\x03\x12\x12\n\npeak_bytes\x18\x18 \x01(\x03\x12\x16\n\x0eresidual_bytes\x18\x19 \x01(\x03\x12\x14\n\x0coutput_bytes\x18\x1a \x01(\x03\x12\x12\n\nparameters\x18\x04 \x01(\x03\x12\x11\n\tfloat_ops\x18\r \x01(\x03\x12\x0f\n\x07\x64\x65vices\x18\n \x03(\t\x12\x1e\n\x16total_definition_count\x18\x17 \x01(\x03\x12\x17\n\x0ftotal_run_count\x18\x16 \x01(\x03\x12\x19\n\x11total_exec_micros\x18\x06 \x01(\x03\x12%\n\x1dtotal_accelerator_exec_micros\x18\x13 \x01(\x03\x12\x1d\n\x15total_cpu_exec_micros\x18\x14 \x01(\x03\x12\x1d\n\x15total_requested_bytes\x18\x07 \x01(\x03\x12\x18\n\x10total_peak_bytes\x18\x1b \x01(\x03\x12\x1c\n\x14total_residual_bytes\x18\x1c \x01(\x03\x12\x1a\n\x12total_output_bytes\x18\x1d \x01(\x03\x12\x18\n\x10total_parameters\x18\x08 \x01(\x03\x12\x17\n\x0ftotal_float_ops\x18\x0e \x01(\x03\x12,\n\x06shapes\x18\x0b \x03(\x0b\x32\x1c.tensorflow.TensorShapeProto\x12H\n\x0cinput_shapes\x18\x10 \x03(\x0b\x32\x32.tensorflow.tfprof.GraphNodeProto.InputShapesEntry\x12\x33\n\x08\x63hildren\x18\x0c \x03(\x0b\x32!.tensorflow.tfprof.GraphNodeProto\x1aP\n\x10InputShapesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.tensorflow.TensorShapeProto:\x02\x38\x01\"\xed\x04\n\x13MultiGraphNodeProto\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x65xec_micros\x18\x02 \x01(\x03\x12\x1f\n\x17\x61\x63\x63\x65lerator_exec_micros\x18\x0c \x01(\x03\x12\x17\n\x0f\x63pu_exec_micros\x18\r \x01(\x03\x12\x17\n\x0frequested_bytes\x18\x03 \x01(\x03\x12\x12\n\npeak_bytes\x18\x10 \x01(\x03\x12\x16\n\x0eresidual_bytes\x18\x11 \x01(\x03\x12\x14\n\x0coutput_bytes\x18\x12 \x01(\x03\x12\x12\n\nparameters\x18\x04 \x01(\x03\x12\x11\n\tfloat_ops\x18\x05 \x01(\x03\x12\x19\n\x11total_exec_micros\x18\x06 \x01(\x03\x12%\n\x1dtotal_accelerator_exec_micros\x18\x0e \x01(\x03\x12\x1d\n\x15total_cpu_exec_micros\x18\x0f \x01(\x03\x12\x1d\n\x15total_requested_bytes\x18\x07 \x01(\x03\x12\x18\n\x10total_peak_bytes\x18\x13 \x01(\x03\x12\x1c\n\x14total_residual_bytes\x18\x14 \x01(\x03\x12\x1a\n\x12total_output_bytes\x18\x15 \x01(\x03\x12\x18\n\x10total_parameters\x18\x08 \x01(\x03\x12\x17\n\x0ftotal_float_ops\x18\t \x01(\x03\x12\x36\n\x0bgraph_nodes\x18\n \x03(\x0b\x32!.tensorflow.tfprof.GraphNodeProto\x12\x38\n\x08\x63hildren\x18\x0b \x03(\x0b\x32&.tensorflow.tfprof.MultiGraphNodeProto\"\xc2\x01\n\x0b\x41\x64viceProto\x12>\n\x08\x63heckers\x18\x01 \x03(\x0b\x32,.tensorflow.tfprof.AdviceProto.CheckersEntry\x1aW\n\rCheckersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.tensorflow.tfprof.AdviceProto.Checker:\x02\x38\x01\x1a\x1a\n\x07\x43hecker\x12\x0f\n\x07reports\x18\x02 \x03(\tb\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_types__pb2.DESCRIPTOR,])




_TFPROFTENSORPROTO = _descriptor.Descriptor(
  name='TFProfTensorProto',
  full_name='tensorflow.tfprof.TFProfTensorProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dtype', full_name='tensorflow.tfprof.TFProfTensorProto.dtype', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_double', full_name='tensorflow.tfprof.TFProfTensorProto.value_double', index=1,
      number=2, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_int64', full_name='tensorflow.tfprof.TFProfTensorProto.value_int64', index=2,
      number=3, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_str', full_name='tensorflow.tfprof.TFProfTensorProto.value_str', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=152,
  serialized_end=270,
)


_GRAPHNODEPROTO_INPUTSHAPESENTRY = _descriptor.Descriptor(
  name='InputShapesEntry',
  full_name='tensorflow.tfprof.GraphNodeProto.InputShapesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.tfprof.GraphNodeProto.InputShapesEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.tfprof.GraphNodeProto.InputShapesEntry.value', index=1,
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
  serialized_start=1103,
  serialized_end=1183,
)

_GRAPHNODEPROTO = _descriptor.Descriptor(
  name='GraphNodeProto',
  full_name='tensorflow.tfprof.GraphNodeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.tfprof.GraphNodeProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tensor_value', full_name='tensorflow.tfprof.GraphNodeProto.tensor_value', index=1,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='run_count', full_name='tensorflow.tfprof.GraphNodeProto.run_count', index=2,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exec_micros', full_name='tensorflow.tfprof.GraphNodeProto.exec_micros', index=3,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accelerator_exec_micros', full_name='tensorflow.tfprof.GraphNodeProto.accelerator_exec_micros', index=4,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu_exec_micros', full_name='tensorflow.tfprof.GraphNodeProto.cpu_exec_micros', index=5,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requested_bytes', full_name='tensorflow.tfprof.GraphNodeProto.requested_bytes', index=6,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peak_bytes', full_name='tensorflow.tfprof.GraphNodeProto.peak_bytes', index=7,
      number=24, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='residual_bytes', full_name='tensorflow.tfprof.GraphNodeProto.residual_bytes', index=8,
      number=25, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_bytes', full_name='tensorflow.tfprof.GraphNodeProto.output_bytes', index=9,
      number=26, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='tensorflow.tfprof.GraphNodeProto.parameters', index=10,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_ops', full_name='tensorflow.tfprof.GraphNodeProto.float_ops', index=11,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='devices', full_name='tensorflow.tfprof.GraphNodeProto.devices', index=12,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_definition_count', full_name='tensorflow.tfprof.GraphNodeProto.total_definition_count', index=13,
      number=23, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_run_count', full_name='tensorflow.tfprof.GraphNodeProto.total_run_count', index=14,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_exec_micros', full_name='tensorflow.tfprof.GraphNodeProto.total_exec_micros', index=15,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_accelerator_exec_micros', full_name='tensorflow.tfprof.GraphNodeProto.total_accelerator_exec_micros', index=16,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_cpu_exec_micros', full_name='tensorflow.tfprof.GraphNodeProto.total_cpu_exec_micros', index=17,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_requested_bytes', full_name='tensorflow.tfprof.GraphNodeProto.total_requested_bytes', index=18,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_peak_bytes', full_name='tensorflow.tfprof.GraphNodeProto.total_peak_bytes', index=19,
      number=27, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_residual_bytes', full_name='tensorflow.tfprof.GraphNodeProto.total_residual_bytes', index=20,
      number=28, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_output_bytes', full_name='tensorflow.tfprof.GraphNodeProto.total_output_bytes', index=21,
      number=29, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_parameters', full_name='tensorflow.tfprof.GraphNodeProto.total_parameters', index=22,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_float_ops', full_name='tensorflow.tfprof.GraphNodeProto.total_float_ops', index=23,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shapes', full_name='tensorflow.tfprof.GraphNodeProto.shapes', index=24,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_shapes', full_name='tensorflow.tfprof.GraphNodeProto.input_shapes', index=25,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='children', full_name='tensorflow.tfprof.GraphNodeProto.children', index=26,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GRAPHNODEPROTO_INPUTSHAPESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=273,
  serialized_end=1183,
)


_MULTIGRAPHNODEPROTO = _descriptor.Descriptor(
  name='MultiGraphNodeProto',
  full_name='tensorflow.tfprof.MultiGraphNodeProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.tfprof.MultiGraphNodeProto.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exec_micros', full_name='tensorflow.tfprof.MultiGraphNodeProto.exec_micros', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accelerator_exec_micros', full_name='tensorflow.tfprof.MultiGraphNodeProto.accelerator_exec_micros', index=2,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpu_exec_micros', full_name='tensorflow.tfprof.MultiGraphNodeProto.cpu_exec_micros', index=3,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requested_bytes', full_name='tensorflow.tfprof.MultiGraphNodeProto.requested_bytes', index=4,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='peak_bytes', full_name='tensorflow.tfprof.MultiGraphNodeProto.peak_bytes', index=5,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='residual_bytes', full_name='tensorflow.tfprof.MultiGraphNodeProto.residual_bytes', index=6,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_bytes', full_name='tensorflow.tfprof.MultiGraphNodeProto.output_bytes', index=7,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='tensorflow.tfprof.MultiGraphNodeProto.parameters', index=8,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_ops', full_name='tensorflow.tfprof.MultiGraphNodeProto.float_ops', index=9,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_exec_micros', full_name='tensorflow.tfprof.MultiGraphNodeProto.total_exec_micros', index=10,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_accelerator_exec_micros', full_name='tensorflow.tfprof.MultiGraphNodeProto.total_accelerator_exec_micros', index=11,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_cpu_exec_micros', full_name='tensorflow.tfprof.MultiGraphNodeProto.total_cpu_exec_micros', index=12,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_requested_bytes', full_name='tensorflow.tfprof.MultiGraphNodeProto.total_requested_bytes', index=13,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_peak_bytes', full_name='tensorflow.tfprof.MultiGraphNodeProto.total_peak_bytes', index=14,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_residual_bytes', full_name='tensorflow.tfprof.MultiGraphNodeProto.total_residual_bytes', index=15,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_output_bytes', full_name='tensorflow.tfprof.MultiGraphNodeProto.total_output_bytes', index=16,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_parameters', full_name='tensorflow.tfprof.MultiGraphNodeProto.total_parameters', index=17,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_float_ops', full_name='tensorflow.tfprof.MultiGraphNodeProto.total_float_ops', index=18,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='graph_nodes', full_name='tensorflow.tfprof.MultiGraphNodeProto.graph_nodes', index=19,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='children', full_name='tensorflow.tfprof.MultiGraphNodeProto.children', index=20,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1186,
  serialized_end=1807,
)


_ADVICEPROTO_CHECKERSENTRY = _descriptor.Descriptor(
  name='CheckersEntry',
  full_name='tensorflow.tfprof.AdviceProto.CheckersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.tfprof.AdviceProto.CheckersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.tfprof.AdviceProto.CheckersEntry.value', index=1,
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
  serialized_start=1889,
  serialized_end=1976,
)

_ADVICEPROTO_CHECKER = _descriptor.Descriptor(
  name='Checker',
  full_name='tensorflow.tfprof.AdviceProto.Checker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reports', full_name='tensorflow.tfprof.AdviceProto.Checker.reports', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1978,
  serialized_end=2004,
)

_ADVICEPROTO = _descriptor.Descriptor(
  name='AdviceProto',
  full_name='tensorflow.tfprof.AdviceProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='checkers', full_name='tensorflow.tfprof.AdviceProto.checkers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ADVICEPROTO_CHECKERSENTRY, _ADVICEPROTO_CHECKER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1810,
  serialized_end=2004,
)

_TFPROFTENSORPROTO.fields_by_name['dtype'].enum_type = tensorflow_dot_core_dot_framework_dot_types__pb2._DATATYPE
_GRAPHNODEPROTO_INPUTSHAPESENTRY.fields_by_name['value'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_GRAPHNODEPROTO_INPUTSHAPESENTRY.containing_type = _GRAPHNODEPROTO
_GRAPHNODEPROTO.fields_by_name['tensor_value'].message_type = _TFPROFTENSORPROTO
_GRAPHNODEPROTO.fields_by_name['shapes'].message_type = tensorflow_dot_core_dot_framework_dot_tensor__shape__pb2._TENSORSHAPEPROTO
_GRAPHNODEPROTO.fields_by_name['input_shapes'].message_type = _GRAPHNODEPROTO_INPUTSHAPESENTRY
_GRAPHNODEPROTO.fields_by_name['children'].message_type = _GRAPHNODEPROTO
_MULTIGRAPHNODEPROTO.fields_by_name['graph_nodes'].message_type = _GRAPHNODEPROTO
_MULTIGRAPHNODEPROTO.fields_by_name['children'].message_type = _MULTIGRAPHNODEPROTO
_ADVICEPROTO_CHECKERSENTRY.fields_by_name['value'].message_type = _ADVICEPROTO_CHECKER
_ADVICEPROTO_CHECKERSENTRY.containing_type = _ADVICEPROTO
_ADVICEPROTO_CHECKER.containing_type = _ADVICEPROTO
_ADVICEPROTO.fields_by_name['checkers'].message_type = _ADVICEPROTO_CHECKERSENTRY
DESCRIPTOR.message_types_by_name['TFProfTensorProto'] = _TFPROFTENSORPROTO
DESCRIPTOR.message_types_by_name['GraphNodeProto'] = _GRAPHNODEPROTO
DESCRIPTOR.message_types_by_name['MultiGraphNodeProto'] = _MULTIGRAPHNODEPROTO
DESCRIPTOR.message_types_by_name['AdviceProto'] = _ADVICEPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TFProfTensorProto = _reflection.GeneratedProtocolMessageType('TFProfTensorProto', (_message.Message,), dict(
  DESCRIPTOR = _TFPROFTENSORPROTO,
  __module__ = 'tensorflow.core.profiler.tfprof_output_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tfprof.TFProfTensorProto)
  ))
_sym_db.RegisterMessage(TFProfTensorProto)

GraphNodeProto = _reflection.GeneratedProtocolMessageType('GraphNodeProto', (_message.Message,), dict(

  InputShapesEntry = _reflection.GeneratedProtocolMessageType('InputShapesEntry', (_message.Message,), dict(
    DESCRIPTOR = _GRAPHNODEPROTO_INPUTSHAPESENTRY,
    __module__ = 'tensorflow.core.profiler.tfprof_output_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.tfprof.GraphNodeProto.InputShapesEntry)
    ))
  ,
  DESCRIPTOR = _GRAPHNODEPROTO,
  __module__ = 'tensorflow.core.profiler.tfprof_output_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tfprof.GraphNodeProto)
  ))
_sym_db.RegisterMessage(GraphNodeProto)
_sym_db.RegisterMessage(GraphNodeProto.InputShapesEntry)

MultiGraphNodeProto = _reflection.GeneratedProtocolMessageType('MultiGraphNodeProto', (_message.Message,), dict(
  DESCRIPTOR = _MULTIGRAPHNODEPROTO,
  __module__ = 'tensorflow.core.profiler.tfprof_output_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tfprof.MultiGraphNodeProto)
  ))
_sym_db.RegisterMessage(MultiGraphNodeProto)

AdviceProto = _reflection.GeneratedProtocolMessageType('AdviceProto', (_message.Message,), dict(

  CheckersEntry = _reflection.GeneratedProtocolMessageType('CheckersEntry', (_message.Message,), dict(
    DESCRIPTOR = _ADVICEPROTO_CHECKERSENTRY,
    __module__ = 'tensorflow.core.profiler.tfprof_output_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.tfprof.AdviceProto.CheckersEntry)
    ))
  ,

  Checker = _reflection.GeneratedProtocolMessageType('Checker', (_message.Message,), dict(
    DESCRIPTOR = _ADVICEPROTO_CHECKER,
    __module__ = 'tensorflow.core.profiler.tfprof_output_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.tfprof.AdviceProto.Checker)
    ))
  ,
  DESCRIPTOR = _ADVICEPROTO,
  __module__ = 'tensorflow.core.profiler.tfprof_output_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.tfprof.AdviceProto)
  ))
_sym_db.RegisterMessage(AdviceProto)
_sym_db.RegisterMessage(AdviceProto.CheckersEntry)
_sym_db.RegisterMessage(AdviceProto.Checker)


_GRAPHNODEPROTO_INPUTSHAPESENTRY.has_options = True
_GRAPHNODEPROTO_INPUTSHAPESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_ADVICEPROTO_CHECKERSENTRY.has_options = True
_ADVICEPROTO_CHECKERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
