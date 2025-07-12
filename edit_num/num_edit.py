def num_editor(num) : 
    num_lst = []
    count = len(num) - 1
    for i in range(len(num)) : 
        num_lst.append(num[i]) 
        num_lst[i] = num[(count - i)]   
    result = "".join(num_lst)
    print(result)

txt = "I born in 6002 and  alive "
def analyze(matn) : 
    txt_lst = []
    for i in matn:
        if i.isdigit() :
            txt_lst.append(i)
    num_editor(txt_lst)
    
    
analyze(txt)
    