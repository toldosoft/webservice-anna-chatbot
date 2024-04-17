# Encryption and Decryption Service

## Overview
This Python script provides a secure method for encrypting and decrypting data using DES3 encryption. It is designed to send encrypted data to a server and process the encrypted response.

## Features
- **DES3 Encryption**: Utilizes Triple DES encryption for securing data.
- **Data Transmission**: Sends encrypted data over HTTP POST requests.
- **Response Handling**: Receives and decrypts data from server responses.

## Requirements
- Python 3.x
- `requests` library
- `pycryptodome` library

## Setup
1. **Install Python Dependencies**:
   Ensure Python 3.x is installed on your system. Install the necessary Python libraries using pip:
   ```bash
   pip install requests pycryptodome
   ```

2. **Configuration**:
   - Set the server's URL and the encryption/decryption keys in the script.
   - Configure additional parameters such as user ID, user name, and action according to your needs.

## Usage
Run the script to encrypt data, send it to the server, and decrypt the response:
```bash
python app.py
```

## Example of Encrypted Communication
- Data is encrypted using a base64 encoded key and IV before being sent.
- Server responses are expected to be encrypted and require decryption using the specified decryption key and a new IV.

## Contributing
Contributions to this project are welcome. Ensure that any pull requests or contributions adhere to the existing coding style and add relevant tests for new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
