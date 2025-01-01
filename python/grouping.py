import random

# 1ヵ月後にやったもので、課題提出時よりもコードが汚いです
pick_up_number = random.randint(2, 3)
group_list = ["A", "B", "C", "D", "E", "F"]
groupX = random.sample(group_list, pick_up_number)
group1 = []
group2 = []
for i in group_list:
    if i in groupX:
        group1.append(i)
    else:
        group2.append(i)
print(group1)
print(group2)