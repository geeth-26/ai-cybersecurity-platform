from colorama import Fore, Style, init
init()

def scan_code_file(filename):
    print(Fore.CYAN + "="*55)
    print("     AI CYBERSECURITY ANALYSIS PLATFORM")
    print("="*55 + Style.RESET_ALL)

    try:
        with open(filename, "r") as f:
            code = f.read()
    except:
        print(Fore.RED + "Error reading file")
        return

    issues = []

    if "execute(" in code and "+" in code:
        issues.append("SQL Injection Risk Detected")

    if "<script>" in code:
        issues.append("XSS Vulnerability Detected")

    if "password =" in code or "api_key =" in code:
        issues.append("Hardcoded Credential Found")

    print("\n===== ANALYSIS REPORT =====")
    print("Module: Application Security\n")

    if issues:
        for issue in issues:
            print(Fore.RED + "⚠️ " + issue)
    else:
        print(Fore.GREEN + "✅ No vulnerabilities detected")

    print("===========================\n")

    with open("app_security_report.txt", "w") as f:
        for issue in issues:
            f.write(issue + "\n")


file = input("Enter code file name (e.g., sample_code.py): ")
scan_code_file(file)