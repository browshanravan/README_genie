from openai import OpenAI


def authenticate_model(api_key, organization, project):
    return OpenAI(
        api_key= api_key,
        organization= organization,
        project= project,
        )


def openai_llm(client, model, preprompt, prompt, stream=False):
    response = client.responses.create(
        model= model,
        input=[
            {
                "role": "system",
                "content": preprompt,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        stream= stream,
    )
    
    return response.output_text