# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: xds/type/matcher/v3/matcher.proto
# Protobuf Python Version: 5.29.1
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
    1,
    '',
    'xds/type/matcher/v3/matcher.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from xds.core.v3 import extension_pb2 as xds_dot_core_dot_v3_dot_extension__pb2
from xds.type.matcher.v3 import string_pb2 as xds_dot_type_dot_matcher_dot_v3_dot_string__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!xds/type/matcher/v3/matcher.proto\x12\x13xds.type.matcher.v3\x1a\x1bxds/core/v3/extension.proto\x1a xds/type/matcher/v3/string.proto\x1a\x17validate/validate.proto\"\x96\x0e\n\x07Matcher\x12@\n\x0cmatcher_list\x18\x01 \x01(\x0b\x32(.xds.type.matcher.v3.Matcher.MatcherListH\x00\x12@\n\x0cmatcher_tree\x18\x02 \x01(\x0b\x32(.xds.type.matcher.v3.Matcher.MatcherTreeH\x00\x12\x39\n\x0bon_no_match\x18\x03 \x01(\x0b\x32$.xds.type.matcher.v3.Matcher.OnMatch\x1a\x97\x01\n\x07OnMatch\x12/\n\x07matcher\x18\x01 \x01(\x0b\x32\x1c.xds.type.matcher.v3.MatcherH\x00\x12\x33\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32!.xds.core.v3.TypedExtensionConfigH\x00\x12\x15\n\rkeep_matching\x18\x03 \x01(\x08\x42\x0f\n\x08on_match\x12\x03\xf8\x42\x01\x1a\xb9\x07\n\x0bMatcherList\x12Q\n\x08matchers\x18\x01 \x03(\x0b\x32\x35.xds.type.matcher.v3.Matcher.MatcherList.FieldMatcherB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x1a\xb2\x05\n\tPredicate\x12^\n\x10single_predicate\x18\x01 \x01(\x0b\x32\x42.xds.type.matcher.v3.Matcher.MatcherList.Predicate.SinglePredicateH\x00\x12V\n\nor_matcher\x18\x02 \x01(\x0b\x32@.xds.type.matcher.v3.Matcher.MatcherList.Predicate.PredicateListH\x00\x12W\n\x0b\x61nd_matcher\x18\x03 \x01(\x0b\x32@.xds.type.matcher.v3.Matcher.MatcherList.Predicate.PredicateListH\x00\x12I\n\x0bnot_matcher\x18\x04 \x01(\x0b\x32\x32.xds.type.matcher.v3.Matcher.MatcherList.PredicateH\x00\x1a\xd3\x01\n\x0fSinglePredicate\x12:\n\x05input\x18\x01 \x01(\x0b\x32!.xds.core.v3.TypedExtensionConfigB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12\x39\n\x0bvalue_match\x18\x02 \x01(\x0b\x32\".xds.type.matcher.v3.StringMatcherH\x00\x12\x39\n\x0c\x63ustom_match\x18\x03 \x01(\x0b\x32!.xds.core.v3.TypedExtensionConfigH\x00\x42\x0e\n\x07matcher\x12\x03\xf8\x42\x01\x1a`\n\rPredicateList\x12O\n\tpredicate\x18\x01 \x03(\x0b\x32\x32.xds.type.matcher.v3.Matcher.MatcherList.PredicateB\x08\xfa\x42\x05\x92\x01\x02\x08\x02\x42\x11\n\nmatch_type\x12\x03\xf8\x42\x01\x1a\xa1\x01\n\x0c\x46ieldMatcher\x12O\n\tpredicate\x18\x01 \x01(\x0b\x32\x32.xds.type.matcher.v3.Matcher.MatcherList.PredicateB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12@\n\x08on_match\x18\x02 \x01(\x0b\x32$.xds.type.matcher.v3.Matcher.OnMatchB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x1a\xe5\x03\n\x0bMatcherTree\x12:\n\x05input\x18\x01 \x01(\x0b\x32!.xds.core.v3.TypedExtensionConfigB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01\x12L\n\x0f\x65xact_match_map\x18\x02 \x01(\x0b\x32\x31.xds.type.matcher.v3.Matcher.MatcherTree.MatchMapH\x00\x12M\n\x10prefix_match_map\x18\x03 \x01(\x0b\x32\x31.xds.type.matcher.v3.Matcher.MatcherTree.MatchMapH\x00\x12\x39\n\x0c\x63ustom_match\x18\x04 \x01(\x0b\x32!.xds.core.v3.TypedExtensionConfigH\x00\x1a\xaf\x01\n\x08MatchMap\x12Q\n\x03map\x18\x01 \x03(\x0b\x32:.xds.type.matcher.v3.Matcher.MatcherTree.MatchMap.MapEntryB\x08\xfa\x42\x05\x9a\x01\x02\x08\x01\x1aP\n\x08MapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.xds.type.matcher.v3.Matcher.OnMatch:\x02\x38\x01\x42\x10\n\ttree_type\x12\x03\xf8\x42\x01\x42\x0e\n\x0cmatcher_typeB\\\n\x1e\x63om.github.xds.type.matcher.v3B\x0cMatcherProtoP\x01Z*github.com/cncf/xds/go/xds/type/matcher/v3b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'xds.type.matcher.v3.matcher_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.github.xds.type.matcher.v3B\014MatcherProtoP\001Z*github.com/cncf/xds/go/xds/type/matcher/v3'
  _globals['_MATCHER_ONMATCH'].oneofs_by_name['on_match']._loaded_options = None
  _globals['_MATCHER_ONMATCH'].oneofs_by_name['on_match']._serialized_options = b'\370B\001'
  _globals['_MATCHER_MATCHERLIST_PREDICATE_SINGLEPREDICATE'].oneofs_by_name['matcher']._loaded_options = None
  _globals['_MATCHER_MATCHERLIST_PREDICATE_SINGLEPREDICATE'].oneofs_by_name['matcher']._serialized_options = b'\370B\001'
  _globals['_MATCHER_MATCHERLIST_PREDICATE_SINGLEPREDICATE'].fields_by_name['input']._loaded_options = None
  _globals['_MATCHER_MATCHERLIST_PREDICATE_SINGLEPREDICATE'].fields_by_name['input']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_MATCHER_MATCHERLIST_PREDICATE_PREDICATELIST'].fields_by_name['predicate']._loaded_options = None
  _globals['_MATCHER_MATCHERLIST_PREDICATE_PREDICATELIST'].fields_by_name['predicate']._serialized_options = b'\372B\005\222\001\002\010\002'
  _globals['_MATCHER_MATCHERLIST_PREDICATE'].oneofs_by_name['match_type']._loaded_options = None
  _globals['_MATCHER_MATCHERLIST_PREDICATE'].oneofs_by_name['match_type']._serialized_options = b'\370B\001'
  _globals['_MATCHER_MATCHERLIST_FIELDMATCHER'].fields_by_name['predicate']._loaded_options = None
  _globals['_MATCHER_MATCHERLIST_FIELDMATCHER'].fields_by_name['predicate']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_MATCHER_MATCHERLIST_FIELDMATCHER'].fields_by_name['on_match']._loaded_options = None
  _globals['_MATCHER_MATCHERLIST_FIELDMATCHER'].fields_by_name['on_match']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_MATCHER_MATCHERLIST'].fields_by_name['matchers']._loaded_options = None
  _globals['_MATCHER_MATCHERLIST'].fields_by_name['matchers']._serialized_options = b'\372B\005\222\001\002\010\001'
  _globals['_MATCHER_MATCHERTREE_MATCHMAP_MAPENTRY']._loaded_options = None
  _globals['_MATCHER_MATCHERTREE_MATCHMAP_MAPENTRY']._serialized_options = b'8\001'
  _globals['_MATCHER_MATCHERTREE_MATCHMAP'].fields_by_name['map']._loaded_options = None
  _globals['_MATCHER_MATCHERTREE_MATCHMAP'].fields_by_name['map']._serialized_options = b'\372B\005\232\001\002\010\001'
  _globals['_MATCHER_MATCHERTREE'].oneofs_by_name['tree_type']._loaded_options = None
  _globals['_MATCHER_MATCHERTREE'].oneofs_by_name['tree_type']._serialized_options = b'\370B\001'
  _globals['_MATCHER_MATCHERTREE'].fields_by_name['input']._loaded_options = None
  _globals['_MATCHER_MATCHERTREE'].fields_by_name['input']._serialized_options = b'\372B\005\212\001\002\020\001'
  _globals['_MATCHER']._serialized_start=147
  _globals['_MATCHER']._serialized_end=1961
  _globals['_MATCHER_ONMATCH']._serialized_start=350
  _globals['_MATCHER_ONMATCH']._serialized_end=501
  _globals['_MATCHER_MATCHERLIST']._serialized_start=504
  _globals['_MATCHER_MATCHERLIST']._serialized_end=1457
  _globals['_MATCHER_MATCHERLIST_PREDICATE']._serialized_start=603
  _globals['_MATCHER_MATCHERLIST_PREDICATE']._serialized_end=1293
  _globals['_MATCHER_MATCHERLIST_PREDICATE_SINGLEPREDICATE']._serialized_start=965
  _globals['_MATCHER_MATCHERLIST_PREDICATE_SINGLEPREDICATE']._serialized_end=1176
  _globals['_MATCHER_MATCHERLIST_PREDICATE_PREDICATELIST']._serialized_start=1178
  _globals['_MATCHER_MATCHERLIST_PREDICATE_PREDICATELIST']._serialized_end=1274
  _globals['_MATCHER_MATCHERLIST_FIELDMATCHER']._serialized_start=1296
  _globals['_MATCHER_MATCHERLIST_FIELDMATCHER']._serialized_end=1457
  _globals['_MATCHER_MATCHERTREE']._serialized_start=1460
  _globals['_MATCHER_MATCHERTREE']._serialized_end=1945
  _globals['_MATCHER_MATCHERTREE_MATCHMAP']._serialized_start=1752
  _globals['_MATCHER_MATCHERTREE_MATCHMAP']._serialized_end=1927
  _globals['_MATCHER_MATCHERTREE_MATCHMAP_MAPENTRY']._serialized_start=1847
  _globals['_MATCHER_MATCHERTREE_MATCHMAP_MAPENTRY']._serialized_end=1927
# @@protoc_insertion_point(module_scope)
