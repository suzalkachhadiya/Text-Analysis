from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TextExtractionConfig:
    root_dir: Path
    input_file: Path
    destination_folder: Path

@dataclass(frozen=True)
class TextProcessingConfig:
    root_dir: Path
    stop_words_folder_path: Path
    processed_text_path: Path
    merged_stop_words_path: Path
    extracted_files_folder_path: Path
    destination_folder: Path

@dataclass(frozen=True)
class TextAnalysisConfig:
    root_dir: Path
    positive_words_path: Path
    negative_words_path: Path
    merged_stop_words_path: Path
    raw_text_path: Path
    processed_text_path: Path
    output_file_path: Path
    destination_folder: Path