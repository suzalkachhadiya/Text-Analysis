from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TextExtractionConfig:
    root_dir: Path
    input_file: Path
    destination_folder: Path