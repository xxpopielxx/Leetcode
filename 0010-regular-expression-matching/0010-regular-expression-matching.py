class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m+1) for _ in range(n+1)] #dp[i][j] = True jeśli s[0:i] pasuje do p[0:j] 

        dp[0][0] = True

        for j in range(2, m+1): #pusty string, jesli np a* no to możemy zrobic z tego ""
            if p[j-1] == "*":
                dp[0][j] = dp[0][j-2] #sprawdzamy czy 2 wcześniej się dało zrobić pusty czy nie
        
        for i in range(1,n+1): #każdy podstring od początku do i w s
            for j in range(1, m+1): #tak samo tylko dla p
                #case1 zwykłe dopasowanie
                if p[j-1] == s[i-1] or p[j-1] == ".":
                    dp[i][j] = dp[i-1][j-1]
                
                #case2 *
                elif p[j-1] == "*":
                    #case2.1 zero razy
                    dp[i][j] = dp[i][j-2]
                    #case2.2 więcej
                    if p[j-2] == s[i-1] or p[j-2] == ".":
                        dp[i][j] = dp[i][j] or dp[i-1][j] #jeśli 0 wystąpień = True to zostaw, w innym przypadku dp[i-1][j],
                        #czyli najpierw sprawdzamy czy ostani znak w s pasuje do tego przed *, jesli tak to sprawdzamy czy bez tego
                        #ostatniego znaku jest False czy True, jeśli True no to możemy go dołożyć i dalej będzie True jeśli nie no to nie 

        
        return dp[n][m] #crazy zadanie
        