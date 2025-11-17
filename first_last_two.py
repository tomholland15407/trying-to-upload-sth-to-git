s=input().strip()
if len(s)<2:
    print("empty")
else:
    print(s[:2] + s[-2:])