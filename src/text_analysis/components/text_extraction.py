import requests
from bs4 import BeautifulSoup
import pandas as pd

from src.text_analysis.entity.config_entity import TextExtractionConfig
from src.text_analysis.constants import *
class TextExtraction:
    def __init__(self, config: TextExtractionConfig):
        self.config = config

    def extract_text(self):
        
        df=pd.read_excel(self.config.input_file)
        
        url_list=list(df["URL"])
        url_id_list=list(df["URL_ID"])

        for id, url in zip(url_id_list,url_list):
            print(id,url)

            response=requests.get(url,headers=HEADERS)
            html_content=response.text

            soup=BeautifulSoup(html_content,"html.parser")

            for ele in soup.find_all(["script","style","nav","footer","header","aside"]):
                ele.decompose()

            article_selectors=[
                "article",
                "[class*='article']",
                "[class*='post']",
                "main",
                ".content",
                "#content"
            ]

            title=""
            title_tag=soup.find("h1") or soup.find("title")
            if title_tag:
                title=title_tag.get_text().strip()

            article_content=None
            for selector in article_selectors:
                article_content=soup.select_one(selector)
                if article_content:
                    break
            text=article_content.get_text(separator="\n",strip=True)

            # Create filename from title or timestamp
            filename = id
            filename = f"artifacts/text_extraction/{filename}.txt"

            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"Title: {id}\n")
                file.write(f"Source URL: {url}\n")
                file.write("=" * 50 + "\n\n")
                file.write(text)

                