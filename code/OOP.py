import datetime
h,m,s,x = map(int, input().split())

t = datetime.datetime(1,1,1, h, m, s) + datetime.timedelta(0,x)

print(' '.join([str(int(_)) for _ in  t.strftime("%I %M %S").split(' ')]))
