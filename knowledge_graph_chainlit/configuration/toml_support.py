from pathlib import Path
import tomli
from knowledge_graph_chainlit.configuration.config import cfg


def read_toml(file: Path) -> dict:
    with open(file, "rb") as f:
        return tomli.load(f)


def read_prompts_toml() -> dict:
    return read_toml("./prompts_chainlit.toml")


prompts = read_prompts_toml()
