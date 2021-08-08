class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        num_of_bulls = 0
        secret = list(secret)
        guess = list(guess)

        for i,s,g in zip(list(range(len(secret))),secret,guess):
            if s == g:
                num_of_bulls += 1
                secret[i] = ''
                guess[i] = ''

        num_of_cows = 0
        for s in secret:
            if s == '':
                continue
            if s in guess:
                num_of_cows += 1
                guess.remove(s)

        result = str(num_of_bulls) + "A" + str(num_of_cows) +"B"
        #print(result)
        return result
Solution().getHint(secret = "1807", guess = "7810")
Solution().getHint(secret = "1", guess = "0")
Solution().getHint(secret = "1", guess = "1")





