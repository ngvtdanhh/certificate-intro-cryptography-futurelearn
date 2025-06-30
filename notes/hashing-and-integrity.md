# 🛡️ Hashing and Integrity

Hash functions play a vital role in verifying that data has not been changed.

---

## 🔁 What Is a Hash Function?

A hash function:
- Takes input of any size
- Produces a fixed-length digest
- Is deterministic (same input → same output)
- Is **one-way**: infeasible to reverse

---

## 🔐 Properties of Secure Hash Functions

- ✅ **Pre-image resistance**: Hard to find input from hash
- ✅ **Second pre-image resistance**: Hard to find another input with same hash
- ✅ **Collision resistance**: Hard to find two different inputs with same hash

---

## 🔍 Common Algorithms

| Algorithm | Notes |
|-----------|-------|
| SHA-256   | Most common, used in TLS, Bitcoin, etc. |
| SHA-1     | Deprecated (collision found) |
| MD5       | Broken, still found in legacy systems |

---

## ✉️ Use Cases

- 📦 File integrity verification (e.g., SHA256SUM)
- 🪪 Password storage (with salt & hash)
- ✍️ Digital signatures (hash the data first)
- 🧮 Blockchain (link blocks via hash pointers)

---

## ⚠️ Hash ≠ Encryption

- Hashing is **irreversible**
- Encryption is **reversible with a key**
