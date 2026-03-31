import pandas as pd
import datetime


# DataFrame 非空
# 主键(played_at)唯一性校验
# 无空值 (Data Accuracy)

def validate_data(df: pd.DataFrame) -> bool:
    
    if df.empty:
        print("No tracks found. Finishing execution.")
        return False

    # Primary Key Check
    if not pd.Series(df['played_at']).is_unique:
        raise Exception("Data Consistency Error: Primary Key violation found.")

    # Data Quality Check
    if df.isnull().values.any():
        raise Exception("Data Accuracy Error: Null values detected.")

    return True

 # 数据转换 (Transform): Pandas 进行数据清洗与结构化

def transform_tracks(raw_data):
    song_names, artist_names, played_at_list, timestamps = [], [], [], []

    for item in raw_data.get("items", []):
        song_names.append(item["track"]["name"])
        artist_names.append(item["track"]["album"]["artists"][0]["name"])
        played_at_list.append(item["played_at"])
        timestamps.append(item["played_at"][0:10])

    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "timestamp": timestamps
    }

    return pd.DataFrame(song_dict)