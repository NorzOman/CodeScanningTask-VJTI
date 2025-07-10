
# Git Security : GitBully & GitPeak

Welcome! This repository hosts two distinct but complementary security tools designed to find secrets and vulnerabilities in codebases.

The primary focus of this repository is **GitBully 🐂**, a powerful, custom-built C++ tool designed to aggressively scan Git repositories for exposed secrets.

The second project is **GitPeak**, a Python script that uses Google's Gemini AI to perform intelligent code analysis for vulnerabilities.

<br>

---

## A little insight into one tool : GitBully

**GitBully was built from the ground up to be a simple, fast, and effective secret scanner.**

During its initial development, it immediately proved its value by discovering approximately **42 open MongoDB connection URLs** across various public repositories. This highlighted a common and critical security oversight that leaves sensitive data exposed.

> **Real-World Impact**
> One notable finding was an abandoned database connection for a startup. Although the company had migrated to a new database, the old credentials still provided access to a system containing contact information, emails, and other credentials.

The ultimate proof of concept, however, came from a different discovery. While scanning another public repository, **GitBully flagged a hardcoded Google Gemini API key.**

The key was not only valid but is the same one now hardcoded into **GitPeak** for demonstration purposes. It perfectly illustrates how easily secrets can be leaked and why automated tools like GitBully are essential.

<br>

---

## Project Spotlight: GitBully 🐂

GitBully is a no-nonsense, command-line security tool written entirely in C++. It "bullies" Git repositories into revealing their secrets by performing a comprehensive scan of both the current files and the project's entire history.

It is a powerful, standalone tool for any developer or security analyst's arsenal.

#### **Key Features:**

*   Scans for sensitive filenames and uses powerful regex patterns for content inspection.
*   Analyzes the full `git diff` history to find secrets that were committed and later removed.
*   Built to be fast and efficient, with intelligent filtering to avoid noise.

> ### **For full installation and usage instructions, see the GitBully documentation:**
> ### ➡️ **[GitBully/README.md](./GitBully/README.md)**

<br>

---

## Project Spotlight: GitPeak

GitPeak is a command-line scanner that leverages the Google Gemini AI model to analyze code. It can scan single files or entire directories to identify potential security vulnerabilities and provide AI-generated suggestions for fixes.

As a direct result of the findings from GitBully, the `GitPeak` script is pre-configured with the discovered API key. This allows you to run the tool immediately and see its AI scanning capabilities in action, all while serving as a live example of the very type of secret GitBully is designed to find.

> ### **For full installation and usage instructions, see the GitPeak documentation:**
> ### ➡️ **[GitPeak/README.md](./GitPeak/README.md)**
