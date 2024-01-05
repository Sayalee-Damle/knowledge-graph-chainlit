from pathlib import Path
import knowledge_graph.backend.create_ontology as ontology
import knowledge_graph.backend.create_graph as create_g
import knowledge_graph.backend.read_graph as read_g
from knowledge_graph.configuration.log_factory import logger
from knowledge_graph.configuration.config import cfg
import knowledge_graph.backend.qna_service as qna
import knowledge_graph.services.vector_db as v_db
#import knowledge_graph.frontend.input_text as chk_inp


from knowledge_graph_chainlit.configuration.model import ResponseTags
import knowledge_graph_chainlit.configuration.tagging_service as ts
import chainlit as cl



async def ask_user_msg(question):
    ans = None
    while ans == None:
        ans = await cl.AskUserMessage(
            content=f"{question}", timeout=cfg.ui_timeout, raise_on_timeout= True
        ).send()
    return ans

@cl.on_chat_start
async def on_chat_start():

    await cl.Message(content="Create knowledge Graphs for the data you give").send()
    inp_text = await ask_user_msg("Give the input text")
    #if not await chk_inp.check_if_text_exists(inp_text):
    table = await ontology.return_ontology(inp_text)
    await cl.Message(content=table).send()
    ontology_relations, ontology_terms = await ontology.extract_ontology(table)
    G = await create_g.create_network(list(ontology_relations))
    path_description = await create_g.create_subgraph(G)
    await cl.Message(content=f"The summary derived from graphs is stored here: {path_description}").send()
    #await chk_inp.put_into_directory(inp_text)
    db_text = await v_db.create_embeddings_text(inp_text)
    db_summary = await v_db.create_embeddings_summary(Path(path_description))

    while True:
        ques = await ask_user_msg("Please ask any question realted to the topic if you want to")
        ans = await qna.return_answer(ques)
        await cl.Message(content=ans).send()


