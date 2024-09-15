import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

embeddings_model = OpenAIEmbeddings(api_key=os.getenv("OPEN_AI_KEY"))
llm = ChatOpenAI(model_name = "tgi", base_url=os.getenv("FRIDA_AI_BASE_URL"), api_key=os.getenv("FRIDA_KEY"))

with open("./data.txt", "w", encoding="utf-8") as f:
    f.write("hola")


loader = TextLoader("./data.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = text_splitter.split_documents(documents)
db = Chroma.from_documents(chunks, embedding = embeddings_model)

#vectordb = Chroma(persist_directory="test_index", embedding_function = embeddings_model)

TEMPLATE = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

Question: {question} 

Context: {context} 

Answer:
"""

retriever = db.as_retriever()
prompt = PromptTemplate.from_template(template=TEMPLATE)
chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()
)

output = chain.invoke("what is firebase?")

print(output)


class RAG():
    def __init__(self, context: str):
        with open("./data.txt", "w", encoding="utf-8") as f:
            f.write(context)

        TEMPLATE = """
            You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

            Question: {question} 

            Context: {context} 

            Answer:
        """

        self.loader = TextLoader("./data.txt")
        self.documents = self.loader.load()
        self.embeddings_model = OpenAIEmbeddings(api_key=os.getenv("OPEN_AI_KEY"))
        self.llm = ChatOpenAI(model_name = "tgi", base_url=os.getenv("FRIDA_AI_BASE_URL"), api_key=os.getenv("FRIDA_KEY"))
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        self.chunks = self.text_splitter.split_documents(self.documents)
        self.db = Chroma.from_documents(self.chunks, embedding = self.embeddings_model)
        self.prompt = PromptTemplate.from_template(template=TEMPLATE)
        self.retriever = self.db.as_retriever()
        self.chain = (
            {"context": self.retriever | _format_docs, "question": RunnablePassthrough()} | self.prompt | self.llm | StrOutputParser()
        )
    
    def _format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def answer_question(self, question: str):
        return self.chain.invoke(question)