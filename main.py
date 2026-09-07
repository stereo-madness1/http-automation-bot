import time
from datetime import datetime, timedelta
import requests
import sys
import shutil

# Advanced ANSI Color Palette for Termux
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
PRIMARY = "\033[38;5;39m"    # Bright Cyan
SUCCESS = "\033[38;5;46m"    # Bright Green
WARNING = "\033[38;5;220m"   # Bright Yellow
DANGER = "\033[38;5;196m"    # Bright Red
ACCENT = "\033[38;5;201m"    # Bright Magenta
MUTED = "\033[38;5;242m"     # Slate Gray

def get_terminal_width():
    try:
        columns, _ = shutil.get_terminal_size(fallback=(80, 24))
 except Exception:
        columns = 80
    return min(columns, 60)  # Cap width for optimal mobile/Termux readability

def clear_screen():
    print("\033[H\033[J", end="")

def print_banner():
    clear_screen()
    width = get_terminal_width()
    line = "═" * width
    
    print(f"{PRIMARY}{line}{RESET}")
    print(f"{BOLD}{ACCENT}       HTTP AUTOMATION BOT         {RESET}".center(wi>
    print(f"{DIM}           Made by stereo_madness1            {RESET}".center(>
    print(f"{PRIMARY}{line}{RESET}\n")
def get_user_inputs():
    print_banner()
    width = get_terminal_width()
    
    print(f"{WARNING} [ TARGET CONFIGURATION ]{RESET}")
    url = input(f"   {PRIMARY}Website URL (e.g., example.com):{RESET} ").strip()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    print(f"\n{WARNING} [ TIMING & FREQUENCY ]{RESET}")
    while True:
        try:
            interval_min = float(input(f"   {PRIMARY}Interval in minutes (Min: >
            if interval_min < 1:
                print(f"   {DANGER}[-] Error: Interval cannot be below 1 minute>
                continue
            break
        except ValueError:
            print(f"   {DANGER}[-] Please enter a valid number.{RESET}")
 interval_seconds = interval_min * 60

    count_input = input(f"   {PRIMARY}Total runs (Enter count or 'inf'):{RESET}>
    if count_input == 'inf' or count_input == '':
        total_runs = float('inf')
    else:
        try:
            total_runs = int(count_input)
        except ValueError:
            print(f"   {WARNING}[!] Invalid input. Defaulting to indefinite.{RE>
            total_runs = float('inf')

    print(f"\n{WARNING} [ SCHEDULE OPTIONS ]{RESET}")
    future_input = input(f"   {PRIMARY}Execution mode (now / delay):{RESET} ").>
    start_delay_seconds = 0
except ValueError:
            print(f"   {DANGER}[!] Invalid delay. Starting immediately.{RESET}")

    return url, interval_seconds, total_runs, start_delay_seconds

def main():
    url, interval, total_runs, start_delay = get_user_inputs()
    
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Android; Mobile; rv:109.0) Gecko/110.0 Fire>
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=>
    })

    print_banner()
    width = get_terminal_width()
     if start_delay > 0:
        target_start_time = datetime.now() + timedelta(seconds=start_delay)
        print(f"{WARNING}[⏰] Scheduled! Task will launch at {target_start_time>
        time.sleep(start_delay)

    mode_text = 'Indefinite Loop' if total_runs == float('inf') else f'{int(tot>
    
    print(f"{SUCCESS}──────────────────────────────────────────────{RESET}")
    print(f"{SUCCESS} STATUS: ACTIVE & RUNNING{RESET}")
    print(f" Target   : {url}")
    print(f" Interval : {interval / 60} min(s)")
    print(f" Mode     : {mode_text}")
    print(f"{SUCCESS}──────────────────────────────────────────────{RESET}\n")

    run_count = 0
    success_count = 0
    fail_count = 0

    try:
        while run_count < total_runs:
            run_count += 1
            timestamp = datetime.now().strftime('%H:%M:%S')
            run_label = f"#{run_count}" if total_runs != float('inf') else f"#{>

            print(f"{PRIMARY}[{timestamp}] Dispatching Request {run_label}{RESE>

            try:
                start_t = time.time()
                response = session.get(url, timeout=20)
                elapsed = time.time() - start_t

                if response.status_code == 200:
                    status_str = f"{SUCCESS}200 OK{RESET}"
                     success_count += 1

                print(f" ├── Status : {status_str}")
                print(f" ├── Latency: {PRIMARY}{elapsed:.2f}s{RESET}")
                print(f" └── Size   : {MUTED}{len(response.content)} bytes{RESE>
            except requests.exceptions.RequestException as e:
                fail_count += 1
                print(f" └── {DANGER}Failed : {e}{RESET}")

            print(f" {DIM}📊 Stats -> Success: {success_count} | Failed: {fail_>

            if run_count >= total_runs:
                print(f"\n{SUCCESS}[✔] Target run count completed successfully.>
                break

            print(f" {ACCENT}⏳ Cooling down for {interval / 60} min(s)...{RESE>
            time.sleep(interval)
             except KeyboardInterrupt:
        print(f"\n\n{DANGER}[!] Process terminated by user. Exiting safely.{RES>
        sys.exit(0)

if __name__ == "__main__":
    main() 




