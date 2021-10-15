import pandas_test as pd
from pathlib import Path
from sqlalchemy import create_engine


'''
Should be passed as parameters
'''
HOST = "localhost"
PORT = 3306
USER = "root"
PASS = "...."
DB = "Test"
TABLE_NAME = "raw_data"
MY_SQL_DRIVER = ".../mysql-connector-java-8.0.23.jar"
SOURCE_DIR = ".../data"
ARCH_LOCATION = ".../data/archive"

jsons_location = Path(SOURCE_DIR)

list_of_df = []
list_of_files = []
# reads json files from the source dir

for file in jsons_location.iterdir():
    if file.is_file() and file.suffix == '.json':
        data = pd.read_json(file, lines=True)
        list_of_df.append(data)
        list_of_files.append(file)

# concatenate all dataframes with data.
data_from_files_df = pd.concat(list_of_df, ignore_index=True)

# Connect to MySQL
engine = create_engine(f"mysql://{USER}:{PASS}@{HOST}/{DB}")
con = engine.connect()


data_from_files_df.to_sql(name=TABLE_NAME, con=con, if_exists='append', index=False)

# move processed files to archive
for json_file in list_of_files:
    src_file_name = SOURCE_DIR + "/" + json_file.stem + ".json"
    dest_file_name = ARCH_LOCATION + "/" + json_file.stem + ".json"
    Path(src_file_name).rename(dest_file_name)

con.close()
exit(0)
