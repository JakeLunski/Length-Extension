# Length-Extension
This is a project that conducts a length extension attack.

Description
------------
In this project, I successfully implemented a length extension attack to modify an existing URL and append an additional command without knowing the secret key. The new token was generated based on the updated message, and the server accepted the modified URL. I learned a lot about cryptographic vulnerabilities and how to exploit the structure of hash functions like SHA-256. This project deepened my understanding of how attacks can leverage weaknesses in commonly used algorithms.


Challenges Faced
----------------
Understanding Padding: The most challenging part of the project was understanding how padding works in the SHA-256 algorithm and ensuring it was correctly calculated based on the message length and the secret key length.
Maintaining Hash State: It was important to initialize the hash with the correct internal state derived from the original token, so the new token would be valid after appending the UnlockSafes command.


The main parts of the script are as follows:

    URL Class:
        The URL class was used to parse the URL into the prefix, token, and suffix. This class allowed me to easily manipulate and print the modified URL after performing the length extension attack.

    Token Validation:
        I validated the token to ensure it was a 64-character hexadecimal string, which is necessary for SHA-256 hash values. If the token was invalid, the program would terminate.

    Padding Calculation:
        I used the padding() function from pysha256 to calculate the padding for the original message, based on its length (including the secret). The padding ensures that the total message length is a multiple of 64 bytes, as required by the SHA-256 algorithm.

    Modifying the Hash:
        The sha256() function allowed me to initialize the hash with the original token's internal state and append the new command. The update() function added the new command (UnlockSafes) to the hash.

    Output:
        The modified URL, with the new token and appended command, was printed for use in interacting with the API server.
        

