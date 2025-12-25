import datetime
import json
import webbrowser
import urllib.parse
import os
import time

# ---------------- CONFIG ----------------
SUPPORT_EMAIL = "support@whatsapp.com"
LOG_DIR = "reports"
LOG_FILE = os.path.join(LOG_DIR, "scam_reports.json")
COOLDOWN_HOURS = 24

# ---------------- UTILS ----------------
def ensure_logs():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

def load_logs():
    ensure_logs()
    with open(LOG_FILE, "r") as f:
        return json.load(f)

def save_log(entry):
    logs = load_logs()
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)

def cooldown_check(number):
    logs = load_logs()
    now = time.time()
    for log in reversed(logs):
        if log["number"] == number:
            elapsed = (now - log["timestamp"]) / 3600
            if elapsed < COOLDOWN_HOURS:
                return COOLDOWN_HOURS - elapsed
    return 0

# ---------------- INPUT SANITIZATION ----------------
def sanitize_input(text, max_len=500):
    return text.strip()[:max_len]

# ---------------- TEMPLATES ----------------
def generate_template(scam_type, number, country, description):
    templates = {
        "investment": f"""
Hello WhatsApp Support Team,

I am reporting a WhatsApp account involved in an investment/crypto scam.

Scammer Number: {number}
Country: {country}

Description:
{description}

Please review this account for policy violations.

Thank you.
""",
        "impersonation": f"""
Hello WhatsApp Support Team,

I am reporting a WhatsApp account impersonating a business or individual.

Scammer Number: {number}
Country: {country}

Description:
{description}

Kindly investigate and take appropriate action.

Thank you.
""",
        "romance": f"""
Hello WhatsApp Support Team,

I am reporting a WhatsApp account involved in a romance scam.

Scammer Number: {number}
Country: {country}

Description:
{description}

I believe this account violates WhatsApp safety policies.

Thank you.
""",
        "marketplace": f"""
Hello WhatsApp Support Team,

I am reporting a WhatsApp account committing marketplace fraud.

Scammer Number: {number}
Country: {country}

Description:
{description}

Please review this report.

Thank you.
""",
    }

    return templates.get(
        scam_type,
        f"""
Hello WhatsApp Support Team,

I am reporting a WhatsApp account involved in scam activity.

Scammer Number: {number}
Country: {country}

Description:
{description}

Please investigate.

Thank you.
"""
    )

# ---------------- ACTIONS ----------------
def open_gmail(report_text):
    params = {
        "to": SUPPORT_EMAIL,
        "subject": "Reporting a Scammer on WhatsApp",
        "body": report_text
    }
    query = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    webbrowser.open(f"mailto:?{query}")

def open_whatsapp_web():
    webbrowser.open("https://www.whatsapp.com/contact/?subject=messenger")

# ---------------- MAIN ----------------
def main():
    print("\n=== EXLONE WhatsApp Scammer Report Bot ===\n")

    number = sanitize_input(input("Scammer phone number (with country code): "), 20)
    country = sanitize_input(input("Your country: "), 50)

    remaining = cooldown_check(number)
    if remaining > 0:
        print(f"\n⚠️ Cooldown active. Wait {remaining:.1f} more hours before reporting this number again.")
        return

    print("\nScam Types:")
    print("1) Investment / Crypto")
    print("2) Impersonation")
    print("3) Romance")
    print("4) Marketplace Fraud")
    print("5) Other")

    scam_choice = input("Choose scam type (1-5): ").strip()
    scam_map = {
        "1": "investment",
        "2": "impersonation",
        "3": "romance",
        "4": "marketplace",
        "5": "other"
    }
    scam_type = scam_map.get(scam_choice, "other")

    description = sanitize_input(input("\nBrief description of the scam:\n> "), 400)

    report = generate_template(scam_type, number, country, description)

    print("\n---------------- REPORT PREVIEW ----------------\n")
    print(report)
    print("------------------------------------------------\n")

    choice = input("Choose action:\n1) Open Gmail draft\n2) Open WhatsApp Web report page\n3) Exit\n> ").strip()

    if choice == "1":
        open_gmail(report)
    elif choice == "2":
        open_whatsapp_web()

    save_log({
        "number": number,
        "scam_type": scam_type,
        "timestamp": time.time()
    })

    print("\n✅ Report saved locally in reports/scam_reports.json")

if __name__ == "__main__":
    main()
