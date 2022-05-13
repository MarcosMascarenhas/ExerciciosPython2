cv, ce, cs, fv, fe, fs = input().split()
cv = int(cv)
ce = int(ce)
cs = int(cs)
fv = int(fv)
fe = int(fe)
fs = int(fs)

cpontos = cv*3 + ce
fpontos = fv*3 + fe

if cpontos < fpontos:
    print("F")
elif cpontos > fpontos:
    print("C")
else:
    if cs < fs:
        print("F")
    elif cs > fs:
        print("C")
    else:
        print("=")

"""
if cpontos < fpontos:
    print("F")
elif cpontos > fpontos:
    print("C")
elif cs < fs:
    print("F")
elif cs > fs:
    print("C"):
else:
    print("=")
"""

"""
if (cpontos, cs) < (fpontos, fs):
    print("F")
elif (cpontos, cs) >(fpontos, fs):
    print("C")
else:
    print("=")
"""
