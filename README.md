![Python](https://img.shields.io/badge/python-3.9+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Termux%20%7C%20Linux%20%7C%20Windows-lightgrey)
![Status](https://img.shields.io/badge/status-stable-success)

# EXLONE — WhatsApp Scammer Report Bot

A **legitimate, policy-compliant Python tool** that helps users report **WhatsApp scammer numbers** through **official WhatsApp channels**.

This project **does NOT auto-ban accounts**, **does NOT spam**, and **does NOT bypass WhatsApp systems**.  
All reports are **manually submitted by the user**, which is how real enforcement happens.

---

## ✨ Features

- Collects scammer details (number, scam type, description, country)
- Generates **professional abuse reports**
- Multiple **scam-type templates**:
  - Investment / Crypto
  - Impersonation
  - Romance scams
  - Marketplace fraud
  - Other
- Opens **Gmail draft** addressed to WhatsApp Support (manual send)
- Opens **WhatsApp Web reporting page** (manual submission)
- Local **JSON logging** for record keeping
- **Cooldown protection (24 hours)** to prevent spam abuse
- Works on **Termux, Linux, Windows, macOS**
- **MIT Licensed**

---

## 🚫 What This Tool Does NOT Do

- ❌ No automatic bans
- ❌ No mass reporting
- ❌ No forced enforcement
- ❌ No WhatsApp impersonation

> WhatsApp reviews reports manually. This tool helps you submit them **correctly and safely**.

---

## 📧 Official Reporting Channel

- **Email:** support@whatsapp.com  
- **WhatsApp Web:** https://www.whatsapp.com/contact/?subject=messenger

---

## 🧰 Requirements

- Python **3.9 or newer**
- Git (for cloning)
- Internet connection (to submit reports)

---

## 📦 Installation (Termux / Linux / macOS / Windows)

```bash
git clone https://github.com/exloneshop-source/exlone-whatsapp-scam-report-bot.git
cd exlone-whatsapp-scam-report-bot
python whatsapp_scam_report_bot.py
