flitered: list[list] = []
with open("D:/Users/admin/Documents/温度传感器数据.txt", "r") as fSource:
    lines = fSource.readlines()
    flitered.append(lines[0])
    lines.remove(lines[0])
    i = 0
    pTemp = 0
    for line in lines:
        j = 0
        while line[j] != '\t':
            j += 1
        temperature = float(line[:j])
        if temperature - pTemp > 2:
            pTemp = int(temperature)
            flitered.append(line)
with open("D:/Users/admin/Documents/温度传感器-过滤.txt", "w") as fTar:
    fTar.writelines(flitered)
