# 🔑 Symmetric vs Asymmetric Encryption

Cryptographic systems use keys to encrypt and decrypt data. These keys can be **shared** (symmetric) or **separate** (asymmetric).

---

## 🔐 Symmetric Encryption

- Same key is used to **encrypt and decrypt**
- Fast and efficient for large data
- Requires a **secure key exchange** method

| Algorithm | Description        |
|-----------|--------------------|
| AES       | Advanced Encryption Standard (modern standard) |
| DES       | Deprecated symmetric cipher |
| RC4       | Stream cipher, not recommended now |

### 🔁 Example
```bash
Plaintext --> [Encrypt w/ Key] --> Ciphertext
Ciphertext --> [Decrypt w/ Key] --> Plaintext
```

## 🔏 Asymmetric Encryption

- Uses public key (to encrypt) and private key (to decrypt)

- Solves the key exchange problem

- Slower, but ideal for secure key sharing and digital signatures

  | Algorithm | Use Case                          |
| --------- | --------------------------------- |
| RSA       | Secure email, TLS handshake       |
| ECC       | Lightweight crypto for mobile/IoT |
| ElGamal   | Digital signatures                |

## 🔐 Hybrid Approach in Real Life

- Modern systems use:

- Asymmetric encryption to exchange symmetric session keys

- Symmetric encryption to transfer data

🔒 Example: HTTPS uses asymmetric RSA or ECC to negotiate an AES session key.

## 🧠 Summary

| Feature  | Symmetric       | Asymmetric                      |
| -------- | --------------- | ------------------------------- |
| Keys     | Same            | Public/Private                  |
| Speed    | Fast            | Slower                          |
| Use Case | File encryption | Key exchange, digital signature |
