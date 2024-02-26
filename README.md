# PyPortScanner

PyPortScanner is a Python 3.12.2 script that allows users to scan for open ports on a specified domain name or IP address.

## Overview

This script utilizes Python's `socket` module to establish TCP connections with various ports on the target host, determining whether they are open or closed. It provides a simple yet effective tool for network diagnostics and security assessments.

## Features

- Scan a single host for open ports within a specified range.
- Identify open ports and print the results to the console.
- Utilize DNS resolution to convert domain names to IP addresses for scanning.

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/sudo-user101/PyPortScanner.git
    ```

2. Navigate to the repository directory:

    ```bash
    cd PyPortScanner
    ```

3. Run the script and follow the on-screen instructions:

    ```bash
    python port_scanner.py
    ```

## Requirements

- Python 3.12.2
- Internet connection (for DNS resolution)

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

