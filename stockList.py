class StockSectors():
    def get_sector_list():
        Sec_list = ['Auto', 'Banking', 'Finance', 'FMCG', 'IT']
        return Sec_list

    def get_sector_stocks(sector):
        if sector == 'Auto':
            return ['AMARAJABAT', 'BAJAJ-AUTO', 'BALKRISIND', 'BHARATFORG', 'BOSCHLTD', 'ASHOKLEY', 'EICHERMOT', 'EXIDEIND', 'HEROMOTOCO', 'MRF', 'M&M', 'MARUTI', 'TVSMOTOR', 'TATAMOTORS', 'TIINDIA']
        elif sector == 'Banking':
            return ['AXISBANK', 'BANKBARODA', 'BANKINDIA', 'BHARATBANK', 'CANBK', 'CENTURYBANK', 'DHFL', 'IDFC', 'IDBI', 'IFCI', 'INDIANB', 'INDRAPRAS', 'IOB', 'KOTAKBANK', 'LICHSGFIN', 'PNB', 'PUNJLLOYD', 'SBIN', 'SOUTHBANK', 'SYNDIBANK', 'YESBANK', 'ZEEL']
        elif sector == 'Finance':
            return ['ADANIENT', 'ADANIPORTS', 'ADANIPOWER', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'ARVIND', 'ASHOKLEY', 'ASIANPAINT', 'AUROPHARMA', 'AXISBANK', 'BAJAJ-AUTO']
        elif sector == 'FMCG':
            return ['BRITANNIA', 'COLPAL', 'DABUR', 'EMAMILTD', 'GODREJCP', 'HINDUNILVR', 'ITC', 'MARICO', 'NESTLEIND', 'PGHH', 'RADICO', 'TATACONSUM', 'UBL', 'MCDOWELL-N', 'VBL'
                    ]
        elif sector == 'IT':
            return ['COFORGE', 'HCLTECH', 'INFY', 'LTTS', 'LTI', 'MINDTREE', 'MPHASIS', 'TCS', 'TECHM', 'WIPRO'
                    ]

    # Banking=['AUBANK'
    # ,'AXISBANK'
    # ,'BANDHANBNK'
    # ,'FEDERALBNK'
    # ,'HDFCBANK'
    # ,'ICICIBANK'
    # ,'IDFCFIRSTB'
    # ,'INDUSINDBK'
    # ,'KOTAKBANK'
    # ,'PNB'
    # ,'RBLBANK'
    # ,'SBIN'
    # ]

    # Finance=['AXISBANK'
    # ,'BAJFINANCE'
    # ,'BAJAJFINSV'
    # ,'CHOLAFIN'
    # ,'HDFCAMC'
    # ,'HDFCBANK'
    # ,'HDFCLIFE'
    # ,'HDFC'
    # ,'ICICIBANK'
    # ,'ICICIGI'
    # ,'ICICIPRULI'
    # ,'KOTAKBANK'
    # ,'M&MFIN'
    # ,'MUTHOOTFIN'
    # ,'PEL'
    # ,'PFC'
    # ,'RECLTD'
    # ,'SBIN'
    # ,'SBILIFE'
    # ,'SRTRANSFIN'
    # ]

    # FMCG=['BRITANNIA'
    # ,'COLPAL'
    # ,'DABUR'
    # ,'EMAMILTD'
    # ,'GODREJCP'
    # ,'HINDUNILVR'
    # ,'ITC'
    # ,'MARICO'
    # ,'NESTLEIND'
    # ,'PGHH'
    # ,'RADICO'
    # ,'TATACONSUM'
    # ,'UBL'
    # ,'MCDOWELL-N'
    # ,'VBL'
    # ]

    # it_sector=['COFORGE'
    # ,'HCLTECH'
    # ,'INFY'
    # ,'LTTS'
    # ,'LTI'
    # ,'MINDTREE'
    # ,'MPHASIS'
    # ,'TCS'
    # ,'TECHM'
    # ,'WIPRO'
    # ]
    # return Sec_list
