#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from scapy.all import *
import time

print "!! USE Ctrl+C FOR EXIT !!\n"

print "Demarrage Serveur..."
print "Ecoute..."

def filtremessage(pkt): # Filtre a la reception
        data = pkt[Raw].load
        datas = data.split(" : ")
        for key in datas:
                # Si le message contient RATESD
                if key == "RATESD":
                        # Affichage du message
                        print pkt[Raw].load
                        # On capture le message à envoyer 
                        msg = raw_input("Serveur : ")
                        # On récupère l'emetteur
                        srcip=pkt[IP].src
                        # Envoi de la réponse
                        send( IP(dst=srcip) / ICMP(type="echo-reply", id=0x123) / Raw(load="Serveur : $
                        # On continu la conversation
                        main()

def main ():
        # Sniff réseau des paquets ICMP
        sniff(prn=filtremessage, filter="icmp", count=1)

main()
