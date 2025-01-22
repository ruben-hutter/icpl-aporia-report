if True:
    a = 3
if True:
    pred_0 = a > 0
if True:
    pred_1 = not pred_0
if pred_0:
    pred_2 = a > 2
if pred_0:
    pred_3 = not pred_2
if True:
    pred_4 = pred_0 and pred_2
if pred_4:
    b = 1
if True:
    pred_5 = pred_0 and pred_3
if pred_5:
    b = 0
if pred_0:
    print(b)
if pred_1:
    print(2) 
