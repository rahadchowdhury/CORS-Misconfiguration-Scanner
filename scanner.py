import argparse
import requests

#python cors_scanner.py domains.txt

print ("""

   ____ ___  ____  ____    __  __ _                      __ _                       _   _             
  / ___/ _ \|  _ \/ ___|  |  \/  (_)___  ___ ___  _ __  / _(_) __ _ _   _ _ __ __ _| |_(_) ___  _ __  
 | |  | | | | |_) \___ \  | |\/| | / __|/ __/ _ \| '_ \| |_| |/ _` | | | | '__/ _` | __| |/ _ \| '_ \ 
 | |__| |_| |  _ < ___) | | |  | | \__ \ (_| (_) | | | |  _| | (_| | |_| | | | (_| | |_| | (_) | | | |
  \____\___/|_| \_\____/  |_|  |_|_|___/\___\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|\__|_|\___/|_| |_|
                                                              |___/                                   
CORS Misconfiguration Scanner
Command: python scanner.py --file=domains.txt
Exploit URL: https://github.com/rahadchowdhury/CORS-Misconfiguration-Scanner
Author: Rahad Chowdhury
Info : This is a simple python script for detect CORS Misconfiguration!.
""")

def check_cors_vulnerability(domain):
    try:
        # Send a CORS request to the domain
        response = requests.get(domain)
        
        # Check if CORS headers are present in the response
        if 'Access-Control-Allow-Origin' in response.headers:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while scanning {domain}: {e}")
        return False

def main(file_path):
    # Read the list of domains from the specified file
    with open(file_path, 'r') as file:
        domain_list = [line.strip() for line in file.readlines()]
    
    vulnerable_domains = []
    safe_domains = []
    
    for domain in domain_list:
        if check_cors_vulnerability(domain):
            vulnerable_domains.append(domain)
        else:
            safe_domains.append(domain)
    
    print("Vulnerable domains:")
    for domain in vulnerable_domains:
        print(domain)
    
    print("\nSafe domains:")
    for domain in safe_domains:
        print(domain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan domains for CORS misconfiguration vulnerability")
    parser.add_argument("-f","--file", help="Path to the file containing a list of domains")
    args = parser.parse_args()
    
    main(args.file)
