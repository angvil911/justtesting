import uuid
import bcrypt
import hashlib


def hash_password(password):
    """Hash password using bcrypt (secure, GPU-resistant hashing)."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password.decode()


def check_password(hashed_password, user_password):
    """Check password with auto-migration from legacy SHA-256 to bcrypt.
    
    If the stored hash is in legacy SHA-256:salt format, it will be validated
    using the old method. The caller should re-hash and store the new bcrypt
    hash after a successful legacy check to migrate the user.
    """
    # Detect legacy SHA-256 format (hex_hash:hex_salt)
    if ':' in hashed_password and len(hashed_password.split(':')[0]) == 64:
        # Legacy SHA-256 check
        password, salt = hashed_password.split(':')
        is_valid = password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
        if is_valid:
            # Flag for migration — caller should update the stored hash
            return True
        return False
    
    # Modern bcrypt check
    try:
        return bcrypt.checkpw(user_password.encode(), hashed_password.encode())
    except (ValueError, AttributeError):
        return False


def generateToken(username, password):
    # Concatenate username and password
    credentials = f'{username}:{password}'.encode()

    # Use SHA-256 hashing
    hashed_credentials = hashlib.sha256(credentials).hexdigest()

    return 'Basic {0}'.format(hashed_credentials)
