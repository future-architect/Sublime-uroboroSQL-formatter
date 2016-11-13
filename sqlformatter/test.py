# coding:utf-8
'''
Created on 2016/06/24

@author: ota
'''
import sqlformatter
from sqlformatter import config
from sqlformatter.config import LocalConfig
from sqlformatter.commentsyntax import Doma2CommentSyntax

def parse():
    config.glb.escape_sequence_u005c = True
    format_test(u"""
SELECT    /* _SQL_IDENTIFIER_ */
    TKR.KAISHA_CD                        AS    KAISHA_CD                        --    会社コード
,    TKR.KAISHA_NM                        AS    KAISHA_NM                        --    会社名称
,    TKR.AREA_CD                            AS    AREA_CD                            --    エリアコード
,    TKR.AREA_NM                            AS    AREA_NM                            --    エリア名称
,    TKR.HAMBAIJO_CD                        AS    HAMBAIJO_CD                        --    販売所コード
,    TKR.HAMBAIJO_NM                        AS    HAMBAIJO_NM                        --    販売所名称
,    TKR.TANTOUSHA_CD                    AS    TANTOUSHA_CD                    --    担当者コード
,    TKR.TANTOUSHA_NM                    AS    TANTOUSHA_NM                    --    担当者名称
,    TKR.MOKUHYOU_ARARI_RITSU            AS    HAMBAIJO_MOKUHYOU_ARARI            --    目標粗利率
,    TKR.KOUJI_NO                        AS    KOUJI_NO                        --    工事コード
,    TKR.SEKISAN_KOUJI_KBN                AS    KOUJI_KBN                        --    積算工事区分
,    TKR.KEIYAKU_CD                        AS    KEIYAKU_CD                        --    契約コード
,    TKR.KEIYAKU_CD_EDABAN                AS    KEIYAKU_CD_EDABAN                --    契約コード枝番
,    TKR.GAS_KOUJI_KBN                    AS    GAS_KOUJI_KBN                    --    ガス工事区分
,    TKR.GENKEIYAKU_BI                    AS    KEIYAKU_BI                        --    原契約日
,    TKR.SEKISAN_KOUJI_NM                AS    KOUJI_NM                        --    積算工事名称
,    MJS.TODOUFUKEN_NM                    AS    TODOUFUKEN_NM                    --    都道府県名
,    MJS.SHIKUGUN_NM                        AS    SHIKUGUN_NM                        --    市区郡名
,    MJS.CHOUSONAZA_NM                    AS    CHOUSONAZA_NM                    --    町村字名
,    TKR.GEMBA_TSUIKA_JUSHO                AS    HOJO_JUSHO                        --    現場追加住所
,    COALESCE(
                MKK.GAIKOU_CHAKKOU_BI
            ,    MKK.GAIKOU_CHAKKOU_YOTEI_BI
            )                            AS    GAIKOU_CHAKKOU_BI                --    外構着工日
,    COALESCE(
                MKK.HONTAI_CHAKKOU_BI
            ,    MKK.HONTAI_CHAKKOU_YOTEI_BI
            )                            AS    HONTAI_CHAKKOU_BI                --    本体着工日
,    COALESCE(
                MKK.SHANAI_KENSA_BI
            ,    MKK.SHANAI_KENSA_YOTEI_BI
            )                            AS    KANSEI_YMD                        --    社内検査日
,    TKR.GASPAL_KOUKI_FROM                AS    GASPAL_KOUKI_FROM                --    ガスパル工期(FROM)
,    TKR.GASPAL_KOUKI_TO                    AS    GASPAL_KOUKI_TO                    --    ガスパル工期(TO)
,    MKN.KBN_NM    ||
            ' '    ||
    TKR.MOTOUKE_JIGYOUSHO_NM            AS    HATCHUMOTO_GYOUSHA                --    発注元業者
,    TKR.MOTOUKE_TANTOUSHA                AS    HATCHUMOTO_TANTOUSHA            --    発注元担当者
,    TKR.OKUCHI_KOUJI_FLG                AS    KOUJI_KIBO_KBN                    --    工事規模区分
,    TKR.KOUJI_TAISHOU_KBN                AS    KOUJI_TAISHOU                    --    工事対象
,    TKR.KICHI_SU                        AS    KICHISU                            --    基地数
,    TKR.MUNESU                            AS    MUNESU                            --    棟数
,    TKR.KOSU                            AS    KOSU                            --    戸数
,    TKR.IPPAN_SHINSEI_NO                AS    IPPAN_SHINSEI_NO                --    一般申請No.
,    TKR.KANKOU_SHOUNIN_SHA_NM            AS    KANKOU_SHOUNIN                    --    完工承認
,    TKR.KANKOU_SHOUNIN_BI                AS    KANKOU_SHOUNIN_BI                --    完工承認日
,    TKR.TANTOUSHA_NM                    AS    KANKOU_SHINSEI                    --    完工申請
,    TKR.KANKOU_SHINSEI_BI                AS    KANKOU_SHINSEI_BI                --    完工申請日
,    TKR.JKYSN_ARARI_KINGAKU                AS    JKYSN_ARARI_KINGAKU                    --    実行予算粗利金額
,    TKR.JKYSN_ARARI_KINGAKU_NCU_FUKUMU    AS    JKYSN_ARARI_KINGAKU_NCU_FUKUMU        --    実行予算粗利金額（NCU含む）
,    TKR.JKYSN_ARARI_RITSU                AS    JKYSN_ARARI_RITSU                    --    実行予算粗利率
,    TKR.JKYSN_ARARI_RITSU_NCU_FUKUMU    AS    JKYSN_ARARI_RITSU_NCU_FUKUMU        --    実行予算粗利率（NCU含む）
,    TKR.JKYSN_GENKA                        AS    JISSEKI_KOUJI_GENKA                    --    実績工事原価
,    TKR.JKYSN_GENKA_NCU_FUKUMU            AS    JISSEKI_KOUJI_GENKA_NCU_FUKUMU        --    実績工事原価（NCU含む）
,    TKR.LOCK_NO                            AS    TKSK_LOCK_NO                        --    ロックNo
FROM
    T_KJ_SKSN_KNR    TKR                                                            --    工事積算管理トラン
,    M_KYK            MKK                                                            --    契約マスタ
,    M_JS            MJS                                                            --    住所マスタ
,    M_KBN            MKN                                                            --    区分マスタ
WHERE    1=1
AND        TKR.KOUJI_NO            =    /*koujiNo*/'00000000001'
AND        TKR.SAKUJO_FLG            =    /*#CLS_COMMON_VALUE_FLAG_OFF*/'0'
AND        TKR.KEIYAKU_CD            =    MKK.KEIYAKU_CD
AND        MKK.TSUIKA_CD            =    /*#CLS_GPR_KEIYAKU_TSUIKA_CD_HONTAI_KOUJI_KEIYAKU*/001
AND        MKK.SAKUJO_FLG            =    /*#CLS_COMMON_VALUE_FLAG_OFF*/'0'
AND        TKR.GEMBA_JUSHO_CD        =    MJS.JUSHO_CD(+)
AND        MJS.SAKUJO_KBN(+)        =    /*#CLS_COMMON_VALUE_FLAG_OFF*/'0'
AND        TKR.MOTOUKE_GYOUSHA_KBN    =    MKN.KBN_CD(+)
AND        MKN.KBN_TYPE_CD(+)        =    /*#CLS_MOTOUKE_GYOUSHA_KBN*/'0239'
""")


def format_test(sql):
    print("\n--------------------------------------------------\n")
    print (sqlformatter.format_sql(sql, LocalConfig().set_commentsyntax(Doma2CommentSyntax())))

if __name__ == '__main__':
    parse()
