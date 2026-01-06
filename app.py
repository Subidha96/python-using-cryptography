from cryptography.hazmat.primitives import hashes

data = b"DevOps and Docker Security"
digest = hashes.Hash(hashes.SHA256())
digest.update(data)
hash_value = digest.finalize()

print("SHA-256 Hash:", hash_value.hex())

