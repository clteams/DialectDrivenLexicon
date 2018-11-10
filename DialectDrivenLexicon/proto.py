#!/usr/bin/python3


class DialectDrivenLexicon:
    def __init__(self, entries=None):
        self.entries = entries


class LexiconEntry:
    def __init__(self, title_groups, transl_groups, context_groups, metadata_groups, source_data):
        self.title_groups = title_groups
        self.transl_groups = transl_groups
        self.context_groups = context_groups
        self.metadata_groups = metadata_groups
        self.source_data = source_data


class TitleVarieties:
    def __init__(self, *varieties):
        self.varieties = varieties


class ScriptForm:
    def __init__(self, script_id, dialect_id, direct_script):
        self.script_id = script_id
        self.dialect_id = dialect_id
        self.direct_script = direct_script


class TitleForm(ScriptForm):
    def __init__(self, title_string, dialect_id, script_id):
        ScriptForm.__init__(self, script_id, dialect_id, title_string)


class TranslatedEntity:
    def __init__(self, x_language, direct_script, script_id, semantic_cats, metadata_rel):
        self.x_language = x_language
        self.direct_script = direct_script
        self.script_id = script_id
        self.semantic_cats = semantic_cats
        self.metadata_rel = metadata_rel


class MetadataObject:
    def __init__(self, direct_key, direct_value, common_key, common_value):
        self.direct_key = direct_key
        self.direct_value = direct_value
        self.common_key = common_key
        self.common_value = common_value


class ContextFrame:
    def __init__(self, context_string, metadata_rel, context_translations):
        self.context_string = context_string
        self.metadata_rel = metadata_rel
        self.context_translations = context_translations


class ContextString(ScriptForm):
    def __init__(self, _string, root_points, script_id, dialect_id):
        ScriptForm.__init__(self, script_id, dialect_id, _string)
        self.root_points = root_points


class SemanticCategory:
    def __init__(self, cat_name):
        self.cat_name = cat_name


class Script:
    def __init__(self, script_id, script_chars):
        self.script_id = script_id
        self.script_chars = script_chars


class ScriptChar:
    def __init__(self, direct_sequence, transliterated_sequences):
        self.direct_sequence = direct_sequence
        self.transliterated_sequences = transliterated_sequences
