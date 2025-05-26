from README_genie.src.utils import (
    get_all_file_paths,
    get_file_contents,
    create_preprompt,
    create_prompt,
    authenticate_llm_model,
    readme_generator,
)

import os

##PLEASE CHANGE THE PARAMETERS INSIDE THE HASH BOX BASED ON YOUR SETUP
###################################################################
OPEN_AI_MODEL= ["o4-mini-2025-04-16", "gpt-4.1-2025-04-14"][0]
OPENAI_API_KEY= os.environ["OPENAI_API_KEY"]
OPENAI_PROJECT_ID= os.environ["OPENAI_PROJECT_ID"]
OPENAI_ORGANISATION_ID= os.environ["OPENAI_ORGANISATION_ID"]


HOME_DIRECTORY= os.environ["HOME"]
TARGET_REPO_DIRECTORY= "/GitHub/forecast_engine"
CURRENT_WORKING_DIRECTORY= os.environ["PWD"]
TEMP_OUTPUT_FILE= "/temp_output_file.txt"
GIT_IGNORE= "/.gitignore"
CUSTOM_EXCLUSIONS= [".ipynb", ".csv", ".fastq", ".fasta", ".rst"]
GENERATIVE_README= "/GENERATIVE_README.md"
###################################################################


all_files_full_path = get_all_file_paths(
    directory_path=HOME_DIRECTORY+TARGET_REPO_DIRECTORY
    )

get_file_contents(
    exclution_path= HOME_DIRECTORY+TARGET_REPO_DIRECTORY+GIT_IGNORE,
    ouput_file_path= CURRENT_WORKING_DIRECTORY+TEMP_OUTPUT_FILE,
    all_file_paths= all_files_full_path,
    custom_exclusions= CUSTOM_EXCLUSIONS,
    )

pre_prompt= create_preprompt()

prompt= create_prompt(
    ouput_file_path= CURRENT_WORKING_DIRECTORY+TEMP_OUTPUT_FILE,
    )

client= authenticate_llm_model(
    api_key= OPENAI_API_KEY, 
    organization= OPENAI_ORGANISATION_ID, 
    project= OPENAI_PROJECT_ID
    )

readme_generator(
    client= client,
    model= OPEN_AI_MODEL,
    preprompt= pre_prompt,
    prompt= prompt,
    readme_output_file= CURRENT_WORKING_DIRECTORY+GENERATIVE_README,
)