from src.text_analysis.constants import *
from src.text_analysis.utils.common import read_yaml_file, create_directories
from src.text_analysis.entity.config_entity import TextExtractionConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH):

        self.config = read_yaml_file(config_filepath)

        create_directories([self.config.artifacts_root])


    def get_text_extraction_config(self) -> TextExtractionConfig:
        config = self.config.text_extraction

        create_directories([config.root_dir])

        data_ingestion_config = TextExtractionConfig(
            root_dir=config.root_dir,
            input_file=config.input_file,
            destination_folder=config.destination_folder
        )

        return data_ingestion_config