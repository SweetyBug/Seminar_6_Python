def rle_encod(data):
    encod_s = ''
    count = 1
    for i in range(len(data)):
        if i != 0:
            if data[i] == data[i-1]:
                count += 1
            else:
                encod_s += str(count) + data[i-1]
                count = 1
    encod_s += str(count) + data[i]
    return encod_s

def rle_decod(data):
    slovar_nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    decode_s = ''
    s = ''
    for i in range(len(data)):
        if data[i] in slovar_nums:
            s += data[i]
        else:
            decode_s += int(s) * data[i]
            s = ''
    return decode_s





