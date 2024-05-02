from main import accounts
import random

def generate_unique_IBAN():
    iban = "TB"
    id = str(random.randint(1,9999)).zfill(4)
    iban += id
    if iban not in accounts:
        return iban