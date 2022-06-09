N = int(input())

cnt = 0
for hour in range(N+1):
    if hour % 10 == 3 or hour // 10 == 3:
        cnt += 3600
        continue
    for minute in range(60):
        if minute % 10 == 3 or minute//10==3:
            cnt += 60
            continue
        for sec in range(60):
            if sec % 10 == 3 or sec//10==3:
                cnt+=1

# 3이 들어갈 때 라는 조건을 몫과 나머지로 잘 구현했지만
# if '3' in str(hour)+str(minute)+str(sec):
#   cnt += 1 이 더 깔끔하다..!
        
    
print(cnt)
