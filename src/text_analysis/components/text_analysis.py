from src.text_analysis.entity.config_entity import TextAnalysisConfig

import nltk
from nltk import word_tokenize
import pandas as pd
import os

class TextAnalysis:
    def __init__(self, config: TextAnalysisConfig):
        self.config = config
        
    def word_count(self,text):
        
        stop_words=set(open(self.config.merged_stop_words_path,encoding="ISO-8859-1").read().split())
        
        words=word_tokenize(text)
        words=[word for word in words if word not in stop_words]
        
        return len(words), words
    
    def total_words_count(self,text):
        total_words=0
        avg_word_len=0
        for sentence in text.split("\n"):
            for word in sentence.split(" "):
                total_words=total_words+1
                avg_word_len=avg_word_len+len(word)
                
        return total_words, avg_word_len
    
    def sentiment_check(self,text):
        
        positive_words_path=self.config.positive_words_path
        negative_words_path=self.config.negative_words_path
        
        positive_words = set(open(positive_words_path,encoding="ISO-8859-1").read().split())
        negative_words = set(open(negative_words_path,encoding="ISO-8859-1").read().split())
        
        positive_score = 0
        negative_score = 0
        total_words=0
        
        for sentence in text.split("\n"):
            for word in sentence.split(" "):
                total_words=total_words+1
                if word in positive_words:
                    positive_score += 1
                elif word in negative_words:
                    negative_score -= 1
                
        polarity_score = (positive_score + negative_score) / ((positive_score - negative_score) + 0.000001)
        subjectivity_score =(positive_score + negative_score)/ (total_words + 0.000001)
        
        return positive_score, negative_score, polarity_score, subjectivity_score
    
    def sentence_analysis(self,text,total_words):
        avg_sen_len=total_words/len(text.split("\n"))

        avg_words_sen=0
        num_sen=0
        for sentence in text.split("\n"):
            avg_words_sen = avg_words_sen + len(sentence.split(" "))
            num_sen=num_sen+1

        avg_words_sen=avg_words_sen / num_sen
        return avg_words_sen, avg_sen_len
    
    def count_syllables(self,word):
        word = word.lower()
        vowels = "aeiou"
        syllable_count = 0
        previous_char_was_vowel = False

        for char in word:
            if char in vowels:
                # Count only when encountering a vowel for the first time in a sequence
                if not previous_char_was_vowel:
                    syllable_count += 1
                previous_char_was_vowel = True
            else:
                previous_char_was_vowel = False

        # Adjustments for silent 'e' at the end
        if word.endswith("e") or word.endswith("es") or word.endswith("ed"):
            syllable_count -= 1
        return max(1, syllable_count)
    
    # Function to count complex words in text
    def count_complex_words(self,text,avg_sen_len):
        complex_words_count=0
        cnt=0
        for sentence in text.split("\n"):
            # Count complex words based on syllable count
            for word in sentence.split(" "):
                cnt=cnt+1
                if self.count_syllables(word) >= 3:
                    complex_words_count += 1
        
        pct_complex_words=complex_words_count/cnt
        fog_index = 0.4 * (avg_sen_len + pct_complex_words)

        
        return complex_words_count, pct_complex_words, fog_index
    
    def syllable_count_per_word(self,text,total_words):
        syllable_words_count=0
        for sentence in text.split("\n"):
            for word in sentence.split(" "):
                syllable_words_count=syllable_words_count+self.count_syllables(word)

        syllable_words_count=syllable_words_count/total_words
        return syllable_words_count
    
    def pronoun_count(self,text):
        # Pronouns in lowercase
        pronouns = [
            # Personal pronouns (subjective and objective)
            "i", "me", "you", "he", "him", "she", "her", "it", "we", "us", "they", "them",

            # Possessive pronouns
            "my", "mine", "your", "yours", "his", "her", "hers", "its", "our", "ours", "their", "theirs",

            # Reflexive pronouns
            "myself", "yourself", "himself", "herself", "itself", "ourselves", "yourselves", "themselves",

            # Demonstrative pronouns
            "this", "that", "these", "those",

            # Relative pronouns
            "who", "whom", "whose", "which", "that",

            # Interrogative pronouns
            "who", "whom", "whose", "which", "what",

            # Indefinite pronouns
            "anybody", "anyone", "anything", "each", "everybody", "everyone", "everything",
            "nobody", "no one", "nothing", "somebody", "someone", "something","no one", "nothing", "somebody", "someone", "something",
            "any", "all", "some", "none", "both", "few", "several", "many", "others"
        ]

        num_pronoun=0
        for sentence in text.split("\n"):
            for word in sentence.split(" "):
                if word.lower() in pronouns:
                    num_pronoun=num_pronoun+1

        return num_pronoun

    def text_analysis(self):
        processed_text_path = self.config.processed_text_path
        raw_text_path = self.config.raw_text_path
        
        # processed_text_path_list=os.listdir(processed_text_path),
        # raw_text_path_list=os.listdir(raw_text_path),
        
        url_id_list=[]
        url_list=[]
        positive_score_list=[]
        negative_score_list=[]
        polarity_score_list=[]
        subjectivity_score_list=[]
        avg_sen_len_list=[]
        pct_complex_words_list=[]
        fog_index_list=[]
        avg_words_sen_list=[]
        complex_words_count_list=[]
        word_count_list=[]
        syllable_words_count_list=[]
        num_pronoun_list=[]
        avg_word_len_list=[]
        
        for processed_filename, raw_filename in zip(os.listdir(processed_text_path),os.listdir(raw_text_path)):
            raw_file_path=os.path.join(raw_text_path,raw_filename)
            processed_file_path=os.path.join(processed_text_path,processed_filename)
            print(processed_file_path)
            with open(processed_file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                
            word_count, words = self.word_count(text)
            word_count_list.append(word_count)
            
            total_words, avg_word_len=self.total_words_count(text)
            avg_word_len_list.append(avg_word_len)
            
            positive_score, negative_score, polarity_score, subjectivity_score = self.sentiment_check(text)
            positive_score_list.append(positive_score)
            negative_score_list.append(negative_score)
            polarity_score_list.append(polarity_score)
            subjectivity_score_list.append(subjectivity_score)
            
            avg_words_sen, avg_sen_len=self.sentence_analysis(text,total_words)
            avg_sen_len_list.append(avg_sen_len)
            avg_words_sen_list.append(avg_sen_len)
            
            complex_words_count, pct_complex_words, fog_index= self.count_complex_words(text,avg_sen_len)
            complex_words_count_list.append(complex_words_count)
            pct_complex_words_list.append(pct_complex_words)
            fog_index_list.append(fog_index)
            
            syllable_words_count=self.syllable_count_per_word(text,total_words)
            syllable_words_count_list.append(syllable_words_count)
            
            pronouns_count=self.pronoun_count(text)
            num_pronoun_list.append(pronouns_count)
            
            # Initialize variables for URL_ID and URL
            url_id = None
            url = None

            # Open and read the file
            with open(raw_file_path, "r", encoding="ISO-8859-1") as file:
                for line in file:
                    # Check if the line contains the URL_ID by matching "Title: "
                    if line.startswith("Title:"):
                        url_id = line.split("Title:")[1].strip()

                    # Check if the line contains the URL by matching "Source URL: "
                    elif line.startswith("Source URL:"):
                        url = line.split("Source URL:")[1].strip()
                        
            url_id_list.append(url_id)
            url_list.append(url)
                        
        data = {
                "URL_ID": url_id_list,
                "URL": url_list,
                "POSITIVE SCORE": positive_score_list,
                "NEGATIVE SCORE": negative_score_list,
                "POLARITY SCORE": polarity_score_list,
                "SUBJECTIVITY SCORE": subjectivity_score_list,
                "AVG SENTENCE LENGTH": avg_sen_len_list,
                "PERCENTAGE OF COMPLEX WORDS": pct_complex_words_list,
                "FOG INDEX": fog_index_list,
                "AVG NUMBER OF WORDS PER SENTENCE": avg_words_sen_list,
                "COMPLEX WORD COUNT": complex_words_count_list,
                "WORD COUNT": word_count_list,
                "SYLLABLE PER WORD": syllable_words_count_list,
                "PERSONAL PRONOUNS": num_pronoun_list,
                "AVG WORD LENGTH": avg_word_len_list
            }
        
        # Create DataFrame
        df = pd.DataFrame(data)

        # Specify the file path to save the Excel file
        file_path = self.config.output_file_path

        # Write to Excel file
        df.to_excel(file_path, index=False)

                
    