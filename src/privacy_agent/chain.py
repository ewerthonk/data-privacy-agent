import sys
from pathlib import Path
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# Add src to Python path for local imports
PROJECT_ROOT_PATH = Path.cwd().parent.resolve(strict=True)
sys.path.append(str(PROJECT_ROOT_PATH.joinpath("src")))

from privacy_agent.prompts import system_prompt, AnalysisResult

def create_chain(model, model_provider):    
    # Prompt
    prompt = ChatPromptTemplate([
        ("system", system_prompt),
        ("human", "{human_input}"),
    ])
    # Model
    model = init_chat_model(
        model=model,
        model_provider=model_provider,
        temperature=0.0,
    )
    # Chain
    return prompt | model.with_structured_output(schema=AnalysisResult)