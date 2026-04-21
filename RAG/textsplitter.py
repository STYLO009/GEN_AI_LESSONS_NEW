from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Load single text file
loader = TextLoader(r'D:\GEN_AI\RAG\Files\india.txt', encoding='utf-8')
docs = loader.load()

# Load all txt files from folder
dir_loader = DirectoryLoader(
    path=r'D:\GEN_AI\RAG\Files',
    glob='*.txt',
    loader_cls=TextLoader
)

# Text splitter
textsplitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

# Split documents
text = textsplitter.split_documents(docs)


print(text)