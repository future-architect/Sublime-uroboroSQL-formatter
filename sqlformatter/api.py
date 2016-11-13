# coding:utf-8
'''
SQL Formatter API.
@author: ota
'''

import os
import traceback
import codecs
import sys
import sqlformatter
from sqlformatter.exceptions import SqlFormatterException

# pylint: disable=bare-except
def format_dir(indir, outdir, local_config):
    """
        [indir]フォルダ内のSQLファイルをフォーマットして指定フォルダ[outdir]に出力する
    """
    if indir.endswith("/") or indir.endswith("\\"):
        indir = indir[:-1]
    if outdir.endswith("/") or outdir.endswith("\\"):
        outdir = outdir[:-1]

    for file_name, full_path in fild_all_sql_files(indir):
        try:
            sql = __read_file(full_path)
        except:
            print(full_path)
            print(traceback.format_exc())
            continue
        error = False
        try:
            out_sql = sqlformatter.format_sql(sql, local_config)
        except SqlFormatterException as ex:
            exs = __decode(str(ex))
            trace = __decode(traceback.format_exc())
            out_sql = sql + "\n/*"  + exs + "\n" + trace + "\n*/"
            error = True
        except:
            trace = __decode(traceback.format_exc())
            out_sql = sql + "\n/*" + trace + "\n*/"
            error = True

        if not error:
            out_path = os.path.join(outdir, file_name)
        else:
            out_path = os.path.join(outdir, "formaterror_" + file_name)
        out_dir = os.path.dirname(out_path)
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        __write_file(out_path, out_sql)

def fild_all_sql_files(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if os.path.splitext(file_name)[1].lower() == ".sql":
                path = os.path.join(root, file_name)
                yield path[len(directory) + 1:], path


def __read_file(path):
    target_file = codecs.open(path, "r", "utf-8")
    ret = target_file.read()
    target_file.close()
    return ret

def __write_file(path, value):
    target_file = codecs.open(path,"w", "utf-8")
    target_file.write(value)
    target_file.close()


def __decode(text):
    text = str(text)
    if sys.version_info[0] < 3:
        return text.decode("utf-8")
    else:
        return text
