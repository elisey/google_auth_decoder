# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: google_auth.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    "",
    "google_auth.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11google_auth.proto\x12\ngoogleauth"\x84\x05\n\x10MigrationPayload\x12\x42\n\x0eotp_parameters\x18\x01 \x03(\x0b\x32*.googleauth.MigrationPayload.OtpParameters\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x12\n\nbatch_size\x18\x03 \x01(\x05\x12\x13\n\x0b\x62\x61tch_index\x18\x04 \x01(\x05\x12\x10\n\x08\x62\x61tch_id\x18\x05 \x01(\x05\x1a\x89\x02\n\rOtpParameters\x12\x0e\n\x06secret\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06issuer\x18\x03 \x01(\t\x12\x39\n\talgorithm\x18\x04 \x01(\x0e\x32&.googleauth.MigrationPayload.Algorithm\x12\x37\n\x06\x64igits\x18\x05 \x01(\x0e\x32\'.googleauth.MigrationPayload.DigitCount\x12\x32\n\x04type\x18\x06 \x01(\x0e\x32$.googleauth.MigrationPayload.OtpType\x12\x0f\n\x07\x63ounter\x18\x07 \x01(\x03\x12\x11\n\tunique_id\x18\x08 \x01(\t"Q\n\tAlgorithm\x12\x19\n\x15\x41LGORITHM_UNSPECIFIED\x10\x00\x12\x08\n\x04SHA1\x10\x01\x12\n\n\x06SHA256\x10\x02\x12\n\n\x06SHA512\x10\x03\x12\x07\n\x03MD5\x10\x04"H\n\nDigitCount\x12\x1b\n\x17\x44IGIT_COUNT_UNSPECIFIED\x10\x00\x12\x07\n\x03SIX\x10\x01\x12\t\n\x05\x45IGHT\x10\x02\x12\t\n\x05SEVEN\x10\x03"7\n\x07OtpType\x12\x18\n\x14OTP_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04HOTP\x10\x01\x12\x08\n\x04TOTP\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "google_auth_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals["_MIGRATIONPAYLOAD"]._serialized_start=34
  _globals["_MIGRATIONPAYLOAD"]._serialized_end=678
  _globals["_MIGRATIONPAYLOAD_OTPPARAMETERS"]._serialized_start=199
  _globals["_MIGRATIONPAYLOAD_OTPPARAMETERS"]._serialized_end=464
  _globals["_MIGRATIONPAYLOAD_ALGORITHM"]._serialized_start=466
  _globals["_MIGRATIONPAYLOAD_ALGORITHM"]._serialized_end=547
  _globals["_MIGRATIONPAYLOAD_DIGITCOUNT"]._serialized_start=549
  _globals["_MIGRATIONPAYLOAD_DIGITCOUNT"]._serialized_end=621
  _globals["_MIGRATIONPAYLOAD_OTPTYPE"]._serialized_start=623
  _globals["_MIGRATIONPAYLOAD_OTPTYPE"]._serialized_end=678
# @@protoc_insertion_point(module_scope)
