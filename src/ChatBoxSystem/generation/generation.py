from ChatBoxSystem import logger
import pandas as pd
from google import genai
from google.genai import types
from ChatBoxSystem.constants import *
import textwrap

class Generation:
    def __init__(self, retrieval_results, distances):
        self.client = genai.Client(api_key=API_KEY)
        self.retrieval_results = retrieval_results
        self.distances = distances
    
    def build_prompt(self, query: str, contexts: list) -> str:
        context_text = "\n".join([f"- {c}" for c in contexts])
        prompt = f"""
        You are a helpful assistant.
        Answer the question based on the provided context. If the answer is not contained within the context, respond with "I don't know". 
        Use the following context to answer the question.

        Context:
        {context_text}

        Question: {query}

        Answer:
        """
        return textwrap.dedent(prompt)  # loại bỏ khoảng trắng thừa

    def generate_answer(self, query: str, contexts: list) -> str:
        prompt = self.build_prompt(query, contexts)

        contents = [
            types.Content(role="user", parts=[types.Part.from_text(text=prompt)])
        ]

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents
        )

        return response.text.strip()