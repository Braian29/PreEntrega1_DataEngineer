#logic-etl\main.py
from db import get_engine, query_stock_data
from etl import get_stock_data, create_redshift_table, load_data_to_redshift

def main():
    engine = get_engine()
    create_redshift_table(engine)

    tickers = ['AAPL', 'MSFT', 'GOOGL']
    for ticker in tickers:
        df = get_stock_data(ticker)
        load_data_to_redshift(df, ticker, engine)

    df = query_stock_data(engine)
    print(df)

if __name__ == "__main__":
    main()
