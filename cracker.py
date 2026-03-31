import hashlib
from multiprocessing import Pool, cpu_count

# === CONFIG ===
salt = b"your_salt_here"
target = "your_hash_here"
iterations = 2000000

wordlist_file = "/usr/share/wordlists/rockyou.txt"

# === MUTATION RULES ===
def generate_candidates(word):
    return [
        word,
        word + "123",
        word + "1234",
        word + "2024",
        word + "2025",
        word.capitalize(),
        word.upper(),
        word + "!",
        word + "@123",
        "ciph_" + word,
        word + "_backup",
        "backup_" + word
    ]

# === CHECK FUNCTION ===
def check_word(word):
    word = word.strip()
    if not word:
        return None

    for candidate in generate_candidates(word):
        dk = hashlib.pbkdf2_hmac(
            "sha512",
            candidate.encode(),
            salt,
            iterations
        )

        if dk.hex() == target:
            return candidate

    return None

# === MAIN ===
def main():
    print("[*] Loading wordlist...")

    with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
        words = f.readlines()

    print(f"[*] Loaded {len(words)} words")
    print(f"[*] Using {cpu_count()} CPU cores\n")

    with Pool(cpu_count()) as pool:
        for i, result in enumerate(pool.imap_unordered(check_word, words), 1):
            
            if i % 1000 == 0:
                print(f"[*] Tested {i} base words...")

            if result:
                print("\n[+] PASSWORD FOUND:", result)
                print(f"[+] FLAG: ciph{{{result}}}")
                pool.terminate()
                return

    print("\n[-] Password not found.")

if __name__ == "__main__":
    main()
