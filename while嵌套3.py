# 九九乘法表
i = 1  # 控制行号
while i <= 9:
    j = 1
    while j<=i:
        print(f'{j}x{i}={i*j}',end = '\t')
        j += 1
    print('')
    i += 1