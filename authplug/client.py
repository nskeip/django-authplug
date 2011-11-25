from models import HashKey

def sign(params, salt):
    return HashKey.sign(params, salt)