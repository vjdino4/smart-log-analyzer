import matplotlib.pyplot as plt

report_file = "C:/Users/asus/soc_project/logs/security_report.txt"

success = 0
failed = 0
brute = 0

with open(report_file, "r") as file:
    lines = file.readlines()

for line in lines:

    if "Successful Logins" in line:
        success = int(line.split(":")[1])

    if "Failed Logins" in line:
        failed = int(line.split(":")[1])

    if "Brute Force Attacks" in line:
        brute = int(line.split(":")[1])

labels = ["Successful Logins", "Failed Logins", "Brute Force Attacks"]
values = [success, failed, brute]

plt.bar(labels, values)

plt.title("SOC Security Dashboard")
plt.xlabel("Security Events")
plt.ylabel("Count")

plt.show()
