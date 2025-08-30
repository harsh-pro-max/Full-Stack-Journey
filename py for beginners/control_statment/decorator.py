# use of decorator
def deco_result(result_fun):
    def distinction(marks):
        for m in marks:
            if m>75:
                print(m,"Distinction")
            
        result_fun(marks)
    return distinction

@deco_result
def result(marks):
    for e in marks:
        if e>=33:
            pass
        else:
            print("fail")
            break
    else:
        print("pass")
marks=[45,78,98,33,54]
result(marks)

