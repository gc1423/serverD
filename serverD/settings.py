import os
import yaml
import importlib_resources


__all__ = ["load_config"]


ALL_CONFIGS = {}


def load_config(config_name: str):
    if config_name not in ALL_CONFIGS:
        config_file_name = config_name + ".yaml"
        config_resources = importlib_resources.files("serverD")/"configs"
        text = (config_resources/config_file_name).read_text()
        config = yaml.safe_load(text)
        ALL_CONFIGS[config_name] = config
    return ALL_CONFIGS[config_name]
