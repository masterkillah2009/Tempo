# Tempo 🎵🔐

Tempo is a **proof-of-concept encryption tool** that derives cryptographic keys from audio files (music) to encrypt and decrypt data.  
It explores unconventional key derivation, cryptography fundamentals, and how deterministic inputs affect encryption systems.

> ⚠️ **Important:** Tempo is **experimental** and **not intended for real-world secure use**. It exists for learning, exploration, and demonstration only.

---

## Concept Overview

Tempo uses a song (audio file) as the *source of entropy* for encryption.

High-level flow:

1. Load an audio file
2. Normalize it (mono, fixed sample rate)
3. Extract raw audio bytes
4. Hash the bytes using SHA‑256
5. Convert the hash into a Fernet-compatible key
6. Encrypt or decrypt a file using that key

If the **exact same song** is provided during decryption, the original file can be recovered.  
If the song differs even slightly, decryption fails.

---

## How It Works (Technical Breakdown)

### 1. Audio Processing
- Audio is loaded using `pydub`
- Converted to:
  - Mono channel
  - 44.1 kHz sample rate
- Raw PCM audio data is extracted

This normalization ensures consistent hashing across environments *as much as possible*.

### 2. Key Derivation
- SHA‑256 hashes the raw audio bytes
- Output is a 32‑byte digest
- Digest is Base64 URL‑safe encoded
- Resulting key matches Fernet’s required format

```text
Audio → Raw Bytes → SHA‑256 → Base64 → Fernet Key
````

### 3. Encryption / Decryption

* Uses `cryptography.fernet`
* Files are encrypted symmetrically
* Same derived key is required for decryption

---

## Features

* Encrypt files using audio-derived keys
* Decrypt files if the correct song is provided
* Deterministic encryption based on media input
* Simple terminal-based interface
* Minimal dependencies
* Clear demonstration of cryptographic workflows

---

## Requirements

### Software

* Python 3.x
* FFmpeg (required by pydub)

### Python Libraries

* `cryptography`
* `pydub`

### Install Dependencies

```bash
pip install cryptography pydub
```

Install FFmpeg:

**Linux**

```bash
sudo apt update
sudo apt install ffmpeg
sudo apt pyaudioop-lts 
```
NOTICE: The latest versions of Python do not support pyaudioop so use audioop-lts

**macOS**

```bash
brew install ffmpeg
```

**Windows**

* Download FFmpeg and add it to PATH

---

## Usage

Run the program:

```bash
python tempo.py
```

You’ll see a menu:

```text
TEMPO
1. Encrypt file
2. Decrypt file
3. Quit
```

### Encrypting a File

* Provide the file you want to encrypt
* Provide a song file (e.g. `.mp3`, `.wav`)
* Output is an encrypted file

### Decrypting a File

* Provide the encrypted file
* Provide the **same song used for encryption**
* Output is the decrypted original file

---

## Limitations & Security Warnings

Tempo is **not secure** for real-world use. Known limitations include:

* Deterministic keys (no salt or randomness)
* Extremely sensitive to audio changes
* No authentication or integrity checks beyond Fernet defaults
* No key stretching or password-hardening
* Vulnerable to replay and known-input attacks

This project **should not** be used to protect sensitive data.

---

## Learning Outcomes

This project demonstrates:

* Cryptographic hashing (SHA‑256)
* Symmetric encryption (Fernet)
* Key derivation concepts
* Determinism vs entropy in cryptography
* File handling in Python (binary I/O)
* Media processing for non-media applications
* Security trade-offs in unconventional designs

It’s designed to show **how cryptographic systems work**, not to replace them.

---

## Use Case

Tempo is ideal as:

* A learning project
* A cryptography proof-of-concept
* A portfolio demo
* An experiment in unconventional security ideas

---
