from datetime import datetime

# my_tuple_list = [ 
#     ("2024-03-24", 1),
#     ("2024-03-15", 2),
#     ("2006-12-14", 3),
# ]

# for item in my_tuple_list:
#     item_date = datetime.strptime(item[0], ("%Y-%m-%d"))
#     print(item_date.month)
#     print(item_date.year)

current_date = datetime.now().date()
print(current_date)
