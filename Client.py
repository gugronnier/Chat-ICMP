#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
from scapy.all import *

print "!! USE Ctrl+C FOR EXIT !!\n"

print "Demarrage Client ..."
print "Envoi de la trame..."

def filtre(pkt): # Filtre a la reception
        data = pkt[Raw].load
        datas = data.split(" : ")
        for key in datas:
                # Si le message contient Serveur
                if key == "Serveur":
                        # Affichage du message
                        print pkt[Raw].load
                        # Récursif, on continu la conversation
                        main()

def main():
	# On capture le message à envoyer 
	msg = raw_input("RATESD : ")
	# Envoi de la réponse
	send( IP(dst="192.168.43.63") / ICMP(type="echo-request", id=0x123) / Raw(load="RATESD : "+msg),verbose=0)
        # Capture de la réponse
        sniff(prn=filtre, filter="icmp", count=1)
        #if rcv[Raw].load != "":
        #        print rcv[Raw].load
        
        

main()

