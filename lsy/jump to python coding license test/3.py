def chkDupNum(s):
    result=[]
    for num in result:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result)==10
