ips = [
    "192.168.1.10",
    "192.168.1.10",
    "192.168.1.20",
    "192.168.1.30",
    "192.168.1.10",
    "192.168.1.20",
    "192.168.0.10",
    "192.168.0.0"
]

failed_ips = {}

for ip in ips:

    if ip in failed_ips:
        failed_ips[ip] += 1
    else:
        failed_ips[ip] = 1

print(failed_ips)

for ip in failed_ips:
    if failed_ips[ip] >=1:
        print("🚨 Suspicious IP detected:", ip)
