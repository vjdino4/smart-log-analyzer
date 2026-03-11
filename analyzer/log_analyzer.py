import time

log_file = "C:/Users/asus/soc_project/logs/logs.txt"

report_file = "C:/Users/asus/soc_project/logs/security_report.txt"

failed_ips = {}

total_logs = 0
failed_logins = 0
success_logins = 0
brute_force_count = 0

with open(log_file, "r") as file:
    logs = file.readlines()

for log in logs:

    total_logs += 1

    if "LOGIN_SUCCESS" in log:
        success_logins += 1

    if "LOGIN_FAILED" in log:
        failed_logins += 1

        parts = log.split("ip=")
        ip = parts[1].strip()

        if ip in failed_ips:
            failed_ips[ip] += 1
        else:
            failed_ips[ip] = 1

for ip, count in failed_ips.items():
    if count >= 3:
        brute_force_count += 1


report = f"""
===== SECURITY REPORT =====

Total Logs: {total_logs}
Successful Logins: {success_logins}
Failed Logins: {failed_logins}
Brute Force Attacks: {brute_force_count}
"""

print(report)


# Simulated Threat Intelligence Database
malicious_ips = [
    "45.23.11.90",
    "103.45.67.89",
    "185.22.98.10"
]

with open(report_file, "w") as file:
    file.write(report)

print("Report saved to security_report.txt")
ip_activity = {}

for log in logs:

    if "ip=" in log:

        try:
            ip = log.split("ip=")[1].strip()

            if ip in ip_activity:
                ip_activity[ip] += 1
            else:
                ip_activity[ip] = 1

        except:
            continue


print("\nSuspicious IP Activity:\n")

for ip, count in ip_activity.items():

    if count > 3:
        print("⚠ Suspicious activity detected from IP:", ip, "Events:", count)


print("\nThreat Intelligence Check:\n")

for ip in ip_activity:

    if ip in malicious_ips:

        print("⚠ THREAT INTELLIGENCE ALERT")
        print("Malicious IP detected:", ip)



        
while True:

    print("\nMonitoring logs for new activity...\n")

    with open(log_file, "r") as file:
        logs = file.readlines()

    failed_logins = 1

    for log in logs:

        if "FAILED_LOGIN" in log:
            failed_logins += 1

    if failed_logins >= 1:

        print("🚨 SECURITY ALERT 🚨")
        print("Possible brute force attack detected!")

    time.sleep(10)
