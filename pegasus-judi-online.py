from scapy.all import *
import re

# Daftar domain judi online yang diketahui
known_gambling_sites = [
    "examplecasino.com",
    "onlineslots.net",
    "pokerworld.com"
]

# Fungsi untuk memeriksa apakah domain ada dalam daftar judi online
def is_gambling_site(domain):
    for site in known_gambling_sites:
        if site in domain:
            return True
    return False

# Fungsi callback untuk menangkap paket
def packet_callback(packet):
    if packet.haslayer(DNSRR):
        # Ambil domain yang diminta
        dns_query = packet[DNSQR].qname.decode("utf-8")
        if is_gambling_site(dns_query):
            print(f"[!] Detected gambling site access: {dns_query}")

# Menangkap paket jaringan
sniff(prn=packet_callback, store=0)

