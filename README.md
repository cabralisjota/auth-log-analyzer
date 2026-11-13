# Auth Log Analyzer

A small Python tool that scans an SSH authentication log, counts failed login attempts per IP address, and flags IPs that exceed a threshold as suspicious.

## Why I built it

Brute-force login attempts are one of the most common signs of an attack. This project is my practice at parsing logs and turning raw text into a simple security report.

## How it works

1. Reads `auth.log` line by line
2. Finds lines containing "Failed password"
3. Extracts the source IP with a regular expression
4. Counts failures per IP using a dictionary
5. Flags any IP over the threshold (default: 3)

## Usage

    python analyzer.py

## Example output

    === Failed Login Report ===
    SUSPICIOUS: 203.0.113.5 - 5 failed attempts
    ok: 198.51.100.7 - 1 failed attempts

## Notes

- `auth.log` is sample data with fake entries, using documentation-reserved IP ranges.
- Change `THRESHOLD` at the top of `analyzer.py` to adjust sensitivity.
- Built and committed entirely from a phone using Termux.

## Ideas for next steps

- Accept a log file path as a command-line argument
- Output the report to a file
- Add time-window detection (many failures within a minute)
