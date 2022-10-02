import secrets
from base64 import b64encode
from hashlib import sha256
from hmac import HMAC
from urllib.parse import urlencode


def get_random_string(count_letters: int) -> str:
    return secrets.token_hex(count_letters)


def check_vk_sign(query: dict, secret: str) -> bool:
    if not query.get("sign"):
        return False

    vk_subset = sorted(filter(lambda key: key.startswith("vk_"), query))

    if not vk_subset:
        return False

    ordered = {k: query[k] for k in vk_subset}

    hash_code = b64encode(
        HMAC(secret.encode(), urlencode(ordered, doseq=True).encode(), sha256).digest()
    ).decode("utf-8")

    if hash_code[-1] == "=":
        hash_code = hash_code[:-1]

    fixed_hash = hash_code.replace("+", "-").replace("/", "_")
    return query.get("sign") == fixed_hash
