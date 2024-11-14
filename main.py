from src.text_analysis.logging import logger
from src.text_analysis.pipeline.stage_01_text_extraction import TextExtractionPipeline
from src.text_analysis.pipeline.stage_02_text_processing import TextProcessingPipeline
from src.text_analysis.pipeline.stage_03_text_analysis import TextAnalysisPipeline

STAGE_NAME = "Text Extraction stage"
try:
        logger.info(f"===>>> {STAGE_NAME} started <<<===")
        obj = TextExtractionPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Text Processing Stage"
try:
        logger.info(f"===>>> {STAGE_NAME} started <<<===")
        obj = TextProcessingPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
STAGE_NAME="Text analysis Stage"
try:
        logger.info(f"===>>> stage {STAGE_NAME} started <<<===")
        obj = TextAnalysisPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e