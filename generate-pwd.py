from passlib.hash import pbkdf2_sha512

# Ask user for password
plain_password = input("Enter plain password: ")

# Generate encrypted password
encrypted_password = pbkdf2_sha512.using(rounds=600000).hash(plain_password)

# Save to file
with open("generated-pwd.txt", "w") as f:
    f.write(f"Plain Password: {plain_password}\n")
    f.write(f"Encrypted Password: {encrypted_password}\n")

print("Password encrypted successfully.")
print("Encrypted Password:", encrypted_password)

print("Saved to generated-pwd.txt")
