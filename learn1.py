# value = 1
# for i in range(4):
#     for item in range(i+1):
#         print(value, end=" ")
#         value+=1
#     # end for
#     print("")
# # end for

for i in range(9): print(*range((i+1)*(i)//2+1, (i+1)*(i+2)//2+1))


