from lista import *


__all__ = ['pilha_vazia', 'pilha_push', 'pilha_pop']


def pilha_vazia():
    return lst_vazia()


def pilha_push(ele):
    lst_insFin(ele)

def pilha_pop():
     if(not pilha_vazia()):
         return lst_retFin()
     return None
    
