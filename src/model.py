import os
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
import openai

def disable_ssl_verification():
    openai.VERIFY_SSL = False

def set_openai_api_key(api_key):
    os.environ["OPENAI_API_KEY"] = api_key

def load_and_split_pdf(pdf_file):
    loader = PyPDFLoader(pdf_file)
    return loader.load_and_split()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def initialize_chroma_vectorstore(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=20000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    return Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

def initialize_rag_chain(vectorstore):
    retriever = vectorstore.as_retriever()
    prompt = hub.pull("rlm/rag-prompt")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

# Disable SSL verification
disable_ssl_verification()

# Set OpenAI API key
set_openai_api_key("your-api-keys")