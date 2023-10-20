""" buy/sell trigger configuration for ticker """

COL_52W_H = '52W High'
COL_52W_L = '52W Low'
COL_ACT_RANK = 'Most active rank'
COL_AVG_PRICE = 'AVG Price'
COL_BETA = 'Beta'
COL_BOOK_VAL = 'Book Value'
COL_BULKDEALS = 'Bulk Deals'
COL_BUY = 'Buy Value'
COL_BUY_52W_H = 'Buy 52W High'
COL_BUY_CNGE_PERCENT = 'Buy % Change'
COL_MARGIN = 'Buy Margin'
COL_CNGE_PERCENT = '%'
COL_CP_BP_RATIO = 'Price / Book'
COL_DEL_RATIO = 'Del Ratio'
COL_DIV_YIELD = 'Div Yield'
COL_EPS = 'EPS'
COL_MRKT_CAP = 'Mkt Cap'
COL_PNL = 'PNL'
COL_PRICE = 'Price'
COL_PROFIT_GROWTH_PERCENT_3Y = 'Profit Growth % (3Y)'
COL_PROFIT_GROWTH_PERCENT_TTM = 'Profit Growth % (TTM)'
COL_PROMT_PERCENT = 'Prom hold %'
COL_RANK = 'Rank'
COL_RECOMMEND_B_S = 'Buy/Sell/None'
COL_RECOMMEND_NOTES = 'Notes'
COL_ROCE = 'ROCE'
COL_ROE = 'ROE'
COL_SCRIPT = 'Script'
COL_SEC_PE = 'Sct P/E'
COL_SEC_PE_MAX = 'Sector P/E Max'
COL_SEC_PE_MIN = 'Sector P/E Min'
COL_SECTOR = 'Sector'
COL_SYM_PE = 'Sym P/E'
COL_SYM_PE_MAX = 'Symbol P/E Max'
COL_SYM_PE_MIN = 'Symbol P/E Min'
COL_SELL_52W_H = 'Sell 52W High'
COL_SELL_CNGE_PERCENT = 'Sell % Change'
COL_UR_PNL = 'U/R PNL'
COL_QTY = 'Qty'
COL_VAL_TRADED = 'Total Value Traded'
COL_VOL_TRADED = 'Total Volume Traded'
COL_VWAP = 'VWAP'


def need_recommendataion(index, portifolio):
    return portifolio.get(index, {}).get(COL_RANK, 8) < 8


def global_config_filters(df, g_config):
    res = df[g_config[COL_SYM_PE_MIN] <= df[COL_SYM_PE]]
    res = res[res[COL_SYM_PE] <= g_config[COL_SYM_PE_MAX]]
    # res = res[g_config[COL_SEC_PE_MIN] <= res[COL_SEC_PE]]
    # res = res[res[COL_SEC_PE] <= g_config[COL_SEC_PE_MAX]]
    res = res[res[COL_ROE] >= g_config[COL_ROE]]
    res = res[res[COL_ROCE] >= g_config[COL_ROCE]]
    res = res[res[COL_DIV_YIELD] >= g_config[COL_DIV_YIELD]]
    res = res[res[COL_MRKT_CAP] >= g_config[COL_MRKT_CAP]]
    # res = res[res[COL_MARGIN] >= g_config[COL_MARGIN]]
    res = res[res[COL_CP_BP_RATIO] <= g_config[COL_CP_BP_RATIO]]
    res = res[res[COL_52W_H] <= g_config[COL_52W_H]]
    res = res[res[COL_52W_L] <= g_config[COL_52W_L]]
    res = res[res[COL_PROMT_PERCENT] >= g_config[COL_PROMT_PERCENT]]

    return res

def buy_recommendation(df, userconfig, g_config):
    res = df
    res = global_config_filters(df, g_config)

    """
    for index, row in res.iterrows():
        if not need_recommendataion(index, portifolio):
            continue # skip the stock from recommendataion
        notes = []
        if row[COL_PRICE] <= parse_dict(index, COL_BUY, data=portifolio):
            notes.append('our buy target')
        if isinstance(row[COL_SEC_PE], (int, float)) and isinstance(row[COL_SYM_PE], (int, float)) and row[COL_SYM_PE] <= parse_dict(index, COL_SYM_PE, data=portifolio, default=5) and row[COL_SYM_PE] <= row[COL_SEC_PE]:
            notes.append('Sym P/E')
        if row[COL_DIV_YIELD] >= parse_dict(index, COL_DIV_YIELD, data=portifolio, default=10):
            notes.append('Dividend yield')
        if row[COL_CNGE_PERCENT] <= parse_dict(index, COL_BUY_CNGE_PERCENT, data=portifolio, default=-8):
            notes.append('Change in a day')
        if row[COL_BULKDEALS][1] == 'BUY':
            notes.append('Bulk deals')

        if notes:
            res.at[index, COL_RECOMMEND_B_S] = 'Buy'
            res.at[index, COL_RECOMMEND_NOTES] = ','.join(notes)
    """

    # limit dataframe for only buy and sort
    # return res[res[COL_RECOMMEND_B_S] == 'Buy'].sort_values(by=[COL_MARGIN], ascending=False)
    return res.sort_values(by=[COL_MRKT_CAP], ascending=False)


def sell_recommendation(df, portifolio):
    res = df[df[COL_PRICE] > df[COL_52W_H]*95/100]
    return res
    # for index, row in df.iterrows():
    #     if not need_recommendataion(index, portifolio):
    #         continue # skip the stock from recommendataion
    #     notes = []
    #     if row[COL_PRICE] >= parse_dict(index, COL_SELL_52W_H, data=portifolio, default=95)*row[COL_52W_H]/100:
    #         notes.append('52 W taget %')
    #     if row[COL_CNGE_PERCENT] >= parse_dict(index, COL_SELL_CNGE_PERCENT, data=portifolio, default=8):
    #         notes.append('Change in a day')

    #     if notes:
    #         df.at[index, COL_RECOMMEND_B_S] = 'Sell'
    #         df.at[index, COL_RECOMMEND_NOTES] = ','.join(notes)
    # # limit dataframe for only sell and sort
    # return df[df[COL_RECOMMEND_B_S] == 'Sell'].sort_index()

