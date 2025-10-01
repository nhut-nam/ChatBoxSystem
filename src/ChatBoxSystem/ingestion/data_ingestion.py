import os
from ChatBoxSystem.entity.config_entity import DataIngestionConfig
import gdown
from ChatBoxSystem import logger
import pandas as pd
from google import genai
from google.genai import types
from ChatBoxSystem.constants import API_KEY as api_key

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_download_dir)

            logger.info(f"Downloaded file from :[{dataset_url}] and saved at :[{zip_download_dir}]")
        except Exception as e:
            raise e


    def data_augmentation(self):
        if self.config.augmentation:
            df = pd.read_csv(self.config.local_data_file)
            augmented_records = []
            for _, row in df.iterrows():
                paraphrases = self.paraphrase_text(row['Answer'])
                for p in paraphrases:  # nếu paraphrases là list
                    augmented_records.append({
                        "Question": row['Question'],
                        "Answer": p
                    })
            df_augmented = pd.DataFrame(augmented_records)
            df_augmented.to_csv(self.config.local_data_file, index=False)
            logger.info(f"Data augmentation completed and saved to {self.config.local_data_file}")
        else:
            logger.info("Data augmentation is disabled.")


    def paraphrase_text(self, text: str) -> list:
        prompt = f"Paraphrase the following text into 5 different ways:\n{text}"
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash",  # hoặc gemini-2 nếu bạn có quyền
            contents=prompt
        )

        # response.output_text chứa kết quả text
        paraphrases = [line.strip() for line in response.text.split("\n") if line.strip()]
        return paraphrases