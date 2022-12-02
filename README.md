# Traceroute

The utility displays a list of routers through which the packet passes 
until it reaches the destination

Utility get one argument -- destination address 

## Usage example
```
sudo python traceroute.py ya.ru
    
 1	_gateway (192.168.0.1) 0.949 ms
 2	217.197.8.1 (217.197.8.1) 2.021 ms
 3	172.24.31.5 (172.24.31.5) 3.596 ms
 4	vunk-punk.rtr.pu.ru (172.24.25.32) 2.735 ms
 5	magma-vunk.rtr.pu.ru (172.24.25.38) 20.102 ms
 6	vlan3.kronos.pu.ru (195.70.196.3) 4.583 ms
 7	195.70.206.129 (195.70.206.129) 2.558 ms
 8	yandex.spb.piter-ix.net (185.1.152.57) 6.007 ms
 9	sas-32z7-ae1.yndx.net (87.250.239.77) 21.356 ms
10	*
11	ya.ru (87.250.250.242) 19.900 ms

```