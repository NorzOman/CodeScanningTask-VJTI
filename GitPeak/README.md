
# GitPeak - Code Scanner Documentation

## 1. Overview

**GitPeak** is a command-line tool designed to scan source code files for potential security vulnerabilities, secrets, and sensitive data leaks. It leverages the power of Google's Gemini AI model to analyze code and provide actionable security reports.

The tool can scan a single file or recursively scan all supported code files within a directory, making it a versatile utility for developers and security analysts. It provides user-friendly feedback, including a loading spinner, to ensure the user knows the scan is in progress.

### Demo Video

https://github.com/user-attachments/assets/b90613b5-e085-4052-ba08-af0565556f36

### Key Features

*   **AI-Powered Scanning:** Utilizes the Google Gemini model for intelligent code analysis.
*   **Secrets & Vulnerability Detection:** Identifies hardcoded secrets, API keys, and common coding vulnerabilities.
*   **File and Directory Scanning:** Accepts both a single file path and a directory path for comprehensive scanning.
*   **Multi-Language Support:** Recognizes common code file extensions (e.g., `.py`, `.js`, `.java`, `.go`, etc.).
*   **User-Friendly Output:** Presents findings in a clear, structured format specifying the line, issue, and suggested fix.
*   **Interactive Feedback:** Displays a banner and a loading animation during the scanning process.

## 2. Requirements

*   Python 3.x
*   The `google-generativeai` Python library.

## 3. Installation

1.  Save the script to a file, for example, `gitpeak.py`.
2.  Install the required Python package using pip:
    ```bash
    pip install -q -U google-genai
    ```

## 4. Configuration

The script requires a Google AI API key to function.

The script already contains a hardcoded key that was discovered by the tool GitBully. This means its set to go directly no need to configure keys in environment.

## 5. Usage

Run the script from your command line, providing the path to the file or folder you wish to scan as an argument.

### Syntax

```bash
python gitpeak.py <target_path>
```

*   `target_path`: The mandatory path to the source code file or directory to scan.

### Examples

*   **Scan a single file:**
    ```bash
    python gitpeak.py my_vulnerable_script.py
    ```

*   **Scan all supported files in a directory:**
    ```bash
    python gitpeak.py /path/to/my/project/
    ```

*   **Scan the current directory:**
    ```bash
    python gitpeak.py .
    ```
