from enum import IntFlag

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