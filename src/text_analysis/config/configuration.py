from src.text_analysis.constants import *
from src.text_analysis.utils.common import read_yaml_file, create_directories
from src.text_analysis.entity.config_entity import TextExtractionConfig, TextProcessingConfig, TextAnalysisConfig


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
    
    def get_text_processing_config(self) -> TextProcessingConfig:
        config = self.config.text_processing

        create_directories([config.root_dir])

        data_ingestion_config = TextProcessingConfig(
            root_dir=config.root_dir,
            stop_words_folder_path=config.stop_words_folder_path,
            processed_text_path=config.processed_text_path,
            merged_stop_words_path=config.merged_stop_words_path,
            extracted_files_folder_path=config.extracted_files_folder_path,
            destination_folder=config.destination_folder,
        )

        return data_ingestion_config
    
    def get_text_analysis_config(self) -> TextAnalysisConfig:
        config = self.config.text_analysis

        create_directories([config.root_dir])

        text_analysis_config = TextAnalysisConfig(
            root_dir=config.root_dir,
            processed_text_path=config.processed_text_path,
            positive_words_path=config.positive_words_path,
            negative_words_path=config.positive_words_path,
            merged_stop_words_path=config.merged_stop_words_path,
            raw_text_path=config.raw_text_path,
            output_file_path=config.output_file_path,
            destination_folder=config.destination_folder,
        )

        return text_analysis_config