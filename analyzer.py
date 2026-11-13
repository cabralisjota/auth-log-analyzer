import re

counts = {}

with open("auth.log") as f:
    for line in f:
        if "Failed password" in line:
            match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            if match:
                ip = match.group(1)
                counts[ip] = counts.get(ip, 0) + 1

for ip, total in counts.items():
    print(ip, "failed", total, "times")
