import yaml
import logging


CONFIG_FILE = "config.yaml"
logger = logging.getLogger(__name__)

def get_data_path():
    config = load_config()
    return config.get("raw_data_path")
    

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        logger.error(f'Error loading configuration: {e}')
        return {}
