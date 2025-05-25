from README_genie.src.utils import (
    authenticate_model,
    openai_llm,
)

import os


OPEN_AI_MODEL= ["o4-mini-2025-04-16", "gpt-4.1-2025-04-14"][0]
OPENAI_API_KEY= os.environ["OPENAI_API_KEY"]
OPENAI_PROJECT_ID= os.environ["OPENAI_PROJECT_ID"]
OPENAI_ORGANISATION_ID= os.environ["OPENAI_ORGANISATION_ID"]
PRE_PROMPT= "You are a skilled speaker and writter. You speak and write very concisely and to the point"
QUERY= "Tell me a quick joke"



client= authenticate_model(
    api_key= OPENAI_API_KEY, 
    organization= OPENAI_ORGANISATION_ID, 
    project= OPENAI_PROJECT_ID
    )

response= openai_llm(
    client= client,
    model= OPEN_AI_MODEL,
    preprompt= PRE_PROMPT,
    prompt= QUERY,
)

print(response)