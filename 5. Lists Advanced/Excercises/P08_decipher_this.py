# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)

sipher = input().split(" ")
desiphered = []
for i in range(len(sipher)):
    word = list(sipher[i])
    list_num = [x for x in word if(x.isdigit())]
    int_num = "".join(list_num)
    desiphered.append(chr(int(int_num)))
    str_list = [x for x in word if not(x.isdigit())]
    str_list[0], str_list[-1] = str_list[-1], str_list[0]
    str_list = [str(el) for el in str_list]
    final_list = desiphered + str_list

    result =  "".join(final_list)

    print(result, end=" ")
    desiphered = []