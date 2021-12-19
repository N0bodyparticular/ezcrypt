This is a simple encryption/decryption utility written in python.


To generate a key:
```
./ezcrypt.py
Select operation:
k - Generate a new key for encryption.
e - Encrypt a file and optionally create a new key file.
d - Decrypt a file using a key.
-> k
Enter key name: example.key
The key is generated
```

To encrypt a file:
```
./ezcrypt.py
Select operation:
k - Generate a new key for encryption.
e - Encrypt a file and optionally create a new key file.
d - Decrypt a file using a key.
-> e
Enter plaintext file name: example.txt
Enter key file name (leave blank to generate new): example.key
The file is encrypted.
```

To decrypt a file:
```
./ezcrypt.py
Select operation:
k - Generate a new key for encryption.
e - Encrypt a file and optionally create a new key file.
d - Decrypt a file using a key.
-> d
Enter encrypted file name: secret.txt
Enter key file name: secret.txt.key
The file is decrypted.
```
