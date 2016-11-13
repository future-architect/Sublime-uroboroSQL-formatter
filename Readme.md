uroboroSQL Formatter
====================

UroboroSQL Formatter is often used in enterprise systems, For formatting to a highly maintainable style even for very long SQL (1 K step or more) It is a plug-in of Sublime Text 3.

In particular, in countries where English is not their mother tongue, such as Japan, comments may be included in SELECT clauses. In that case, we will align the vertical position of the AS clause and the comment, pursuing the viewability which can be said as artistic anymore, This was developed to realize this automatically.

for Japanese, [Readme.ja.md](Readme.ja.md)

#### In case of general formatter

```sql
SELECT MI.MAKER_CD AS ITEM_MAKER_CD -- メーカーコード
,
       MI.BRAND_CD AS ITEM_BRAND_CD -- ブランドコード
,
       MI.ITEM_CD AS ITEM_CD -- 商品コード
,
       MI.CATEGORY AS ITEM_CATEGORY -- 商品カテゴリ
FROM M_ITEM MI -- 商品マスタ

WHERE 1 = 1
  AND MI.ARRIVAL_DATE = '2016-12-01' -- 入荷日
```

#### In case of uroboroSQL Formatter

```sql
SELECT
    MI.MAKER_CD AS  ITEM_MAKER_CD   -- メーカーコード
,   MI.BRAND_CD AS  ITEM_BRAND_CD   -- ブランドコード
,   MI.ITEM_CD  AS  ITEM_CD         -- 商品コード
,   MI.CATEGORY AS  ITEM_CATEGORY   -- 商品カテゴリ
FROM
    M_ITEM  MI  -- 商品マスタ
WHERE
    1               =   1
AND MI.ARRIVAL_DATE =   '2016-12-01'    -- 入荷日

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

Settings
--------

```json
{
    "uf_tab_size": 4,
    "uf_translate_tabs_to_spaces": false
}
```

-	uf_tab_size
	-	Specify the tab size of the indent after formatting. We recommend 4.
-	uf_translate_tabs_to_spaces
	-	Specify whether the indent after formatting is tab or space. It becomes a space by setting it to true.

License
-------

[python-sqlparse library](https://github.com/andialbrecht/sqlparse) and this code are both on [2-clauses BSD](http://www.opensource.org/licenses/bsd-license.php)

---

Copyright 2016 by Future Corporation.
