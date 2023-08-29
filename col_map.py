""" buy/sell trigger configuration for ticker """

COL_SCRIPT = 'Script'
COL_SECTOR = 'Sector'
COL_BETA = 'Beta'
COL_BUY = 'Buy Value'
COL_MARGIN = 'Buy Margin'
COL_SEC_PE = 'Sector P/E'
COL_SYM_PE = 'Symbol P/E'
COL_PRICE = 'Current Price'
COL_BULKDEALS = 'Bulk Deals'
COL_BUY_CNGE_PERCENT = 'Buy Percentage Change'
COL_SELL_CNGE_PERCENT = 'Sell Percentage Change'
COL_CNGE_PERCENT = 'Percentage Change'
COL_VWAP = 'VWAP'
COL_EPS = 'EPS'
COL_PNL = 'NET PROFIT/LOSS'
COL_VOL_TRADED = 'Total Volume Traded'
COL_VAL_TRADED = 'Total Value Traded'
COL_DEL_RATIO = 'Delivery to Traded Ratio'
COL_ACT_RANK = 'Most active rank'
COL_BOOK_VAL = 'Book Value'
COL_DIV_YIELD = 'Dividend Yield'
COL_52W_H = '52W High'
COL_BUY_52W_H = 'Buy 52W High'
COL_SELL_52W_H = 'Sell 52W High'
COL_52W_L = '52W Low'
COL_RECOMMEND_B_S = 'Buy/Sell/None'
COL_RECOMMEND_NOTES = 'Notes'
COL_RANK = 'Rank'


def parse_dict(*args, data=None, default=None):
    """Function parse data dict in the order of the args."""
    if not data:
        raise ValueError('Data is Empty')
    res = None
    for i in args:
        res = data.get(i, None)
        if not res:
            return default if default != None else res
        # if the res is list of dicts take latest dict
        data = res[0] if isinstance(res, (list, tuple)) else res
    return res


def need_recommendataion(index, portifolio):
    return portifolio.get(index, {}).get(COL_RANK, 8) < 8


def buy_recommendation(df, portifolio):

    res = df[5 <= df[COL_SYM_PE]]
    res = res[res[COL_SYM_PE] <= 25]
    return res
    # for index, row in df.iterrows():
    #     if not need_recommendataion(index, portifolio):
    #         continue # skip the stock from recommendataion
    #     notes = []
    #     if row[COL_PRICE] <= parse_dict(index, COL_BUY, data=portifolio):
    #         notes.append('our buy target')
    #     if isinstance(row[COL_SEC_PE], (int, float)) and isinstance(row[COL_SYM_PE], (int, float)) and row[COL_SYM_PE] <= parse_dict(index, COL_SYM_PE, data=portifolio, default=5) and row[COL_SYM_PE] <= row[COL_SEC_PE]:
    #         notes.append('Sym P/E')
    #     if row[COL_DIV_YIELD] >= parse_dict(index, COL_DIV_YIELD, data=portifolio, default=10):
    #         notes.append('Dividend yield')
    #     if row[COL_CNGE_PERCENT] <= parse_dict(index, COL_BUY_CNGE_PERCENT, data=portifolio, default=-8):
    #         notes.append('Change in a day')
    #     if row[COL_BULKDEALS][1] == 'BUY':
    #         notes.append('Bulk deals')

    #     if notes:
    #         df.at[index, COL_RECOMMEND_B_S] = 'Buy'
    #         df.at[index, COL_RECOMMEND_NOTES] = ','.join(notes)

    # # limit dataframe for only buy and sort
    # return df[df[COL_RECOMMEND_B_S] == 'Buy'].sort_index()


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

