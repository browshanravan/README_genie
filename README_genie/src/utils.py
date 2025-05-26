from openai import OpenAI
import os
import sys
import fnmatch


def authenticate_llm_model(api_key, organization, project):
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


def exclusion_list(exclution_path, full_file_path):
    with open(file=exclution_path, mode="r") as f:
        file_contents= f.readlines()

    for line in file_contents:
        line = line.strip()
        if line.strip():
            breakdown= [f"{x}/" for x in full_file_path.split("/")[1:]][:-1]
            file_name= full_file_path.split("/")[-1]
            breakdown.append(file_name)
            for x in breakdown:
                if fnmatch.fnmatch(name= x, pat= line):
                    return True
    return False


def get_all_file_paths(directory_path):
    '''
    os.walk(directory) recursively traverses the directory and its subdirectories.
        root: the current directory path. In this case it is directory_path
        dirs: a list of directories within root.
        files: a list of files in root.
    For each file in the files list, os.path.join(root, file) is used to get the file's relative path.
    os.path.abspath() converts the relative path into an absolute path.
    '''
    file_paths = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            absolute_path = os.path.abspath(os.path.join(root, file))
            file_paths.append(absolute_path)
    
    return file_paths


def get_file_contents(all_file_paths, ouput_file_path, exclution_path, custom_exclusions):
    if os.path.exists(ouput_file_path):
        os.remove(ouput_file_path)
        print("An old file was deleted")
    
    cleaned_file_paths= [i for i in all_file_paths if "/.git" not in i]
    
    for full_file_path in cleaned_file_paths:
        file_name= full_file_path.split("/")[-1]
        if not exclusion_list(exclution_path= exclution_path, full_file_path= full_file_path) and file_name != ".gitignore":
            if sum([x not in file_name for x in custom_exclusions]) == len(custom_exclusions):
                try:
                    ## This code preserves all the spaces and empty lines
                    # with open(file=f"{full_file_path}", mode="r") as f:
                    #     file_contents= f.read()
                    # with open(file=ouput_file_path, mode="a") as o:
                    #     o.write(f"FILE_PATH: {full_file_path}\n")
                    #     o.write("FILE_CONTENT:\n")
                    #     o.write(file_contents)
                    
                    ## This code removes only empty lines!
                    with open(
                        file=f"{full_file_path}", mode="r") as read_file, open(
                            file=ouput_file_path, mode="a") as write_file:
                        write_file.write("\n")
                        write_file.write(f"FILE_PATH: {full_file_path}\n")
                        write_file.write("FILE_CONTENT:\n")
                        for line in read_file:
                            if line.strip():
                                write_file.write(line)
                    print(file_name)
                except:
                    pass


def create_preprompt():
    return '''
You are an expert programmer with proficiency in all computer languages.
You have been given a task to create a README.md style markdown text for a code you have been provided with.
The content provided to you is written in blocks and each block contains the following:
FILE_PATH: This shows the full path to the file that has the code/text/content
FILE_CONTENT: Anything after this provides the actual text/code contents of file referenced in FILE_PATH

The content you are given will have multiple FILE_PATH and FILE_CONTENT, so multiple blocks. 
This is the case since a typical GitHub repository will have multiple files, 
which are provided you you as blocks! 
There will be usually be one empty/blank line between each block to make it easier to understand. 
Below is an example of two blocks. 

You task is to look at all these blocks and construct a README.md style markdown content/text. 
As mentioned you are asked to produce a GitHub README.md markdown style content so you need to go 
through the code and understand what the project is trying to do. The FILE_PATH and FILE_CONTENT 
should help you understand the codebase structure and how the different files and components call each other.

When producing your README.md style markdown content/text, You need to write about the following, ideally
each with their own headder. However do not feel retructed to only write the suggestions below. Use your
judgement as to what the content should include but below can be very good starting points.

ABOUT THIS PROJECT
This section needs to provide a breif description of what the project/repo is about or is trying to achieve.
If you believe the coding style influences the way this objective is achieved you can mention that briefly
here. An example would be when a codebase uses OOP in pythin to write agents for agent based modelling.

PROJECT DESCRIPTION
Unlike the "about this project" section discussed above, which was meant to be very brieft, this section
goes into the details of what the project is about and the capabilities it has and what the user
can expect to get out of it when using this project and its possible use cases in real life and what
challenges the codebase can address.

GETTING STARTED
This section needs to provide the technical details of how to run the code. You can provide details on
what programming language and version is required and in order to get setup, what the user should 
install. For example in a python project you need to install requirements by executing
pip3 install -r requirements.txt
You can go further by providing a quick start section. For example:
Quickstart
Create a new file named streamlit_app.py in your project directory with the following code:

import streamlit as st
x = st.slider("Select a value")
st.write(x, "squared is", x * x)

Now run it to open the app!
streamlit run streamlit_app.py

REMEMBER, your response to the provided code/text blocks needs to be a README.md style markdown text
as described in details above. Please do not include any unnessessary reponses such as 
"ok, here is the markdown style text requested" or "ok can I help with anything else?".
Please adhere to my instructions. It is important to note that you might come
across a block that contains README. You can use this to help you but they often are not accurate or
very poorly written. It is your responsibility to produce a high quality and concise response and all the contents 
provided is meant to help you acheive this task. Now as mentioned above here is how the blocks will look like.


FILE_PATH: /Users/behzadrowshanravan/GitHub/biokit/requirements.txt
FILE_CONTENT:
easydev>=0.9.34
pandas
bioservices>=1.4.5
colormap
scipy
biopython
matplotlib
numpydoc
colorlog
pyyaml
pysam

FILE_PATH: /Users/behzadrowshanravan/GitHub/biokit/environment.yml
FILE_CONTENT:
name: biokit_env
channels:
- bioconda
dependencies:
- numpy
- pandas
- matplotlib
- scipy
- pip:
  - matplotlib
  - easydev>=0.9.21
  - bioservices
  - sphinx-gallery
  '''


def delete_file(ouput_file_path):
    if os.path.exists(path= ouput_file_path):
        os.remove(path= ouput_file_path)
        print("Temporary file was deleted")
    else:
        sys.exit(f"{ouput_file_path} does not exist")


def create_prompt(ouput_file_path):
    with open(file=f"{ouput_file_path}", mode="r") as f:
        file_contents= f.read()
    
    delete_file(ouput_file_path= ouput_file_path)
    
    return file_contents


def readme_generator(client, model, preprompt, prompt, readme_output_file):
    response= openai_llm(
        client= client,
        model= model,
        preprompt= preprompt,
        prompt= prompt
        )
    
    #remember "w" overwrites
    with open(file=f"{readme_output_file}", mode="w") as f:
        f.write(response)
