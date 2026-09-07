# HTTP Automation Bot (V2)

> A lightweight, zero-browser Python terminal automation tool designed specifically for Termux and Linux environments.

[![Python Version](https://img.shields.io/badge/python-3.x-bsue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

* **Zero-Browser Footprint:** Built entirely on standard HTTP requests using the `requests` library--no heavy Selenium or WebDriver dependencies required.
* **Termux Optimized TUI:** Clean, responsive terminal user interface designed for mobile and desktop terminal screens.
* **Flexible Scheduling:** Configure exact time intervals (minimum 1 minute) and set custom delays before execution starts.
* **Flexible Run Modes:** Run for a specific number of iterations or set it to an indefinite loop.
* **Lightweight & Fast:** Minimal resource usage, perfect for running background tasks on mobile devices or servers.

---

## Termux Installation Guide

Follow these steps to set up and run the bot directly on your Android device using Termux:

1. **Update and Upgrade apt:**
    ```bash
    apt update && apt upgrade -y
    ```
2. **Update Termux packages:**
    ```bash
    pkg update && pkg upgrade -y
    ```
3. **Install Git, Python, and Pip:**
    ```bash
    pkg install git python
    ```
4. **Clone the repository:**
    ```bash
    git clone https://github.com/stereo-madness1/http-automation-bot.git
    ```
5. **Navigate into the project directory:**
    ```bash
    cd http-automation-bot
    ```
6. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
7. **Run the automation bot:**
    ```bash
    python main.py
    ```

---

## Usage Guide

When you launch the script, the interactive terminal interface will guide you through the configuration:
1. **Website URL:** Enter your target URL (e.g, example.com).
2. **Interval:** Set the delay between requests in minutes (minimum 1 minute).
3. **Total Runs:** Enter a specific number of iterations, or type `inf` for an indefinite loop.
4. **Execution Mode:** Choose to start immediately (`now`) or add a delayed start timer (`delay`).

---

## Requirements

* Python 3.7+
* `requests`
* `urllib3`
* `certifi`
* `charset-normalizer`
* `idna`

---

## Author

* **~evin**
* **@stereo_madness1** (Instagram)

---

## License

This project is open-source and available under the [MIT License](LICENSE).
