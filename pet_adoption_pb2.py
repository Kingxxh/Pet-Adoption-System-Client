# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pet_adoption.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'pet_adoption.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12pet_adoption.proto\x12\x0bpetadoption\"T\n\x07PetInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06gender\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\r\n\x05\x62reed\x18\x04 \x01(\t\x12\x0f\n\x07picture\x18\x05 \x01(\x0c\"#\n\x10RegisterResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"+\n\rSearchRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"4\n\x0eSearchResponse\x12\"\n\x04pets\x18\x01 \x03(\x0b\x32\x14.petadoption.PetInfo2\x9e\x01\n\x12PetAdoptionService\x12\x42\n\x0bRegisterPet\x12\x14.petadoption.PetInfo\x1a\x1d.petadoption.RegisterResponse\x12\x44\n\tSearchPet\x12\x1a.petadoption.SearchRequest\x1a\x1b.petadoption.SearchResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pet_adoption_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PETINFO']._serialized_start=35
  _globals['_PETINFO']._serialized_end=119
  _globals['_REGISTERRESPONSE']._serialized_start=121
  _globals['_REGISTERRESPONSE']._serialized_end=156
  _globals['_SEARCHREQUEST']._serialized_start=158
  _globals['_SEARCHREQUEST']._serialized_end=201
  _globals['_SEARCHRESPONSE']._serialized_start=203
  _globals['_SEARCHRESPONSE']._serialized_end=255
  _globals['_PETADOPTIONSERVICE']._serialized_start=258
  _globals['_PETADOPTIONSERVICE']._serialized_end=416
# @@protoc_insertion_point(module_scope)