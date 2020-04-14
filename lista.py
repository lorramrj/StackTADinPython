__all__ = ['lst_vazia', 'lst_insIni', 'lst_insFin', 'lst_retIni', 'lst_retFin', 'lst_posIni', 'lst_prox']

def lst_vazia():
    return lst == []


def lst_insIni(ele):
    global lst
    lst.insert(0, ele)


def lst_insFin(ele):
    global lst
    lst.append(ele)


def lst_retIni():
    global lst
    if(not lst_vazia()):
        return lst.pop(0)
    return None
        

def lst_retFin():
    if(not lst_vazia()):
        return lst.pop()
    return None


def lst_posIni():
     global corr, idx
     if(not lst_vazia()):
       corr = lst[0]
       idx = 0
     else:
       corr = None
     

def lst_prox():
    global corr, idx

    if(corr == None or idx == len(lst)):
        return None

    if(idx == len(lst)-1):
        return corr

    idx += 1
    corr = lst[idx]
    return lst[idx-1]


idx = None
corr = None
lst = []    



    
