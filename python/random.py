
import random

members_list = ["A", "B", "C", "D", "E", "F"]
random.shuffle(members_list)
group_a_size = random.randrange(2, 4)
group_a_members_list = sorted(members_list[:group_a_size])
group_b_members_list = sorted(members_list[group_a_size:])
print(group_a_members_list)
print(group_b_members_list)