from langchain.chains import LLMChain
from langchain.chains import create_tagging_chain_pydantic
from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

from knowledge_graph_chainlit.configuration.config import cfg

from knowledge_graph_chainlit.configuration.model import ResponseTags
from knowledge_graph_chainlit.configuration.toml_support import read_prompts_toml

prompts = read_prompts_toml()


### Sentiment Chain
def prompt_factory_sentiment() -> ChatPromptTemplate:
    section = prompts["tagging_sentiment"]
    human_message = section["human_message"]
    prompt_msgs = [
        SystemMessagePromptTemplate(
            prompt=PromptTemplate(
                template=section["system_message"], input_variables=[]
            )
        ),
        HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                template=human_message,
                input_variables=["answer"],
            )
        ),
    ]
    return ChatPromptTemplate(messages=prompt_msgs)

def sentiment_chain_factory() -> LLMChain:
    return create_tagging_chain_pydantic(
        ResponseTags, cfg.llm, prompt_factory_sentiment(), verbose=True
    )

chain = create_tagging_chain_pydantic(ResponseTags, cfg.llm, prompt_factory_sentiment())






