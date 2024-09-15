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

class RAG():
    def __init__(self, context: str):
        with open("./data.txt", "w", encoding="utf-8") as f:
            f.write(context)

        TEMPLATE = """
            Eres un asistente para el analisis de conversaciones, tu tarea es ayudar a interpretar y resumir conversaciones para proveer informacion
            importante y de ayuda. Se claro con tus respuestas y no des muchas vueltas en tus respuestas.

            Pregunta: {question} 

            Contexto: {context} 

            Respuesta:
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
            {"context": self.retriever | self._format_docs, "question": RunnablePassthrough()} | self.prompt | self.llm | StrOutputParser()
        )
    
    def _format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)

    def answer_question(self, question: str):
        return self.chain.invoke(question)