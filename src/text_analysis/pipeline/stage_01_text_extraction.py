from src.text_analysis.logging import logger
from src.text_analysis.config.configuration import ConfigurationManager
from src.text_analysis.components.text_extraction import TextExtraction

STAGE_NAME="Text Extraction Stage"

class TextExtractionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_text_extraction_config()
        data_ingestion = TextExtraction(config=data_ingestion_config)
        data_ingestion.extract_text()


if __name__=="__main__":
    try:
        logger.info(f"===>>> stage {STAGE_NAME} started <<<===")
        obj = TextExtractionPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e