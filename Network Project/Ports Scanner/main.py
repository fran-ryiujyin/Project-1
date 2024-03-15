# Import necessary modules
import socket
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# Target
target = input("Enter the target IP: ")

# Define Target
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return port
    except:
        return None

# Get Open Ports
def openport(first=1, last=1025):
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = list(executor.map(portscan, range(first, last)))
    return [result for result in results if result]

# Convert to Dataset
def convert():
    open_ports = openport()
    open_ports_df = pd.DataFrame(open_ports, columns=['Port'])
    open_ports_df['Status'] = 'open'
    print(open_ports_df)

# Main Function
def main():
    convert()

if __name__ == "__main__":
    main()