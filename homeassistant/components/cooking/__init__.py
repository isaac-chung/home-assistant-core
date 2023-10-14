"""Component to interact with cooking devices."""
import asyncio
import datetime as dt
from enum import IntFlag, StrEnum

from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity, EntityDescription
from homeassistant.helpers.entity_component import EntityComponent
from homeassistant.helpers.typing import ConfigType

_LOGGER = logging.getLogger(__name__)

DOMAIN = "cooking"
ENTITY_ID_FORMAT = DOMAIN + ".{}"

ATTR_COOKING_MODE = "cooking_mode"
ATTR_SUPPORT_REMOTE_START = "support_remote_start"
ATTR_SUPPORT_REMOTE_START = "support_remote_start"
ATTR_SUPPORTED_COOKING_MODES = "supported_cooking_modes"
ATTR_SUPPORTED_COOKING_STATUSES = "supported_cooking_statuses"

SCAN_INTERVAL = dt.timedelta(seconds=10)


class CookingEntityFeature(IntFlag):
    """Supported features of cooking entity.
    
    https://developer.amazon.com/en-US/docs/alexa/device-apis/cooking-property-schemas.html#cooking-mode
    """

    OFF = 1
    AIR_FRY = 2
    BAKE = 4
    BLANCH = 8
    BOIL = 16
    BREW = 32
    BROIL = 64
    CONVECTION_BAKE = 128
    CONVECTION_BROIL = 256
    CONVECTION_ROAST = 512
    CONVECTION_STEAM = 1024
    CURE = 2048
    DEFROST = 4096
    DEHYDRATE = 8192
    FERMENT = 16384
    FRY = 32768
    GRILL = 65536
    INCUBATE = 131072
    MELT = 262144
    MICROWAVE = 524288
    PRESET = 1048576
    PRESSURE = 2097152
    PROOF = 4194304
    REHEAT = 8388608
    ROAST = 16777216
    SAUTE = 33554432
    SEAR = 67108864
    SLOW_COOK = 134217728
    SMOKE = 268435456
    SOFTEN = 536870912
    SOUS_VIDE = 1073741824
    STEAM = 2147483648
    STIR_FRY = 4294967296
    TOAST = 8589934592
    WARM = 17179869184


class CookingStatus(StrEnum):
    """Possible cooking status.
    
    https://developer.amazon.com/en-US/docs/alexa/device-apis/cooking-property-schemas.html#cooking-status
    """
    COOKING = "COOKING"
    PREHEATING = "PREHEATING"
    PREHEATING_COMPLETED = "PREHEATING_COMPLETED"
    FOOD_TARGET_TEMPERATURE_REACHED = "FOOD_TARGET_TEMPERATURE_REACHED"
    COOKING_COMPLETED = "COOKING_COMPLETED"
    NOT_IN_USE = "NOT_IN_USE"
    READY = "READY"


class CookingDeviceClass(StrEnum):
    """Device class for media players."""

    MICROWAVE = "microwave"
    OVEN = "oven"
    SLOW_COOKER = "slow_cooker"


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Track states and offer events for cooking."""
    component = hass.data[DOMAIN] = EntityComponent[CookingEntity](
        _LOGGER, DOMAIN, hass, SCAN_INTERVAL
    )

    await component.async_setup(config)

    component.async_register_entity_service(
        SERVICE_UNLOCK, LOCK_SERVICE_SCHEMA, _async_unlock
    )
    component.async_register_entity_service(
        SERVICE_LOCK, LOCK_SERVICE_SCHEMA, _async_lock
    )
    component.async_register_entity_service(
        SERVICE_OPEN, LOCK_SERVICE_SCHEMA, _async_open, [LockEntityFeature.OPEN]
    )

    return True


class CookingEntity(Entity):
    """ABC for cooking entities."""
