## 25501 
import sys
def recursion(s, l, r):
    global cnt
    if l >= r: return f"1 {cnt}"
    elif s[l] != s[r]: return f"0 {cnt}"
    else:
        cnt += 1 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(sys.stdin.readline())

for _ in range(T):
    cnt = 1
    word = sys.stdin.readline().rstrip()
    print( isPalindrome(word) )
