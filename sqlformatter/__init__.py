# coding:utf-8
'''
@author: ota
'''

"""SQL Formatter."""



__version__ = '0.0.1'

import sys
import re
import sqlparseforjython as sqlparse
from sqlformatter import filters, config
from sqlparseforjython.lexer import Lexer
from sqlparseforjython import tokens as T, utils

from threading import Thread, Lock

lock = Lock()

def format_sql(sql, localConfig):

    lock.acquire()
    try:
        if not config.glb.escape_sequence_u005c:
            # Oracleの場合リテラルの取り方がにバグがあるので置き換える
            for i, data in enumerate(Lexer.tokens["root"]):
                Single = getattr(T.String, "Single")
                if data[0] == r"'(''|\\\\|\\'|[^'])*'" :
                    if data[1] == Single:
                        Lexer.tokens["root"][i] = (r"'(''|[^'])*'", Single)

                        # 初期化
                        if hasattr(Lexer, "_tokens"):
                            delattr(Lexer, "_tokens")
                        if hasattr(Lexer, "token_variants"):
                            delattr(Lexer, "token_variants")
                        break
            utils.SPLIT_REGEX = re.compile(r"""
            (
             (?:                     # Start of non-capturing group
              (?:\r\n|\r|\n)      |  # Match any single newline, or
              [^\r\n'"]+          |  # Match any character series without quotes or
                                     # newlines, or
              "(?:[^"]|\\.)*"   |  # Match double-quoted strings, or
              '(?:[^']|\\.)*'      # Match single quoted strings
             )
            )
            """, re.VERBOSE)
        else:
            # 元に戻す
            for i, data in enumerate(Lexer.tokens["root"]):
                Single = getattr(T.String, "Single")
                if data[0] == r"'(''|[^'])*'" :
                    if data[1] == Single:
                        Lexer.tokens["root"][i] = (r"'(''|\\\\|\\'|[^'])*'" , Single)

                        # 初期化
                        if hasattr(Lexer, "_tokens"):
                            delattr(Lexer, "_tokens")
                        if hasattr(Lexer, "token_variants"):
                            delattr(Lexer, "token_variants")
                        break
            utils.SPLIT_REGEX = re.compile(r"""
            (
             (?:                     # Start of non-capturing group
              (?:\r\n|\r|\n)      |  # Match any single newline, or
              [^\r\n'"]+          |  # Match any character series without quotes or
                                     # newlines, or
              "(?:[^"\\]|\\.)*"   |  # Match double-quoted strings, or
              '(?:[^'\\]|\\.)*'      # Match single quoted strings
             )
            )
            """, re.VERBOSE)
    finally:
        lock.release()

    stack = sqlparse.engine.FilterStack()
    stack.enable_grouping()


    stack.preprocess.append(sqlparse.filters.KeywordCaseFilter())
    stack.preprocess.append(sqlparse.filters.IdentifierCaseFilter())

    stack.stmtprocess.append(filters.GroupFilter())
    stack.stmtprocess.append(filters.LineDescriptionLineCommentFilter(localConfig))
    stack.stmtprocess.append(filters.MoveCommaFilter(localConfig))
    stack.stmtprocess.append(filters.StripWhitespaceAndToTabFilter())
    stack.stmtprocess.append(filters.AdjustGroupFilter(localConfig))

    stack.stmtprocess.append(filters.OperatorFilter())

    stack.stmtprocess.append(filters.CustomReindentFilter(localConfig))
    stack.postprocess.append(sqlparse.filters.SerializerUnicode())

    if sys.version_info[0] < 3 and isinstance(sql, unicode):
        sql = sql.encode("utf-8")
        s = "\n".join(stack.run(sql))
        return s.decode("utf-8")
    else:
        return "\n".join(stack.run(sql))
