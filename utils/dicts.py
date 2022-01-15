from datetime import datetime

# Some translation dictionaries
REITS = {
    'Industrial': 'BBREINDW Index',
    'Diversified': 'BBREDIVR Index',
    'Self storage': 'BBREPBST Index',
    'Single tenant': 'BBREOUTL Index',
    'Healthcare': 'BBREHLTH Index',
    'Apartment': 'BBREAPT Index',
    'Office': 'BBREOFPY Index',
    'Shopping': 'BBRESHOP Index',
    'Hotel': 'BBREHOTL Index',
    'Regional Malls': 'BBREMALL Index',
    'All': 'BBREIT Index'
}
US_INDICES = {
    'S&P 500 ER': 'SPXFP Index',
    '10y Treasury ER': 'SPUSTTP Index',
    'TIPS ER': 'SPBDU1ST Index'
}
ETFS = {
    'USA': 'IDUP LN Equity',
    'Europe': 'D5BK B2 Equity',
    'Japan': '1476 JT Equity'
}
BZ_INDICES = {
    'Ibovespa': 'IBOV Index',
    'IFIX': 'IFIX Index',
    'Ibovespa ER': 'IBOV Index (ER)',
    'IFIX ER': 'IFIX Index (ER)',
    '10y Government bond': 'BZAD10Y Index (acc)',
    'CDI': 'BZDIOVRA Index (acc)',
    '10y Government bond ER': 'BZAD10Y Index (ER)'
}

# Start dates for when series starts to show meaningful data
START_DATES = {
    'BBREINDW Index': datetime(1994, 1, 1), 'BBREDIVR Index': datetime(1994, 1, 1), 'BBREPBST Index': datetime(1994, 1, 1),
    'BBREOUTL Index': datetime(1994, 1, 1), 'BBREHLTH Index': datetime(1994, 1, 1), 'BBREAPT Index': datetime(1994, 1, 1),
    'BBREOFPY Index': datetime(1994, 1, 1), 'BBRESHOP Index': datetime(1994, 1, 1), 'BBREHOTL Index': datetime(1994, 1, 1),
    'BBREMALL Index': datetime(1994, 1, 1), 'BBREIT Index': datetime(1994, 1, 1), 'SPXFP Index': datetime(1997, 9, 1),
    'SPUSTTP Index': datetime(1994, 1, 1), 'SPBDU1ST Index': datetime(2002, 1, 1), 'IDUP LN Equity': datetime(2006, 11, 1),
    'D5BK B2 Equity': datetime(2018, 1, 1), '1476 JT Equity': datetime(2015, 10, 1), 'IBOV Index': datetime(1994, 1, 1),
    'IFIX Index': datetime(2011, 1, 1), 'IBOV Index (ER)': datetime(1994, 7, 1), 'IFIX Index (ER)': datetime(2011, 1, 1),
    'BZAD10Y Index (acc)': datetime(2009, 9, 1), 'BZDIOVRA Index (acc)': datetime(1994, 7, 1),
    'BZAD10Y Index (ER)': datetime(2009, 9, 1)
}