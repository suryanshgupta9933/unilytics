# Importing Dependencies
import os
import warnings
import pandas as pd
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader

from .branded import detect_brand_term
from .prompts import summary_prompt, ctr_chart_prompt, click_variance_prompt
from .utils import load_image
warnings.filterwarnings('ignore')

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class Agent:
    def __init__(self, data):
        self.llm = ChatOpenAI(model="gpt-4o-mini")
        self.brand_term = detect_brand_term(data)
        self.url = pd.read_excel(data, sheet_name='Pages')['Top pages'][0]

    def brand_summary(self):
        """
        Generate brand summary
        """
        # Load the webpage data
        loader = WebBaseLoader(self.url)
        docs = loader.load()
        webpage_data = docs[0].page_content
        # Generate the summary
        prompt = PromptTemplate.from_template(summary_prompt)
        messages = [
            SystemMessage(summary_prompt),
            HumanMessage("Brand Term: " + self.brand_term + "\nWebpage Data:\n" + webpage_data),
        ]
        response = self.llm.invoke(messages)
        return response.content

    def ctr_chart_analysis(self, figure):
        """
        Generates insights on the CTR chart analysis
        """
        # Load the image data
        encoded_image = load_image(figure)
        # Generate the insights
        prompt = PromptTemplate.from_template(ctr_chart_prompt)
        message_content = [
            {"type": "text", "text": ctr_chart_prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
        ]
        response = self.llm.invoke(
            [HumanMessage(
                content=message_content
            )]
        )
        return response.content

    def click_variance_analysis(self, figure):
        """
        Generates insights on the Click Variance chart analysis
        """
        # Load the image data
        encoded_image = load_image(figure)
        # Generate the insights
        prompt = PromptTemplate.from_template(click_variance_prompt)
        message_content = [
            {"type": "text", "text": click_variance_prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
        ]
        response = self.llm.invoke(
            [HumanMessage(
                content=message_content
            )]
        )
        return response.content
