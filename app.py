import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser


#langsmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')

## Prompt Template
prompt =ChatPromptTemplate.from_messages(
    [
        ('system','you are a helpful assistant. please respond to the question asked'),
        ('user','Question:{question}'),
    ]
)

# streamlit framework
st.title("Langchain Demo with Gemma Model")
input_text=st.text_input('What question you in mind?')


# Ollma Llama2 model
llm=Ollama(model='gemma2:2b') #avaliable models name in our local, for checking purpose open cmd and type "ollama list"

output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
