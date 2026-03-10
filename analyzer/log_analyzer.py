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

with open(report_file, "w") as file:
    file.write(report)

print("Report saved to security_report.txt")
