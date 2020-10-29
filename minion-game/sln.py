def minion(string):
    vowel_list = ['A','E','I','O','U']
    count = 1
    words_dict = {"kevin":[],"stuart":[]}
    while count <= len(string):
        if count == 1:
            for i in string:
                if i in vowel_list:
                    words_dict['kevin'].append(i)
                else:
                    words_dict['stuart'].append(i)
        else:
            for i in range(0,len(string)):
                word = string[i]
                for j in range(i+1,len(string)):
                    if len(word) == count:
                        break
                    else:
                        word+=string[j]
                
                if word[0] in vowel_list and len(word) ==count:
                    words_dict['kevin'].append(word)
                elif len(word) == count:
                    words_dict['stuart'].append(word)
        count+=1
    return words_dict
