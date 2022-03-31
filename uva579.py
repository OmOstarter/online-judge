while True:
    try:
        h, m = map(int, input().split(":"))
    except EOFError:
        break
    if h==0 and m == 0:
        break
    angle_h = h * 30 + m/60 * 30 # 30分 + 15度 
    angle_m = m * 6
    if abs(angle_h - angle_m) >= 360:
        angle = abs(angle_h - angle_m) - 360
    elif abs(angle_h - angle_m) >= 180.0:
        angle = 360 - abs(angle_h - angle_m) 
    else:
        angle = abs(angle_h - angle_m)
    print("{:.3f}".format(angle))
