import MySQLdb

'''
Should be passed as parameters
'''
HOST = "localhost"
PORT = 3306
USER = "root"
PASS = "...."
DB = "Test"
TABLE_NAME = "medals"


if __name__ == '__main__':

    try:
        connect = MySQLdb.connect(host=HOST, port=PORT,
                                  user=USER, passwd=PASS, db=DB, charset='utf8')

        cursor = connect.cursor()

        # read previously loaded max timestamp from raw data
        cursor.execute(f"select max(last_load_time) from Test.etl_process where table_name='{TABLE_NAME}'")
        max_load_dt = cursor.fetchone()[0].strftime('%Y-%m-%d %H:%M:%S')

        # update agg table
        cursor.execute(f"""
           INSERT INTO Test.medals (year, season, cntry_with_medals)
           select raw.year, raw.season, cnt
           from(
           select a.year, a.season, count(distinct a.team) cnt
           from Test.raw_data a
           where a.medal is not null and load_time > '{max_load_dt}'
           group by a.year, a.season
           ) raw
           ON DUPLICATE KEY UPDATE cntry_with_medals = raw.cnt
        """)

        # get max timestamp from raw data
        cursor.execute("select max(load_time) from Test.raw_data")
        update_max_load = cursor.fetchone()[0].strftime('%Y-%m-%d %H:%M:%S')

        # update max loaded timesttamp for the agg table
        cursor.execute(f"UPDATE Test.etl_process SET last_load_time = '{update_max_load}' where table_name='{TABLE_NAME}'")

    except (KeyError, TypeError) as e:
        print(e)

    finally:
        connect.commit()
        connect.close()


exit(0)