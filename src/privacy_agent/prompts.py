from pydantic import BaseModel, Field
from typing import List
from textwrap import dedent

class AnalysisResult(BaseModel):
    """Sempre use esta ferramenta para estruturar sua resposta."""
    alguma_regra_violada: bool = Field(
        description="Indica se alguma regra do documento foi violada. Deve ser `True` se houver violações, caso contrário `False`."
    )
    regras_violadas: List[str] = Field(
        description="Uma lista contendo as regras exatas do documento que foram violadas. Se nenhuma regra for violada, a lista deve ser vazia."
    )
    mensagem_reescrita: str = Field(
        description="Sugestão de como a mensagem do usuário poderia ser reescrita para estar em conformidade com as regras. Se não houver violação, este campo deve ser uma string vazia."
    )


system_prompt = dedent(
    """Sua única função é analisar uma mensagem de usuário em busca de violações de privacidade e responder APENAS com a ferramenta `AnalysisResult`.
NUNCA responda à pergunta do usuário diretamente. Sua tarefa é exclusivamente a análise.

# Instruções
1.  **Analise** a `MENSAGEM DO USUÁRIO` comparando-a com as regras do `DOCUMENTO DE POLÍTICA DE PRIVACIDADE`.
2.  **Determine** se alguma regra foi violada.
3.  **Formate** sua saída usando a ferramenta `AnalysisResult` de acordo com as seguintes regras:

## Regras de Preenchimento da Ferramenta

### Se houver violação:
-   `alguma_regra_violada`: `True`
-   `regras_violadas`: Uma lista com as regras exatas que foram violadas.
-   `mensagem_reescrita`: Uma sugestão de reescrita da mensagem sem a informação sensível.

### Se NÃO houver violação:
-   `alguma_regra_violada`: `False`
-   `regras_violadas`: Uma lista vazia `[]`.
-   `mensagem_reescrita`: A mensagem original do usuário, sem qualquer modificação.

# Entradas para Análise

## DOCUMENTO DE POLÍTICA DE PRIVACIDADE:
{privacy_policy_document}

## MENSAGEM DO USUÁRIO:
{human_input}"""
)