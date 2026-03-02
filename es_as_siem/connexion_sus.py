import socket

def simulate_port_scan(target_ip="127.0.0.1", max_port=1000):
    print(f"🚀 Lancement du scan de ports sur {target_ip}...")
    for port in range(1, max_port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.01) # Timeout très court pour aller vite
            s.connect((target_ip, port))
            s.close()
        except:
            pass
    print("✅ Scan terminé.")

simulate_port_scan()