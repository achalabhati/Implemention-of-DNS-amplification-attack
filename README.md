# Implemention-of-DNS-amplification-attack
Denial of Service attack is explicit attempt by an attacker to prevent legitimate user from ac- cessing the services (that is supposed to access by the user). Criminal perpetrators of DoS attacks often target sites or services hosted on high-profile web servers such as banks, credit card payment gateways; but motives of revenge, blackmail or activism can be behind other attacks.

DNS amplification attack is a sophisticated denial of service attack that takes advantage of DNS server behavior in order to amplify the attack [1] . This attack is a new type of atatck which utilizes the fact that size of response generated by DNS can be much larger than DNS request query. This attack is feasible only in case of recursive DNS server. The huge amount of traffic generated by DNS server is utilized to flood the target server i.e victim to establish denial of service attack.
Two malicious tasks are performed by attacker to launch DNS Amplification Attack on victim.
- The attacker will spoof the IP address of the DNS resolver and replaces it with the victim’s IP address. As a result all the response generated by DNS server will be redirected to victim server instead of going to attacker’s system.
-  The attacker searches for an Internet domain that is registered with many DNS records. During the attack, the attacker sends DNS queries to the DNS server that request the entire list of DNS records for that domain. Due to multiple DNS records associated with the request query , size of the response from DNS server becomes very huge and need to be split over several packets.

# Experimental Setup

We tried simulating DNS amplification attack in two Scenarios. In first scenario we used BIND9 software and dig tool, and in second scenario we used scapy to write an attacker program.

# Scenario 1
We setup a local DNS server using BIND9 software. It is a software that consists the DNS server component, various administration tools, and a DNS resolver interface library. We cre- ated and added our own NS records(name server records). These NS records are of size 4000 bytes. This helped us in simulating the attack by generating large size response,which increased our amplification factor.
We used one machine as an attacker and other machine was used as victim. Attacker spoofed the IP address of the victim using iptables rule(iptable is actually a front end to the kernel-level netfilter hooks that can manipulate the Linux network stack).

# Scenario 2
Using the dig tool we cannot send more than 1 request/second. So in place of dig tool, we used Scapy to generate DNS requests. Using this library we can fabricate packets containing DNS request. There is no need of any IP table rule for IP address spoofing, because we can directly set the victims IP address in source part while packet fabrication.

# Prevention at victim side
The solution is based on the one-to-one mapping of DNS requests and responses. Normal DNS query operation is performed when a client requests a name resolution. The query is being sent to the DNS server with it’s IP address as the source address. DNS query packet is sent using UDP (user datagram protocol) connection to the server. Upon receiving request from user DNS server replies with the answer that the client seek.
But whenever DNS Amplification Attack happens then the targeted machine(victim) receives responses without having previously sent out the corresponding request. As a result, such data (orphan pairs) must be immediately classified as suspicious and discarded. Based on this idea a simple mechanism can be employed at the victim’s side to prevent the attack. The idea [7] is described below:
Whenever a DNS request is being made from the client then store that request in a table. Whenever a DNS response is received then check that the response is legitimate means the response came due to a query that was made by the same system. We can match the query in the table which contains the query done previously. If it matches then there is no need to panic. Simply delete the entry in the table. If the response does not matches then it is suspicious. If such responses increases over a certain threshold values then we can assume that we are under DNS Amplification Attack. Then we can add rules in iptables to discard DNS responses from that particular DNS server.
