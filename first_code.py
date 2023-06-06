class Sequence():
    def __init__(self, nu):
        self.__nu = nu

    def seq(self):
        for i in range(len(self.__nu)):
            for j in range(len(self.__nu)):
                if j + 1 == len(self.__nu):
                    break
                elif self.__nu[j] > self.__nu[j + 1]:
                    self.__nu[j], self.__nu[j + 1] = self.__nu[j + 1], self.__nu[j]
                else:
                    continue
        print(self.__nu)


if __name__ == '__main__':
    nu = [2, -6, 3, 1, -5, 20, -3, 10, 9, 32]
    sq = Sequence(nu)
    sq.seq()
