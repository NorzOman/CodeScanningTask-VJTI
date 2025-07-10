import argparse
import os
import time
import sys
import threading
from google.generativeai import GenerativeModel, configure

def print_banner():
    # just a cool ascii banner for the tool
    banner = r"""
   ____ _ _   ____            _    
  / ___(_) |_|  _ \ ___  __ _| | __
 | |  _| | __| |_) / _ \/ _` | |/ /
 | |_| | | |_|  __/  __/ (_| |   < 
  \____|_|\__|_|   \___|\__,_|_|\_\
        GitPeak - Code Scanner
    """
    print(banner)

def read_file_content(file_path):
    # reads file content, ignores errors because some files might be binary or have encoding issues
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def fake_loading(msg="Scanning with Gemini...", delay=0.2, duration=8):
    # just a simple fake loading spinner so user doesn't think script is dead
    spinner = ['|', '/', '-', '\\']
    t_end = time.time() + duration
    idx = 0
    sys.stdout.write(f"[*] {msg} ")
    sys.stdout.flush()
    while time.time() < t_end:
        sys.stdout.write(spinner[idx % len(spinner)])
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\b')
        idx += 1
    sys.stdout.write('\n')

def scan_with_gemini(code, filename=None):
    # setup Gemini with the api key (hardcoded, not best practice but makes it easy)
    configure(api_key="AIzaSyAAAv8rIeiOsQAdLqXHYx3U5ZZv8SPDawA") 
    # Fun Fact : Hardcoded API key that was discovered in a public repository by the GitBully Tool
    
    model = GenerativeModel("gemini-2.5-flash")
    prompt = (
        "You are a Git security checker. ONLY output in this format: "
        " \n --- LINE: <line number along with the line or the code block>  \n ISSUE: <short issue> \n FIX: <short fix> ---- \n"
        "No essays, no extra text. Just findings in that well format structure. "
        "Analyze the following code for any secrets, sensitive data leaks, and vulnerabilities. "
        "Do both static and dynamic analysis. Here is the code:\n\n"
        f"{code}"
    )
    # sleep a bit to avoid hitting rate limits or timeouts
    time.sleep(2)
    response = model.generate_content(prompt)
    return response.text

def get_code_files(target_path):
    # returns a list of code file paths
    code_files = []
    target_path = os.path.expanduser(target_path)  # expand ~ to /home/username
    if not os.path.exists(target_path):
        print(f"Error: Path does not exist: {target_path}")
        return []
    if os.path.isfile(target_path):
        code_files.append(target_path)
    elif os.path.isdir(target_path):
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.endswith(('.py', '.js', '.java', '.go', '.rb', '.php', '.c', '.cpp', '.cs', '.ts', '.sh')):
                    code_files.append(os.path.join(root, file))
    else:
        print(f"Error: Provided path is neither a file nor a directory: {target_path}")
        return []
    return code_files

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="GitSec: Scan code for secrets and vulnerabilities using Gemini.")
    parser.add_argument("target", help="Path to file or folder to scan")
    args = parser.parse_args()

    print("[*] Collecting code files...")
    code_files = get_code_files(args.target)
    if not code_files:
        print("No code files found to scan.")
        return

    for file_path in code_files:
        print(f"\n[*] Now scanning: {file_path} with Gemini")
        code = read_file_content(file_path)
        if not code.strip():
            print("File empty or unreadable, skipping.")
            continue

        # Start fake loading in a thread so it runs while Gemini is working cause gemini will take time to return
        loading_thread = threading.Thread(target=fake_loading)
        loading_thread.start()

        try:
            report = scan_with_gemini(code, filename=file_path)
        finally:
            loading_thread.join()

        print("\n--- Gemini Security Report ---\n")
        print(report)

if __name__ == "__main__":
    main()