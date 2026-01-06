import yaml
import logging
logger = logging.getLogger(__name__)

def get_data_path():
    config = load_config()
    return config['data_paths']
def get_columns():
    config = load_config()
    return config['columns']
    

def load_config():
    try:
        with open("config.yaml", 'r') as f:
            config = yaml.safe_load(f)
        return config
    except Exception as e:
        logger.error(f'Error loading configuration: {e}')
        return {}


get_data_path()