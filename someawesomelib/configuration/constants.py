from enum import Enum


class EnvProfile(Enum):
    PRODUCTION = "prod"
    STAGING = "stage"
    DEVELOPMENT = "dev"

    @classmethod
    def has(cls, key):
        return key in cls.__members__
