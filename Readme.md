uroboroSQL Formatter
====================

UroboroSQL Formatter is often used in enterprise systems, For formatting to a highly maintainable style even for very long SQL (1 K step or more) It is a plug-in of Sublime Text 3.

In particular, in countries where English is not their mother tongue, such as Japan, comments may be included in SELECT clauses. In that case, we will align the vertical position of the AS clause and the comment, pursuing the viewability which can be said as artistic anymore, This was developed to realize this automatically.

for Japanese, [Readme.ja.md](Readme.ja.md)

#### In case of general formatter

```sql
SELECT MI.MAKER_CD AS ITEM_MAKER_CD -- maker code
,
       MI.BRAND_CD AS ITEM_BRAND_CD -- brand code
,
       MI.ITEM_CD AS ITEM_CD -- item code
,
       MI.CATEGORY AS ITEM_CATEGORY -- item category
FROM M_ITEM MI -- item master

WHERE 1 = 1
  AND MI.ARRIVAL_DATE = '2016-12-01' -- arrival date
```

#### In case of uroboroSQL Formatter

```sql
SELECT
    MI.MAKER_CD AS  ITEM_MAKER_CD   -- maker code
,   MI.BRAND_CD AS  ITEM_BRAND_CD   -- brand code
,   MI.ITEM_CD  AS  ITEM_CD         -- item code
,   MI.CATEGORY AS  ITEM_CATEGORY   -- item category
FROM
    M_ITEM  MI  -- item master
WHERE
    1               =   1
AND MI.ARRIVAL_DATE =   '2016-12-01'    -- arrival date

```

Features
--------

-	Formatting by aligning the vertical position of AS and operator in SELECT clause, WHERE clause
-	Even if there is a comment at the end of each line, the format

How to Use
----------

-	Select "SQL Format" from the Edit menu
-	Select "SQL Format" from the context menu on the editor
-	Select "uroboroSQL Formatter: Format SQL" from the command Palette
-	ctrl + cmd + f on OS X, or ctrl + alt + f on Windows

Settings
--------

```json
{
    "uf_tab_size": 4,
    "uf_translate_tabs_to_spaces": true,
    "uf_case": "lower", // "upper" or "lower" or "capitalize"
    "uf_reserved_case": "upper", // "upper" or "lower" or "capitalize"
    "uf_reserved_words":"SELECT, FROM, WHERE, CREATE",
    "uf_comment_syntax": "uroboroSQL", // "uroboroSQL" or "doma2"
    "uf_escapesequence_u005c": false,
    "uf_save_on_format": true,
    "uf_save_on_format_extensions": [".sql"]
}
```

-	uf_tab_size
	-	Specify the tab size of the indent after formatting. We recommend 4.
-	uf_translate_tabs_to_spaces
	-	Specify whether the indent after formatting is tab or space. It becomes a space by setting it to true.
- uf_case
  - If you want to convert all words to a specific case, set "upper", "lower" or "capitalize".
- uf_reserved_case
  - If you want to convert reserved words to a specific case, set "upper", "lower" or "capitalize".
- uf_reserved_words
  - If you want to convert only reserved words to uppercase, please input reserved words sepalated by a comma. (The input is not case sensitive. So you can input reserved words in both uppercase and lowercase.)   
  If you do not use this option, plase input "noinput" in this option.
- uf_comment_syntax
  - It specifies the comment syntax format.
  - You can specify the "uroboroSQL" or "doma2".
    - In the case of normal SQL, you can specify either.
- uf_escapesequence_u005c
  - If you have specified the escape sequence with a backslash in the SQL to specify the true.
- uf_save_on_format
  - Specify true when formatting automatically when saving files.
- uf_save_on_format_extensions
  - Specify the extension of the file to be formatted in a list.

License
-------

[python-sqlparse library](https://github.com/andialbrecht/sqlparse) and this code are both on [2-clauses BSD](http://www.opensource.org/licenses/bsd-license.php)

---

Copyright 2017 by Future Architect.
