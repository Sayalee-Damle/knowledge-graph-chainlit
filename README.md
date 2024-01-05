conda deactivate knowledge_graph_chainlit
conda remove --name knowledge_graph_chainlit --all
conda create -n knowledge_graph_chainlit python=3.12   
conda activate knowledge_graph_chainlit
pip install poetry
poetry install