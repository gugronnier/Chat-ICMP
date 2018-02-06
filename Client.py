#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
from scapy.all import *

print "!! USE Ctrl+C FOR EXIT !!\n"

print "Demarrage Client ..."
print "Envoi de la trame..."

def filtre(pkt): # Filtre a la reception
	global data
	data = pkt[Raw].load

def traitement(donnees):
	datas = donnees.split(" : ")
        for key in datas:
                # Si le message contient Serveur
                if key == "Serveur":
                        # Affichage du message
                        print donnees

def input_data():
	msg = raw_input("CHATICMP : ")
	return msg

def envoi(msg):
	# Envoi de la réponse
	send( IP(dst="192.168.43.63") / ICMP(type="echo-request", id=0x123) / Raw(load="CHATICMP : " + str(msg)),verbose=0)

def reception():
	sniff(prn=filtre, filter="icmp", count=1)
	return data
        
def main():
	# Capture du message
	msg = input_data()
	# Envoi de la réponse
	envoi(msg)
	# Capture de la réponse
	data = reception()
	# Traitement du message
	traitement(data)
	# Recursif
	main()

# Initialisation 
main()
