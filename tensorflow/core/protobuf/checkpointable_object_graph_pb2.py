# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/checkpointable_object_graph.proto

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
  name='tensorflow/core/protobuf/checkpointable_object_graph.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n:tensorflow/core/protobuf/checkpointable_object_graph.proto\x12\ntensorflow\"\x9b\x05\n\x19\x43heckpointableObjectGraph\x12I\n\x05nodes\x18\x01 \x03(\x0b\x32:.tensorflow.CheckpointableObjectGraph.CheckpointableObject\x1a\xb2\x04\n\x14\x43heckpointableObject\x12\\\n\x08\x63hildren\x18\x01 \x03(\x0b\x32J.tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference\x12_\n\nattributes\x18\x02 \x03(\x0b\x32K.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor\x12h\n\x0eslot_variables\x18\x03 \x03(\x0b\x32P.tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference\x1a\x36\n\x0fObjectReference\x12\x0f\n\x07node_id\x18\x01 \x01(\x05\x12\x12\n\nlocal_name\x18\x02 \x01(\t\x1aK\n\x10SerializedTensor\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tfull_name\x18\x02 \x01(\t\x12\x16\n\x0e\x63heckpoint_key\x18\x03 \x01(\t\x1al\n\x15SlotVariableReference\x12!\n\x19original_variable_node_id\x18\x01 \x01(\x05\x12\x11\n\tslot_name\x18\x02 \x01(\t\x12\x1d\n\x15slot_variable_node_id\x18\x03 \x01(\x05\x42\x03\xf8\x01\x01\x62\x06proto3')
)




_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE = _descriptor.Descriptor(
  name='ObjectReference',
  full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference.node_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_name', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference.local_name', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=555,
)

_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR = _descriptor.Descriptor(
  name='SerializedTensor',
  full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_name', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor.full_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkpoint_key', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor.checkpoint_key', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=557,
  serialized_end=632,
)

_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE = _descriptor.Descriptor(
  name='SlotVariableReference',
  full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='original_variable_node_id', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference.original_variable_node_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_name', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference.slot_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_variable_node_id', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference.slot_variable_node_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=634,
  serialized_end=742,
)

_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT = _descriptor.Descriptor(
  name='CheckpointableObject',
  full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='children', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.children', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slot_variables', full_name='tensorflow.CheckpointableObjectGraph.CheckpointableObject.slot_variables', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE, _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR, _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=742,
)

_CHECKPOINTABLEOBJECTGRAPH = _descriptor.Descriptor(
  name='CheckpointableObjectGraph',
  full_name='tensorflow.CheckpointableObjectGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='tensorflow.CheckpointableObjectGraph.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=742,
)

_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE.containing_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR.containing_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE.containing_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT.fields_by_name['children'].message_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT.fields_by_name['attributes'].message_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT.fields_by_name['slot_variables'].message_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE
_CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT.containing_type = _CHECKPOINTABLEOBJECTGRAPH
_CHECKPOINTABLEOBJECTGRAPH.fields_by_name['nodes'].message_type = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT
DESCRIPTOR.message_types_by_name['CheckpointableObjectGraph'] = _CHECKPOINTABLEOBJECTGRAPH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CheckpointableObjectGraph = _reflection.GeneratedProtocolMessageType('CheckpointableObjectGraph', (_message.Message,), dict(

  CheckpointableObject = _reflection.GeneratedProtocolMessageType('CheckpointableObject', (_message.Message,), dict(

    ObjectReference = _reflection.GeneratedProtocolMessageType('ObjectReference', (_message.Message,), dict(
      DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_OBJECTREFERENCE,
      __module__ = 'tensorflow.core.protobuf.checkpointable_object_graph_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.CheckpointableObjectGraph.CheckpointableObject.ObjectReference)
      ))
    ,

    SerializedTensor = _reflection.GeneratedProtocolMessageType('SerializedTensor', (_message.Message,), dict(
      DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SERIALIZEDTENSOR,
      __module__ = 'tensorflow.core.protobuf.checkpointable_object_graph_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.CheckpointableObjectGraph.CheckpointableObject.SerializedTensor)
      ))
    ,

    SlotVariableReference = _reflection.GeneratedProtocolMessageType('SlotVariableReference', (_message.Message,), dict(
      DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT_SLOTVARIABLEREFERENCE,
      __module__ = 'tensorflow.core.protobuf.checkpointable_object_graph_pb2'
      # @@protoc_insertion_point(class_scope:tensorflow.CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference)
      ))
    ,
    DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH_CHECKPOINTABLEOBJECT,
    __module__ = 'tensorflow.core.protobuf.checkpointable_object_graph_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CheckpointableObjectGraph.CheckpointableObject)
    ))
  ,
  DESCRIPTOR = _CHECKPOINTABLEOBJECTGRAPH,
  __module__ = 'tensorflow.core.protobuf.checkpointable_object_graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.CheckpointableObjectGraph)
  ))
_sym_db.RegisterMessage(CheckpointableObjectGraph)
_sym_db.RegisterMessage(CheckpointableObjectGraph.CheckpointableObject)
_sym_db.RegisterMessage(CheckpointableObjectGraph.CheckpointableObject.ObjectReference)
_sym_db.RegisterMessage(CheckpointableObjectGraph.CheckpointableObject.SerializedTensor)
_sym_db.RegisterMessage(CheckpointableObjectGraph.CheckpointableObject.SlotVariableReference)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\370\001\001'))
# @@protoc_insertion_point(module_scope)
