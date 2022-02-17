
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1

            if (d, target) in memo:
                return memo[(d, target)]

            to_return = 0

            for k in range(max(0, target - f), target):
                print(dp(d - 1, k))
                to_return += dp(d - 1, k)

            memo[(d, target)] = to_return
            return to_return

        return dp(d, target) % (10 ** 9 + 7)


#s = Solution()
#print(s.numRollsToTarget(5, 6, 18))

"""key = {'a':'n', 'b':'o', 'c':'p', 'd':'q',
       'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y',
       'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g',
       'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O',
       'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W',
       'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E',
       'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}


def decipher(sometext):
       result = ""
       for c in sometext:
              if c.isalpha():
                     result += key[c]
              else:
                     result += c
       return result

def main():
       print(decipher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq! "))

       print(decipher("Caesar cipher? I much prefer Caesar salad! "))


if __name__ == '__main__':
    main()"""

"""
class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rectangle[i][j] = newValue
                self.rectangle[i][j] = newValue


    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
"""

def numJewelsInStones(jewels: str, stones: str) -> int:
    count = 0
    for c in stones:
        if c in jewels:
            count += 1
    return count

print(numJewelsInStones("aA", "aAAbbbb"))





