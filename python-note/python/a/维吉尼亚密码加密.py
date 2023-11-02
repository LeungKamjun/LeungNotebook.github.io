def KeyTran(key, keyLen):  # key是原密钥串，keylen是输入的明文长度
    strResult = ""
    if (len(key) > keyLen):  # 密钥串长度大于明文长度
        strResult = key[0:keyLen]  # 字符串赋值，密钥只需要使用明文长度的部分就行,范围是0到keylen-1
    else:  # 密钥长度小于等于明文长度
        newKeyList = list()
        index = 0
        while (index < keyLen):  # append向列表或元组“追加”一个密钥字符
            newKeyList.append(key[index % len(key)])  # 开始给新密钥列表赋值，一个key的长度结束再从这个key的前面开始，如此循环，直到和明文一样长
            index += 1
        strResult = "".join(newKeyList)  # join字符串操作数函，里面放列表、元组、字典
    return strResult


def PassMatrix():  # 明文和密钥组成的矩阵
    pm = list()
    startIndex = 65  # 65是字符A的ascii码值
    while (startIndex < 91):  # 90是字符Z的ascii码值
        pmRow = list()
        i = 0
        while (i < 26):  # 得到一行的字符
            currChr = startIndex + i  # 从字符A开始
            if (currChr > 90):  # 过了Z又重新从A开始
                currChr = currChr - 26
            pmRow.append(chr(currChr))  # 拼接的是字符
            i += 1
        print("".join(pmRow))
        pm.append(pmRow)  # 拼接的是列表
        startIndex += 1
    return pm


txtPlain = input("please input your plain text:")
txtPlain = txtPlain.upper()
print(txtPlain)

txtKey = input("please input your key:")
txtKey = txtKey.upper()
print(txtKey)

print("trasforming the key...")
txtNewKey = KeyTran(txtKey, len(txtPlain))

print("Constructing key password matrix:")
lsPM = PassMatrix()

print("Plain Text:    ", txtPlain)
print("encryption key:", txtNewKey)

print("encrypting...")

gapPlain = 0
gapKey = 0

strResult = list()

index = 0
for ch in txtPlain:
    gapPlain = ord(ch) - ord('A')  # 当前明文字符ch，转成26个字母里的顺序，从A开始是0，若为Z，则gapPlain=25
    gapKey = ord(txtNewKey[index]) - ord('A')  # 新密钥中对应位index上密钥字符txtNewKey[index]对应的索引值
    # print(ch,txtNewKey[txtPlain.index(ch)],"|",gapPlain,",",gapKey,"->",lsPM[gapKey][gapPlain])
    print(ch, txtNewKey[index], "|", gapPlain, ",", gapKey, "->", lsPM[gapKey][gapPlain])
    #  print(txtPlain.index(ch))#当前明文字符ch在txtPlain中第一个匹配项的位置
    strResult.append(lsPM[gapKey][gapPlain])  # 密钥在行，明文在列
    index += 1

print("encryption result:", "".join(strResult))
'''
base=ord('A')
step=ord('T')-ord('R')
print(base)
print(step)
for ch in text:
    if(ord(ch)>=65):
        newchr=ord(ch)+step
        if(newchr>=91):
            newchr-=26
        print(newchr)
        print(ch,"-->",chr(newchr))

'''
