# Basic port scanning using Python (if-else statements)

port = int(input("Enter the port number: "))

common_port = {
    20: "ftp",
    21: "ftp",
    22: "ssh",
    80: "http",
    443: "https",
    53: "dns",
    110: "pop3",
    143: "imap",
    3306: "mysql",
    3389: "rdp",
    5432: "postgres",
}

if port in common_port:
    print(f"Port {port} is open - {common_port[port]}")
    if port in [21, 22, 80, 443]:
        print("Warning!!!! This is an attackable port that might be targeted for attacks and enumeration.")
    else:
        print("This port is common but not typically a primary target for attacks.")
else:
    print("The port is not in the common list or is not open.")

print("\nDisclaimer: This script is for educational purposes only. Use it responsibly. — Prasangam")