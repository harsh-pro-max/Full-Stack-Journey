def deco_result(result_func):
    def distinction(marks):
        for m in marks:
            if m>75:
                print(m,"Distinction")
        else:
            result_func(marks)
    return distinction


@deco_result
def result(marks):
    for m in marks:
        if m>=33:
            pass
        else:
            print("fail")
            break
    else:
        print("pass")

marks=[45,78,90,6,54]
result(marks)