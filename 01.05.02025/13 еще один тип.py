from ipaddress import ip_network, ip_address

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')

for mask in range(10,31):
    net1 = ip_network(f'{ip1}/{mask}',False)
    net2 = ip_network(f'{ip2}/{mask}',False)
    if net1 == net2 and ip1 in net1.hosts() and ip2 in net2.hosts():
        print(net1.num_addresses)

