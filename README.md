# CORS Misconfiguration Scanner
CORS is a security feature implemented by web browsers to restrict cross-origin HTTP requests that are initiated from scripts running within a web page. It is designed to prevent unauthorized access to resources on a different origin (domain).
This is a simple python script for detect CORS Misconfiguration!

# With this script:
You can specify the path to the text file containing the list of domains as a command-line argument.
The script reads the list of domains from the specified file and scans each domain for CORS misconfiguration vulnerability.
It then prints the results, listing vulnerable and safe domains separately.
To use this script, save it to a Python file (e.g., scanner.py) and run it from the command line, specifying the path to the domain list text file:

# Command
python cors_scanner.py --file=domains.txt

![cors_miss](https://github.com/rahadchowdhury/CORS-Misconfiguration-Scanner/assets/41516016/0c0c9f59-852c-4746-a81a-f7bfdc798a97)

Replace domains.txt with the path to your text file containing the list of domains. The script will then scan each domain in the file and print the results.
