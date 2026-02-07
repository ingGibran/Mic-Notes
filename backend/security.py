
from passlib.hash import pbkdf2_sha256

# Convertir la contraseña a un hash
def hash_password(password: str) -> str:
    return pbkdf2_sha256.hash(password)

# Hashear contraseña y validar
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pbkdf2_sha256.verify(plain_password, hashed_password)

