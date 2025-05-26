from openai import OpenAI
import os
import fnmatch


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


