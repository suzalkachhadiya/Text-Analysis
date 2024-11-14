from src.text_analysis.config.configuration import ConfigurationManager
from src.text_analysis.components.text_analysis import TextAnalysis
from src.text_analysis.logging import logger

STAGE_NAME="text analysis stage"

class TextAnalysisPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        text_analysis_config = config.get_text_analysis_config()
        text_analysis = TextAnalysis(config=text_analysis_config)
        text_analysis.text_analysis()
    
if __name__=="__main__":
    try:
        logger.info(f"===>>> stage {STAGE_NAME} started <<<===")
        obj = TextAnalysisPipeline()
        obj.main()
        logger.info(f"===>>> stage {STAGE_NAME} completed <<<===\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e