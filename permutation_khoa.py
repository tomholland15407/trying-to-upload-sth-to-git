n = int(input())
    def merge(currentset,n):
        for s in currentset:

            for i in range(len(s)):
                s.append(s[i])
                s[i]=n
