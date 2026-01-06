"""Compute SHA-256 hash of a bytes literal and print the hex digest."""

from cryptography.hazmat.primitives import hashes

DATA = b"DevOps and Docker Security"

digest = hashes.Hash(hashes.SHA256())
digest.update(DATA)
hash_value = digest.finalize()

print("SHA-256 Hash:", hash_value.hex())
