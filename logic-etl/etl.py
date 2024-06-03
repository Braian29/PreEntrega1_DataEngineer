#logic-etl\etl.py
import yfinance as yf
from datetime import datetime
from sqlalchemy.sql import text

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    hist.reset_index(inplace=True)
    return hist

def create_redshift_table(engine):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS stock_data (
        extract_date TIMESTAMP,
        stock_date TIMESTAMP,
        ticker VARCHAR(10),
        opening_price FLOAT,
        high FLOAT,
        low FLOAT,
        close FLOAT,
        volume BIGINT
    );
    """
    with engine.connect() as connection:
        connection.execute(text(create_table_query))

def load_data_to_redshift(df, ticker, engine):
    df['extract_date'] = datetime.now()
    df['ticker'] = ticker
    df.rename(columns={
        'Date': 'stock_date',
        'Open': 'opening_price',
        'High': 'high',
        'Low': 'low',
        'Close': 'close',
        'Volume': 'volume'
    }, inplace=True)

    connection = engine.raw_connection()
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO stock_data (extract_date, stock_date, ticker, opening_price, high, low, close, volume)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = df[['extract_date', 'stock_date', 'ticker', 'opening_price', 'high', 'low', 'close', 'volume']].values.tolist()
    cursor.executemany(insert_query, values)

    connection.commit()
    cursor.close()
    connection.close()
