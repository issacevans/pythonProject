import sys


class Get_mounth():
    def __init__(self, m1="", char=""):
        self.__m = dict(ja="一月", f="二月", mar="三月", ap="四月", may="五月"
                        , jun="六月", jul="七月", au="八月", s="九月", o="十月", n="十一月", d="十二月")

    def into_key(self, count):
        key_word = input("請輸入月份的第" + str(count + 1) + "個字母 : ")
        while str.isalpha(key_word) != True or len(key_word) != 1:
            key_word = input("請輸入一個英文字母 : ")
        self.char = str.lower(key_word)
        if count > 0:
            self.m1 = self.m1 + str.lower(key_word)
        else:
            self.m1 = str.lower(key_word)

    def find_mounth(self, count):
        if self.m1 in self.__m:
            print(self.__m[self.m1])
            sys.exit()
        for key in self.__m:
            if count >= len(key):
                continue
            if (key[count] == self.char):
                no_mounth = 0
                break
            else:
                no_mounth = 1
        if no_mounth == 1:
            print("查無月份")
            sys.exit()


if __name__ == '__main__':
    get_m = Get_mounth()
    for i in range(3):
        get_m.into_key(i)
        get_m.find_mounth(i)

    # for i in range(3):
    #     key_word = input("請輸入月份的第" + str(i + 1) + "個字母")
    #     if i > 0:
    #         m = m + key_word
    #     else:
    #         m = key_word

    #     # for key in m1:
    #     if m in m1:
    #         print(m1[m])
    #         break

    """key_word = input("請輸入月份的第二個字母")
    # for key in m1:
    if (key_word + key_word1 == m1):
        print(m1[key_word + key_word1])

    key_word2 = input("請輸入月份的第三個字母")
    # for key in m1:
    if (key_word + key_word1 + key_word2 == m1):
        print(m1[key_word + key_word1 + key_word2])"""
