# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/cluster.proto

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
  name='tensorflow/core/protobuf/cluster.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n&tensorflow/core/protobuf/cluster.proto\x12\ntensorflow\"r\n\x06JobDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x05tasks\x18\x02 \x03(\x0b\x32\x1d.tensorflow.JobDef.TasksEntry\x1a,\n\nTasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\nClusterDef\x12\x1f\n\x03job\x18\x01 \x03(\x0b\x32\x12.tensorflow.JobDefBn\n\x1aorg.tensorflow.distruntimeB\rClusterProtosP\x01Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\xf8\x01\x01\x62\x06proto3')
)




_JOBDEF_TASKSENTRY = _descriptor.Descriptor(
  name='TasksEntry',
  full_name='tensorflow.JobDef.TasksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.JobDef.TasksEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.JobDef.TasksEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=168,
)

_JOBDEF = _descriptor.Descriptor(
  name='JobDef',
  full_name='tensorflow.JobDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.JobDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='tensorflow.JobDef.tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_JOBDEF_TASKSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=168,
)


_CLUSTERDEF = _descriptor.Descriptor(
  name='ClusterDef',
  full_name='tensorflow.ClusterDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='tensorflow.ClusterDef.job', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=170,
  serialized_end=215,
)

_JOBDEF_TASKSENTRY.containing_type = _JOBDEF
_JOBDEF.fields_by_name['tasks'].message_type = _JOBDEF_TASKSENTRY
_CLUSTERDEF.fields_by_name['job'].message_type = _JOBDEF
DESCRIPTOR.message_types_by_name['JobDef'] = _JOBDEF
DESCRIPTOR.message_types_by_name['ClusterDef'] = _CLUSTERDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobDef = _reflection.GeneratedProtocolMessageType('JobDef', (_message.Message,), dict(

  TasksEntry = _reflection.GeneratedProtocolMessageType('TasksEntry', (_message.Message,), dict(
    DESCRIPTOR = _JOBDEF_TASKSENTRY,
    __module__ = 'tensorflow.core.protobuf.cluster_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.JobDef.TasksEntry)
    ))
  ,
  DESCRIPTOR = _JOBDEF,
  __module__ = 'tensorflow.core.protobuf.cluster_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.JobDef)
  ))
_sym_db.RegisterMessage(JobDef)
_sym_db.RegisterMessage(JobDef.TasksEntry)

ClusterDef = _reflection.GeneratedProtocolMessageType('ClusterDef', (_message.Message,), dict(
  DESCRIPTOR = _CLUSTERDEF,
  __module__ = 'tensorflow.core.protobuf.cluster_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ClusterDef)
  ))
_sym_db.RegisterMessage(ClusterDef)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032org.tensorflow.distruntimeB\rClusterProtosP\001Z<github.com/tensorflow/tensorflow/tensorflow/go/core/protobuf\370\001\001'))
_JOBDEF_TASKSENTRY.has_options = True
_JOBDEF_TASKSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
