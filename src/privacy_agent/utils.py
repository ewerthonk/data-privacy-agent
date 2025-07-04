import sys
from pathlib import Path
from langchain_community.document_loaders import UnstructuredMarkdownLoader

PROJECT_ROOT_PATH = Path.cwd().parent.resolve(strict=True)
POLICY_DOCS_PATH = PROJECT_ROOT_PATH.joinpath("data").joinpath("privacy_policy_documents")
EXAMPLES_PATH = PROJECT_ROOT_PATH.joinpath("data").joinpath("examples")
sys.path.append(str(EXAMPLES_PATH))

from examples import examples

for policy_file in POLICY_DOCS_PATH.glob("*.md"):
    globals()[f"{policy_file.stem}"] = UnstructuredMarkdownLoader(
        file_path=policy_file,
        mode="single",
    ).load()[0].page_content
