# coding:utf-8
'''
@author: ota
'''
from uroborosqlfmt.commentsyntax import UroboroSqlCommentSyntax


class _GlobalConfig(object):
    def __init__(self):
        self.escape_sequence_u005c = False  # バックスラッシュによるエスケープシーケンス

    def set_escape_sequence_u005c(self, escape_sequence):
        self.escape_sequence_u005c = escape_sequence
        return self


class LocalConfig(object):

    __slots__ = ('comment_syntax', 'case', 'reserved_case','input_reserved_words')

    def __init__(self):
        self.comment_syntax = UroboroSqlCommentSyntax()
        self.case = None
        self.reserved_case = None
        self.input_reserved_words = None

    def set_commentsyntax(self, comment_syntax):
        self.comment_syntax = comment_syntax
        return self

    def set_case(self, case):
        self.case = case
        return self

    def set_reserved_case(self, reserved_case):
        self.reserved_case = reserved_case
        return self

    def set_input_reserved_words(self, input_reserved_words):
        self.input_reserved_words = input_reserved_words
        return self


# グローバル設定
glb = _GlobalConfig()  # pylint: disable=invalid-name
