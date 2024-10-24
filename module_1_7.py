immutable_var = ('чай', 15, 5.0, [9,8])
print(immutable_var)
# immutable_var[1] = 3
# TypeError: 'tuple' object does not support item assignment
mutable_list = ['чай', 15, 5.0, [9,8]]
mutable_list[0] = 'кофе'
mutable_list[1] = 3
print(mutable_list)
