import bcrypt


def hash_password(password: bytes) -> bytes:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)
    return hashed


def verify_password(password: bytes, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(password, hashed_password)
