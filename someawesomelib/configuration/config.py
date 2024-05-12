import logging
import os
from os.path import exists
from omegaconf import OmegaConf

from someawesomelib.configuration.constants import EnvProfile

logger = logging.getLogger(__name__)


def __load_if_exists(env_profile: EnvProfile, config_path: str):
    default_config_file = "settings.yaml"
    default_config_path = os.path.join(config_path, default_config_file)
    logger.debug("Loading default configuration", extra={"file": default_config_path})
    default_config = OmegaConf.load(default_config_path)

    env_config_file = f"settings_{env_profile.value}.yaml" if env_profile else None
    env_config_path = os.path.join(config_path, env_config_file) if env_config_file else None
    if exists(env_config_path):
        logger.debug("Loading env configuration", extra={"file": env_config_path})
        env_config = OmegaConf.load(default_config_path)
        config = OmegaConf.merge(default_config, env_config)
        return config
    else:
        logger.debug("Configuration file does not exists", extra={"file": env_config_path})
        return default_config


def __init_settings():
    env_profiles = os.getenv("ENV_PROFILES")
    env_profiles = env_profiles.split(",") if env_profiles else []
    env_profiles = [EnvProfile(profile.strip()) for profile in env_profiles if EnvProfile.has(profile.strip())]

    for env_profile in env_profiles:
        config = OmegaConf.merge(config, __load_if_exists(env_profile, config_path))
    conf = OmegaConf.merge(
        __load_if_exists(env_profiles),
    )
    OmegaConf.set_readonly(conf, True)
    logger.debug("Loaded all configuration settings")
    return conf


settings = __init_settings()