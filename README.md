# Insta AntiDoom

This repository contains a simple tool to list all Instagram accounts that you follow but which do not follow you back.

## Requirements
- Python 3.8+
- [instaloader](https://instaloader.github.io/) (installed automatically via `requirements.txt`)

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python find_unfollowers.py -u YOUR_USERNAME -p YOUR_PASSWORD
```

If you prefer not to pass the password via command line, set it in the environment variable `INSTAGRAM_PASS` and omit `-p`.

Accounts with two-factor authentication are supported. When required, the script prompts for the verification code after the password is submitted.

The script will output a list of usernames, one per line, representing accounts you follow that do not follow you back.
