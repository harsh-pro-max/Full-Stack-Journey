def persioninfo(**kwargs):
    for k,v in kwargs.items():
        print(k,'->',v)
persioninfo(name="samir",age="22")
persioninfo(name="harsh",age="22",profession="bca")