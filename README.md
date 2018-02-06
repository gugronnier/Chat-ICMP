# Chat-ICMP


## Requirements


#### Linux
###### sudo apt-get install python2.7 python3 python2.7-pip python3-pip
###### sudo pip3 install PyX
###### sudo pip install scapy


#### Windows
###### install python2.7
###### install dnet https://raw.githubusercontent.com/Kondziowy/scapy_win64/master/win64/dnet-1.12.win-amd64-py2.7.exe
###### install pcap https://raw.githubusercontent.com/Kondziowy/scapy_win64/master/win64/pcap-1.1.win-amd64-py2.7.exe
###### install scapy https://raw.githubusercontent.com/Kondziowy/scapy_win64/master/win64/scapy-2.2.0.win-amd64.exe


## Parameters


###### In the client code (Client.py):
######## 	send( IP(dst="192.168.43.63") / ICMP(type="echo-request", id=0x123) / Raw(load="RATESD : "+msg),verbose=0)
###### you need to modify the IP "192.168.43.63" by your server IP.


## Contributors

| Contributors | Contact address | Employer | Position |
|:-----------:|:------------:|:------------:|:------------:|
| Guillaume Gronnier | <gglyon769@gmail.com> | CEIS SecuInsight | Cyber Thread Intelligence Analyst

