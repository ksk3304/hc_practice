import sys
from datetime import datetime, timedelta

month = datetime.now().month

# コマンドライン引数のチェック
if len(sys.argv) >= 3:
    if sys.argv[1] == '-m':
        try:
            month = int(sys.argv[2])
            if month < 1 or month > 12:
                print(f"{month} is neither a month number (1..12) nor a name")
                exit(1)
        except ValueError:
            print(f"{month} is neither a month number (1..12) nor a name")
            exit(1)

now = datetime.now()
this_year = now.year
weekday_list = ["月", "火", "水", "木", "金", "土", "日"]

# 来月の1日を取得する
if month == 12:
    next_month_initial = datetime(this_year+1, 1, 1)
else:
    next_month_initial = datetime(this_year, month+1, 1)

# 今月の最終日を取得する
month_last = next_month_initial - timedelta(days=1)
month_last_day = month_last.day

# 今月の1日から最終日までをリストに格納する
month_day_list = []
for i in range(1, month_last_day+1):
    if i < 10:
        month_day_list.append(" "+str(i))
    else:
        month_day_list.append(str(i))

# 今月の1日の曜日を取得する
month_initial_weekday_index = datetime(this_year, month, 1).weekday()

# 今月1日の曜日に応じて、リストにスペースを格納する
for i in range(0, month_initial_weekday_index):
    month_day_list.insert(0, "  ")

# カレンダー1行目を出力する
print(f"      {month}月 {this_year}")
# カレンダー2行目を出力する
print(" ".join(weekday_list))
# カレンダー3行目以降を出力する
for i in range(0, len(month_day_list)+1, 7):
    print(" ".join(month_day_list[0+i:7+i]))


