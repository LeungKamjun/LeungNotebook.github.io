def vigenere_decrypt(ciphertext, keyword):
    # 将关键词转换为大写，以确保匹配大小写
    keyword = keyword.upper()
    decrypted_text = ""  # 存储解密后的文本
    keyword_len = len(keyword)  # 关键词的长度

    # 遍历密文中的每个字符
    for i in range(len(ciphertext)):
        char = ciphertext[i]  # 获取当前字符
        if char.isalpha():  # 检查字符是否为字母
            keyword_char = keyword[i % keyword_len]  # 获取关键词中的相应字符
            shift = ord(keyword_char) - ord('A')  # 计算移位量

            if char.isupper():  # 如果字符是大写字母
                # 解密大写字母并将其添加到解密文本中
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:
                # 解密小写字母并将其添加到解密文本中
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))

            decrypted_text += decrypted_char  # 将解密的字符添加到解密文本中
        else:
            # 如果字符不是字母，则直接添加到解密文本中
            decrypted_text += char

    return decrypted_text


# 示例用法
ciphertext = "/taz/kgizx/vwzwdhabl/qwkdqnc.mps"
keyword = "sziit"
decrypted_text = vigenere_decrypt(ciphertext, keyword)
print("解密后的文本: ", decrypted_text)
