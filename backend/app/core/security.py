"""Security utilities (authentication, authorization)."""

# Placeholder per future implementazioni di autenticazione JWT
# e gestione password con bcrypt

def get_password_hash(password: str) -> str:
    """Hash a password."""
    # TODO: Implementare con passlib
    return password


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash."""
    # TODO: Implementare con passlib
    return plain_password == hashed_password
