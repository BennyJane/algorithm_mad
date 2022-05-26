# HJ36 字符串加密
while True:
    try:
        word = input()
        s = input()
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()  # 字母表
        n_word = ""  # 融入加密词后的新字母表
        res = ''

        for c in word:
            if c not in n_word:  # 加密单词剔除重复字母
                n_word += c
        for c in alpha:
            if c not in n_word:  # 用字母表剔除已有字母后补齐为26个新字母表n_word
                n_word += c
        for c in s:
            res += n_word[alpha.index(c)]
        print(res)
    except:
        break
