import bcrypt


def hash_password(password: bytes) -> bytes:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed
