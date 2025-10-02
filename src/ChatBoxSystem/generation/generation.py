from ChatBoxSystem import logger
import pandas as pd
from google import genai
from google.genai import types
from ChatBoxSystem.constants import *
import textwrap

class Generation:
    def __init__(self):
        self.client = genai.Client(api_key=API_KEY)
    
    def build_prompt(self, query: str, contexts: list) -> str:
        context_text = "\n".join([f"- {c}" for c in contexts])
        prompt = f"""
        Imagination you are me and you have to answer questions based on the provided context. The context is your own.
        Like or Dislike the following statements based on the context.
        Use the following context to answer the question if possible.
        Answer humanly and conversationally.
        If the answer is not in the context, try your best to answer based on your general knowledge.
        
        Context:
        {context_text}

        Question: {query}

        Answer:
        """
        return textwrap.dedent(prompt)

    def generate_answer(self, query: str, contexts: list) -> str:
        prompt = self.build_prompt(query, contexts)

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()