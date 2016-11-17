# -*- coding: utf-8 -*-
import os
import sys
import sublime
import sublime_plugin
import threading
sys.path.append(os.path.dirname(__file__))
import sqlformatter
from sqlformatter.config import LocalConfig


class UroborosqlFormatCommand(sublime_plugin.TextCommand):
    """SQL Format Command class"""

    def run(self, edit):
        view = self.view
        regions = view.sel()
        settings = view.settings()
        user_settings = sublime.load_settings(
            'sublime-uroborosql-formatter.sublime-settings')
        # set syntax
        if settings.get('syntax') == \
                "Packages/Text/Plain text.tmLanguage":
            view.set_syntax_file("Packages/SQL/SQL.tmLanguage")
        # setting
        settings.set("tab_size", user_settings.get("uf_tab_size"))
        settings.set("translate_tabs_to_spaces",
                     user_settings.get("uf_translate_tabs_to_spaces"))

        # format selection
        if len(regions) > 1 or not regions[0].empty():
            for region in view.sel():
                if not region.empty():
                    raw_text = view.substr(region)
                    formatted_text = self.format(raw_text)
                    view.replace(edit, region, formatted_text)
        else:  # format all
            allregion = sublime.Region(0, view.size())
            raw_text = view.substr(allregion)
            formatted_text = self.format(raw_text)
            view.replace(edit, allregion, formatted_text)

    def format(self, raw_text):
        return sqlformatter.format_sql(raw_text, LocalConfig())
