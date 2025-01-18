```
___  ___            _            _____                  _    __________  ___  _____         _             
|  \/  |           | |          |_   _|                | |  | | ___ \  \/  | |_   _|       | |            
| .  . | ___  _ __ | | _____ _   _| |_   _ _ __   ___  | |  | | |_/ / .  . |   | | ___  ___| |_ ___ _ __  
| |\/| |/ _ \| '_ \| |/ / _ \ | | | | | | | '_ \ / _ \ | |/\| |  __/| |\/| |   | |/ _ \/ __| __/ _ \ '__| 
| |  | | (_) | | | |   <  __/ |_| | | |_| | |_) |  __/ \  /\  / |   | |  | |   | |  __/\__ \ ||  __/ |    
\_|  |_/\___/|_| |_|_|\_\___|\__, \_/\__, | .__/ \___|  \/  \/\_|   \_|  |_/   \_/\___||___/\__\___|_|    
                              __/ |   __/ | |                                                             
                             |___/   |___/|_|                                                             
```

MonkeyType WPM Tester 🚀

![](typerjif.gif)

This project automates typing on MonkeyType using Playwright and measures your Words Per Minute (WPM).

📌 Features

•	✅ Automatically launches MonkeyType in a browser.

•	✅ Simulates a typing test in headed mode (visible browser).

•	✅ Extracts and prints the Words Per Minute (WPM) score.

•	✅ Easy setup with Python, Poetry, and Playwright.

🛠️ Setup Instructions

1️⃣ Install Python3

Make sure Python 3 is installed before running the setup.
Check by running:

python3 --version

If not installed, download it from: Python Official Site

2️⃣ Run the Setup Script

Execute the following command to install dependencies:

source wpm_tester.sh

This script will:
1.	Set up a virtual environment using Python venv.
2.	Install Poetry dependencies.
3.	Install Playwright and required browsers.
4.	Run the typing test in a visible browser.

🚀 Running the Typing Test

After setup, the script will automatically start the typing test in headed mode.

It will extract your WPM score and display it in the terminal.

If you want to manually re-run the test, use:

`python3 test_monkeytype.py`

📊 Expected Output

At the end of the test, the script will print something like:

Typing Test Completed!
Your WPM: 72

🛠 Troubleshooting

🔹 “Command not found: source”

Ensure you’re running the script in a Unix-based shell (Linux/macOS).

For Windows PowerShell, use:

Set-ExecutionPolicy Unrestricted -Scope Process

`./wpm_tester.sh`

🔹 Playwright Not Installed?

Run the following manually:

`poetry run playwright install`

`poetry run playwright install-deps`

🔹 Error: Python Not Found?

Ensure python3 is installed and added to your system path.

💡 Notes

•	The script runs in headed mode so you can see the browser in action.

•	If you want to run it in headless mode, modify the test_monkeytype.py script:

browser = p.chromium.launch(headless=True)

📝 Author: Ian Allheim

Built with ❤️ using Python, Poetry, and Playwright.

🚀 Happy Typing! 🚀