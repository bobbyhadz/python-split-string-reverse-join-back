# Split a string, reverse it and join it back in Python

my_str = 'bobby hadz com'

my_list = my_str.split(' ')
print(my_list)  # 👉️ ['bobby', 'hadz', 'com']

my_list.reverse()
print(my_list)  # 👉️ ['com', 'hadz', 'bobby']

my_str_again = ' '.join(my_list)
print(my_str_again)  # 👉️ com hadz bobby