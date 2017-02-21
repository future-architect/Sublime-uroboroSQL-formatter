uroboroSQL Formatter
====================

uroboroSQL Formatterは、エンタープライズシステムで用いられることの多い、  
非常に長いSQL(1K step以上)でも見やすく保守性の高いスタイルへフォーマットするための  
Sublime Text 3のプラグインです。

特に日本など、英語を母国語としない国では、SELECT句などにコメントを入れることがあります。  
その場合、AS句とコメントの縦位置を揃えて、もはや芸術的とも言える見やすさを追求しますが、  
これ自動的に実現するために開発したものです。

#### 一般的なフォーマッタの場合

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

#### uroboroSQL Formatterの場合

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

-	SELECT句、WHERE句内でASや演算子の縦位置を揃えてフォーマット
-	各行の末尾にコメントがあっても正しくフォーマット

How to Use
----------

-	Editメニューから「SQL Format」を選択
-	エディタ上のコンテキストメニューから「SQL Format」を選択
-	コマンドPaletteから「uroboroSQL Formatter: Format SQL」を選択
-	ctrl + cmd + f on OS X, or ctrl + alt + f on Windows

Settings
--------

```json
{
    "uf_tab_size": 4,
    "uf_translate_tabs_to_spaces": true,
    "uf_uppercase": true,
    "uf_comment_syntax": "uroboroSQL", // "uroboroSQL" or "doma2"
    "uf_escapesequence_u005c": false,
}
```

-	uf_tab_size
	-	フォーマット後のインデントのタブサイズを指定します。4つを推奨します。
-	uf_translate_tabs_to_spaces
	-	フォーマット後のインデントをタブにするかスペースにするかを指定します。trueにすることでスペースになります。
- uf_uppercase
  - 予約語と識別子を大文字に変換する場合はtrueを指定します。
- uf_comment_syntax
  - コメントのシンタックス形式を指定します。
  - 「uroboroSQL」または「doma2」の指定が可能です。
    - 通常のSQLの場合は、どちらを指定してもかまいません。
- uf_escapesequence_u005c
  - SQL内でエスケープシーケンスをバックスラッシュで指定している場合にtrueを指定します。

License
-------

[python-sqlparse library](https://github.com/andialbrecht/sqlparse) and this code are both on [2-clauses BSD](http://www.opensource.org/licenses/bsd-license.php)

---

Copyright 2016-2017 by Future Corporation.
