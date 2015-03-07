# -*- coding: utf-8 -*-

import math
import itertools

NUMBERS=u"☉ノ入∆□☖구す೭୫xc"
WORD_NUMS=["gó","θó","nē","hē","kâ","lâ","bō","fō","tī","rī","kwā","sā"]
PLACE_VALUE=[]

def convert_base(x, base=12, precision=None):
    length_of_int = int(math.log(x, base))
    iexps = range(length_of_int, -1, -1)
    if precision == None: fexps = itertools.count(-1, -1)
    else: fexps = range(-1, -int(precision + 1), -1)

    def cbgen(x, base, exponents):
        for e in exponents:
            d = int(x // (base ** e))
            x -= d * (base ** e)
            yield d
            if x == 0 and e < 0: break

    return cbgen(int(x), base, iexps), cbgen(x - int(x), base, fexps)

def to_galbraithanese(x):
    x=convert_base(x)
    part1=""
    for item in x[0]:
        if item in range(10):
            part1+=str(item)
        elif item==10:
            part1+="A"
        elif item==11:
            part1+="B"
        elif item==12:
            part1+="10"
        else:
            raise ValueError()
    part2=""
    for item in x[1]:
        if item in range(10):
            part2+=str(item)
        elif item==10:
            part2+="A"
        elif item==11:
            part2+="B"
        else:
            raise ValueError()
    base12=part1+"."+part2
    if part2=="0":
        base12=base12[:-2]
    for x in range(12):
        base12=base12.replace("0123456789AB"[x], NUMBERS[x])
    return base12.replace(".","_")[::-1]

def from_galbraithanese(n):
    for x in range(12):
        n=n.replace(NUMBERS[x], "0123456789AB"[x])
    return int(n[::-1],12)
    


def galbraithanese_number(n):
    if isinstance(n, int) or isinstance(n, long):
        n=to_galbraithanese(n)
    li=[]
    for let in n:
        li.append(NUMBERS.find(let))
    output=[]
    output.append(WORD_NUMS[li.pop(0)])
    output.append(WORD_NUMS[li.pop(0)]+"dē")
    pvalue=1
    for item in li:
        if pvalue>11:
            raise ValueError("Item over sā sādē sā-θógō sā-nēgō sā-hēgō sā-kâgō sā-lâgō sā-bōgō sā-fōgō sā-tīgō sā-rīgō sā-kwāgō sā-sāgō (106993205379071)")
        output.append(WORD_NUMS[item]+"-"+WORD_NUMS[pvalue]+"gō")
        pvalue+=1
    return " ".join(output)

    
    
            
    
    
