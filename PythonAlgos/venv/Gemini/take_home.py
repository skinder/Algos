from binance.client import Client
import os
import pandas_test as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pyspark.sql import Row
from pyspark.sql import SparkSession

def get_klines_data(symbol: str, interval: str, start_ts: int, end_ts: int, output_location: str):
    '''

    :param symbol: traiding pair: example, BTCUSDT
    :param interval: time interval, 1m, 3m, 1h ...
    :param start_ts: start timestamp
    :param end_ts: end timestamp
    :param output_location: output file location ends with /
    :return: file on file system
    Example: get_data('BTCUSDT', '1m', 1630683540000, 1630683599999)
    '''
    try:
        BINANCE_API_KEY=os.environ["BINANCE_API_KEY"]
        BINANCE_SECRET_KEY=os.environ["BINANCE_SECRET_KEY"]
    except KeyError:
        raise KeyError

    client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)
    candles = client.get_klines(
        symbol=symbol,
        interval=interval,
        startTime=start_ts,
        endTime=end_ts
    )
    #pandas dataframe
    data = [sub[:len(sub)-3] for sub in candles] # removes unused data
    [sub.append(symbol) for sub in data] # add symbol as column
    columns = ["open_time", "open_price", "high_price", "low_price", "close_price", "BTC_volume", "close_time", "USD_volume", "number_of_trades", "trading_pair"]
    output_file = f'{output_location}{symbol}_{start_ts}_{end_ts}.parquet'

    df = pd.DataFrame(data=data, columns=columns)
    # write out parquet file
    table = pa.Table.from_pandas(df)
    pq.write_table(table, output_file, compression='GZIP')
    # print dataframe.
    print(df)

    '''
    #spark dataframe
    #loads data to the Spark Dataframe
    spark = SparkSession.builder.appName("Binance").getOrCreate()
    dataframe = spark.createDataFrame(data, columns)
    dataframe.show()
    dataframe.write.parquet(output_file)

    '''

    return f"Done. File location: {output_file}"


