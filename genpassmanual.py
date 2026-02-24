import bcrypt

hashed = bcrypt.hashpw("admin".encode(), bcrypt.gensalt()).decode()
print(hashed)