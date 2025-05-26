from README_genie.src.utils import (
    get_all_file_paths,
    get_file_contents,
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


HOME_DIRECTORY= os.environ["HOME"]
TARGET_REPO_DIRECTORY= "/GitHub/biokit"
CURRENT_WORKING_DIRECTORY= os.environ["PWD"]
OUTPUT_FILE= "/output_file.txt"
GIT_IGNORE= "/.gitignore"
CUSTOM_EXCLUSIONS= [".ipynb", ".csv", ".fastq", ".fasta", ".rst"]



all_files_full_path = get_all_file_paths(
    directory_path=HOME_DIRECTORY+TARGET_REPO_DIRECTORY
    )

cleaned_files= get_file_contents(
    exclution_path= CURRENT_WORKING_DIRECTORY+GIT_IGNORE,
    ouput_file_path= CURRENT_WORKING_DIRECTORY+OUTPUT_FILE,
    all_file_paths= all_files_full_path,
    custom_exclusions= CUSTOM_EXCLUSIONS,
    )



# client= authenticate_model(
#     api_key= OPENAI_API_KEY, 
#     organization= OPENAI_ORGANISATION_ID, 
#     project= OPENAI_PROJECT_ID
#     )

# response= openai_llm(
#     client= client,
#     model= OPEN_AI_MODEL,
#     preprompt= PRE_PROMPT,
#     prompt= QUERY,
# )

# print(response)