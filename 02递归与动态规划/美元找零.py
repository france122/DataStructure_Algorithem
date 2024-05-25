# 当change>0时找coinvaluelist中最接近change的coin
# 贪心算法在美元体系中表现尚可，但如果有21、25这种币值就不再适用了
def txchange(coinvaluelist,change,coinslist):
    if change in coinvaluelist:
        coinslist.append(change)
    else:
        while change>0:
            coin=max([c for c in coinvaluelist if c<=change])
            coinslist.append(coin)
            change-=coin
    return coinslist
if __name__=="__main__":
    coinvaluelist=[1,5,10,20,50,100]
    output=txchange(coinvaluelist,63,[])
    print("最少硬币数为",len(output))
    print("分别为",end="")
    print(*(x for x in output))