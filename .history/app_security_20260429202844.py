from colorama import Fore, Style, init
init()
def scan_code_file(filename):
    try:
        with open(filename, "r") as f:
            code = f.read()
    except:
        print(Fore.RED + "Error reading file")
        return

    issues = []

    # SQL Injection detection
    if "execute(" in code and "+" in code:
        issues.append("SQL Injection Risk Detected")

    # XSS detection
    if "<script>" in code:
        issues.append("XSS Vulnerability Detected")

    # Hardcoded credentials
    if "password =" in code or "api_key =" in code:
        issues.append("Hardcoded Credential Found")

    if issues:
        print(Fore.RED + "\n⚠️ Vulnerabilities Found:")
        for issue in issues:
            print("-", issue)
    else:
        print(Fore.GREEN + "\n✅ No vulnerabilities detected")

    # Save report
    with open("app_security_report.txt", "w") as f:
        for issue in issues:
            f.write(issue + "\n")


# Run
file = input("Enter code file name (e.g., test.py): ")
scan_code_file(file)