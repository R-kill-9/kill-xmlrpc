# kill-xmlrpc

This Python script automates the brute force attack on XML-RPC endpoints, specifically targeting WordPress installations with the XML-RPC API enabled. The script iterates through a list of usernames and passwords (from wordlists) to find valid login credentials for the WordPress site.

## Features

- Reads usernames and passwords from wordlists.
- Sends XML-RPC requests to the target WordPress site's `xmlrpc.php` endpoint.
- Checks for valid login credentials by looking for a successful response (any response that doesn't indicate "Incorrect username or password").
- Reports when valid credentials are found.

## Requirements

- Python 3.x
- `requests` library (Install via `pip install requests`)

## Setup

1. Download or clone this repository.
2. Modify the following variables in the script to match your target environment:

   - `password_wordlist`: Path to the password wordlist.
   - `username_wordlist`: Path to the username wordlist.
   - `url`: The URL of the WordPress site's XML-RPC endpoint (e.g., `http://192.168.1.41/xmlrpc.php`).

3. Run the script.

## Usage

After setting up the variables, run the script using:

```bash
python3 xmlrpc.py
```

The script will attempt to find valid credentials by sending XML-RPC requests to the target URL with each combination of usernames and passwords from the wordlists.

## Example

```bash
python3 xmlrpc.py
```

Once the script completes, if valid credentials are found, it will output:
```bash
[+] Exploit completed successfully. Credentials obtained.
Username: {username}
Password: {password}
```

If no valid credentials are found:
```bash
[-] No valid credentials found. Try different wordlists or approaches.
```

## Notes

- Make sure the target WordPress site has XML-RPC enabled and is vulnerable to brute-force attacks.
- If you encounter issues with encoding or wordlist formats, ensure the wordlists are UTF-8 encoded.
- This script is intended for educational purposes and should be used responsibly and legally.

## License

This project is licensed under the MIT License - see the LICENSE file for details.




Created by: kill-9
