#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
from scapy.all import *

print "!! USE Ctrl+C FOR EXIT !!\n"

print "Demarrage Serveur..."
print "Ecoute..."

def filtre(pkt): # Filtre a la reception
	global data,srcip
	srcip=pkt[IP].src
	data = pkt[Raw].load

def traitement(donnees):
	datas = donnees.split(" : ")
	for key in datas:
		# Si le message contient Serveur
		if key == "CHATICMP":
			# Affichage du message
			print donnees

def envoi(msg):
	# Envoi de la réponse
	send( IP(dst=srcip) / ICMP(type="echo-reply", id=0x123) / Raw(load="Serveur : " + str(msg)),verbose=0)

def reception():
	sniff(prn=filtre, filter="icmp", count=1)
	return data

def input_data():
	msg = raw_input("Serveur : ")
	return msg

def main():
	# Capture de la réponse
	data = reception()
	# Traitement du message
	traitement(data)
	# Capture du message a envoyer
	msg = input_data()
	# Envoi de la réponse
	envoi(msg)
	# Récursif, on continu la conversation
	main()
        

# Initialisation 
main()
