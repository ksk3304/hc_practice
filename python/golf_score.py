import sys

def validate_par_numbers(numbers):
    for j in numbers:
        if j < 3 or j > 5:
            return False
    return True

def validate_score_numbers(numbers):
    for j in numbers:
        if j <1:
            return False
    return True



golf_list = []
for line in sys.stdin.readlines():
    golf_list.append(line.strip())

par_list = golf_list[0].split(",")
if len(par_list) == 18:
    try:
        par_list = [int(i) for i in par_list]
        if not validate_par_numbers(par_list):
            print("規定打数は、3から5の間の数字を入力して下さい。")
            exit(1)
    except:
        print("数字以外が入力されています。")
        exit(1)
else:
    print("カンマ区切りで、18個の数字を入力して下さい。")
    exit(1)

score_list = golf_list[1].split(",")
if len(score_list) == 18:
    try:
        score_list = [int(i) for i in score_list]
        if not validate_score_numbers(score_list):
            print("スコアは、1以上の数字を入力して下さい。")
            exit(1)
    except:
        print("数字以外が入力されています。")
        exit(1)
else:
        print("カンマ区切りで、18個の数字を入力して下さい。")
        exit(1)

results = []
score_hash = {-4:"コンドル", -3:"アルバトロス", -2:"イーグル", -1:"バーディ", 0:"パー", 1:"ボギー"}
for i in range(0, 18):
    over = score_list[i] - par_list[i]
    if over >= 2:
        results.append(f"{over}ボギー")
        continue
    elif ((par_list[i] == 4 and over == -3) or
          (par_list[i] == 3 and over == -2)):
        results.append("ホールインワン")
        continue
    else:
        results.append(score_hash[over])
print(*results, sep=",")