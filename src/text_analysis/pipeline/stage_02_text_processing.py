from src.text_analysis.config.configuration import ConfigurationManager
from src.text_analysis.components.text_processing import TextProcessing
from src.text_analysis.logging import logger

STAGE_NAME="Text Processing Stage"

class TextProcessingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        text_processing_config = config.get_text_processing_config()
        text_processing = TextProcessing(config=text_processing_config)
        text_processing.merge_stop_words_files()
        text_processing.process_text()

if __name__=="__main__":
    try:
        logger.info(f"===>>> stage {STAGE_NAME} started <<<===")
        obj = TextProcessingPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e