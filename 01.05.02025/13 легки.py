from ipaddress import ip_network

net = ip_network('157.127.172.56/157.127.191.78')
cnt = 0
for i in net:
    i = f'{int(i):032b}'
    if i.count('1')%2!=0:
        cnt+=1
print(cnt)