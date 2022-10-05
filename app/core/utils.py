from base64 import b64encode
from hashlib import sha256
from hmac import HMAC
from urllib.parse import parse_qsl, urlencode

from app.config import config
from app.internal.schemes import UserModel


def check_vk_sign(vk_params: str) -> bool:
    if config.TEST_MODE:
        return True

    query = dict(parse_qsl(vk_params, keep_blank_values=True))

    if not query.get("sign"):
        return False

    vk_subset = sorted(filter(lambda key: key.startswith("vk_"), query))

    if not vk_subset:
        return False

    ordered = {k: query[k] for k in vk_subset}

    hash_code = b64encode(
        HMAC(
            config.BACKEND_VK_SECRET_KEY.encode(),
            urlencode(ordered, doseq=True).encode(),
            sha256,
        ).digest()
    ).decode("utf-8")

    if hash_code[-1] == "=":
        hash_code = hash_code[:-1]

    fixed_hash = hash_code.replace("+", "-").replace("/", "_")
    return query.get("sign") == fixed_hash


def check_user(user: UserModel, vk_params: str) -> bool:
    if config.TEST_MODE:
        return True

    query = dict(parse_qsl(vk_params, keep_blank_values=True))
    vk_subset = sorted(filter(lambda key: key.startswith("vk_"), query))
    ordered = {k: query[k] for k in vk_subset}

    return ordered["vk_user_id"] == str(user.vk_user_id)
