import hashlib
import logging
import random
import uuid
from fastapi import APIRouter, Depends

from src.core.api.dto import UserRegisterRequest, UserRegisterResponse
from src.core.api.resolvers import get_cache
from src.core.cache.redis import Redis

LOGGER = logging.getLogger(__name__)

login_router = APIRouter()


@login_router.post("/register")
async def register(
    user_register_request: UserRegisterRequest, cache: Redis = Depends(get_cache)
):
    """
    Register a user with a phone number. This will generate an OTP and send it
    to the user's phone number.

    :param user_register_request: UserRegisterRequest
    :param cache: Redis

    :return: UserRegisterResponse
    """
    LOGGER.info(
        f"Registering user with phone number: {user_register_request.phone_number}"
    )
    user_id = str(uuid.uuid4())
    otp = _generate_otp()
    LOGGER.info(f"Generated OTP: {otp}")

    cache.set(user_register_request.phone_number, otp, expiration=300)
    LOGGER.info("OTP stored in cache")

    # send_otp(user_register_request.phone_number, otp)
    LOGGER.info("OTP sent to the user")

    return UserRegisterResponse(
        phone_number=user_register_request.phone_number,
        user_id=user_id,
        message="OTP sent successfully",
        otp=otp,
    )


def _generate_otp():
    """
    Generate a random 4 digit number.
    """
    # !TODO: This will be replaced with a proper OTP generation library.
    input_uuid = str(uuid.uuid4())
    uuid_bytes = input_uuid.encode("utf-8")
    # Create a hash object using SHA-256
    hash_object = hashlib.sha256(uuid_bytes)
    # Get the hexadecimal representation of the hash
    hex_hash = hash_object.hexdigest()
    # Take the first 4 characters
    return str(int(hex_hash[:4], 16) % 9000 + 1000)
