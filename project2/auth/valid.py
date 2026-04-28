
def pw_len_check( pw ):
    return len(pw) >=6 

def id_len_check( id ):
    return len(id) >= 4 and len(id)<=12
    # if  4 <= len(id) <=12:
    # if len(id) >= 4 and len(id)<=12 :
    #     return True
    # else:
    #     return False