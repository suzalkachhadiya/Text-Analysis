import re

import os

from src.text_analysis.entity.config_entity import TextProcessingConfig


class TextProcessing:
    def __init__(self, config: TextProcessingConfig):
        self.config = config
    
    def merge_stop_words_files(self):
        folder_path=self.config.stop_words_folder_path
        print(folder_path)
        merged_file_path=os.path.join(self.config.merged_stop_words_path,"StopWords")
        os.makedirs(merged_file_path, exist_ok=True)
        print(merged_file_path)
        unwanted_pattern = re.compile(r"(http[s]?://|www\.)|Surnames from 1990 census|census\.gov")

        print(os.listdir(folder_path))        

        for filename in os.listdir(folder_path):
            file_path=os.path.join(folder_path,filename)

            if os.path.isfile(file_path):
                with open(file_path,"r",encoding="ISO-8859-1") as file:
                    lines = file.readlines()

                # Process each line to extract the relevant content
                new_lines = []
                for line in lines:
                    if unwanted_pattern.search(line):
                        continue

                    if '|' in line:
                        # Split by '|', strip whitespace, and remove text in parentheses
                        parts = [re.sub(r'\s*\(.*?\)\s*', '', part).strip() for part in line.split('|')]
                        # Add each part as a separate line in the new format
                        new_lines.append(parts[0] + '\n' + parts[1] + '\n')
                    else:
                        # If no '|' separator, add the line as it is
                        new_lines.append(line)

        # Write the modified content back to the same file
        merged_file_path=os.path.join(merged_file_path,filename)
        with open(merged_file_path, "w", encoding="ISO-8859-1") as file:
                file.writelines(new_lines)
                
    
    def process_text(self):
        folder_path=self.config.extracted_files_folder_path
        for filename in os.listdir(folder_path):
            
            file_path=os.path.join(folder_path,filename)
            
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            
            content_start = text.find('==================================================\n\n\n')
            if content_start != -1:
                text = text[content_start + 51:]
                
            text=text[1:]
            
            text=re.sub(r"[^a-zA-Z\s]","",text)
            text=text.lower()
            
            file_path=os.path.join(self.config.processed_text_path,filename)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text)