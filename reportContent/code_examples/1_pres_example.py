a = 3
pred_0 = a > 0
pred_1 = not pred_0
if pred_0:
    pred_2 = a > 2
    pred_3 = not pred_2
    if pred_2:
        b = 1
    if pred_3:
        b = 0
    print(b)
if pred_1:
    print(2)
