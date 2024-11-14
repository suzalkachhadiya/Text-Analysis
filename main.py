from src.text_analysis.logging import logger
from src.text_analysis.pipeline.stage_01_text_extraction import TextExtractionPipeline
# from NWPproject.pipline.stage_02_data_validation import DataValidationTrainingPipeline
# from NWPproject.pipline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from NWPproject.pipline.stage_04_model_trainer import ModelTrainerPipeline
# from NWPproject.pipline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f"===>>> {STAGE_NAME} started <<<===")
        obj = TextExtractionPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e