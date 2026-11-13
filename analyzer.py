import re

THRESHOLD = 3
counts = {}

with open("auth.log") as f:
    for line in f:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                counts[ip] = counts.get(ip, 0) + 1

print("=== Failed Login Report ===")
for ip, total in counts.items():
    if total > THRESHOLD:
        print("SUSPICIOUS:", ip, "-", total, "failed attempts")
    else:
        print("ok:", ip, "-", total, "failed attempts")
