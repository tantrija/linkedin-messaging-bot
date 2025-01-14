### Getting Started with LinkedIn Messaging Bot

Here’s a simple **`README.md`** file to guide users on how to get started with your LinkedIn messaging bot:

---

# LinkedIn Messaging Bot

This LinkedIn bot automates sending personalized messages to your connections. Follow these steps to set up, configure, and run the bot.

## Prerequisites

1. **Install Python**:
   Ensure you have Python installed on your system. [Download Python](https://www.python.org/downloads/)

2. **Install Required Packages**:
   Install the necessary Python packages using `pip`:
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**:
   - Download the ChromeDriver version compatible with your Chrome browser: [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/)
   - Alternative: https://googlechromelabs.github.io/chrome-for-testing/#stable
   - Place the `chromedriver` binary in a known location, such as `/path/to/chromedriver`.

4. **LinkedIn Account**:
   - A LinkedIn account with connections you want to message.

---

## Setup

### 1. Clone the Repository
Download or clone this repository:
```bash
git clone https://github.com/tantrija/linkedin-messaging-bot.git
cd linkedin-messaging-bot
```

### 2. Create a Config File
Create a `config.json` file in the project directory with the following content:
```json
{
  "email": "your-linkedin-email@example.com",
  "password": "your-linkedin-password",
  "chromedriver_path": "/path/to/chromedriver"
}
```

- Replace `your-linkedin-email@example.com` with your LinkedIn email.
- Replace `your-linkedin-password` with your LinkedIn password.
- Update the `chromedriver_path` with the path to your ChromeDriver.

### 3. Update the Script
Ensure the script references the correct paths and loads the configuration dynamically:
- Script automatically loads values from `config.json`.

---

## Running the Bot

1. **Start the Bot**:
   Run the Python script:
   ```bash
   python linkedin_bot.py
   ```

2. **How It Works**:
   - Logs into LinkedIn using your credentials.
   - Scrolls through your connections to find those without prior messages.
   - Sends personalized messages using the provided template.

---

## Troubleshooting

### Common Issues
1. **`chromedriver` not found**:
   - Ensure the `chromedriver` path in `config.json` is correct.
   - Make sure the driver is executable:
     ```bash
     chmod +x /path/to/chromedriver
     ```

2. **Bot doesn't click buttons**:
   - LinkedIn may update their website layout. Update the XPaths in the script accordingly.

3. **Two-factor Authentication**:
   - Disable two-factor authentication temporarily or use session cookies for login.

---

## Disclaimer
Use this bot responsibly. Spamming or violating LinkedIn's terms of service can lead to account suspension.

---

This file can be saved as **`README.md`** or a similar **`getting_started.txt`** file for distribution.