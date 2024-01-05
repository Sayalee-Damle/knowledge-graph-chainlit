import os
from knowledge_graph.configuration.config import Config
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI


load_dotenv()

class KnowledgeGraphConfig(Config):
    model_name = os.getenv("OPENAI_MODEL")
    llm_cache = os.getenv("LLM_CACHE") == "True"
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model=model_name,
        temperature=0,
        request_timeout=os.getenv("REQUEST_TIMEOUT"),
        cache=llm_cache,
        streaming=True,
        verbose=True,
    )


cfg = KnowledgeGraphConfig()
