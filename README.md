# README_genie

## About this project
The aim of this project is for the user to be able to upload their Git repository and recieve a markdown `README.md` file.

This project requires `.gitignore` to ensure unwanted files are not analysed and sent to the OpenAI LLM model. 

You can however add custom exclusion file extensions such as `.csv` or `.ipynb`, which some projects can have but should not be a critical or operational part of a repo.

## Project output example
You can compare the the current [forecast_engine repo README.md](https://github.com/browshanravan/forecast_engine/blob/main/README.md) file to the [forecast_engine GENERATIVE_README.md](https://github.com/browshanravan/README_genie/blob/main/GENERATIVE_README.md) produced by this application.

## Project limitations
Please note that since the project uses OpenAI API the tool is limited by the number of tokens each model can accomodate per call. 

For this reason it is imperative that you have a very well populated `.gitignore` and you add any file extensions to the `custom exclusion`, which you do not want to be considred as part of generating the `README.md`. Example of of such extensions include `.csv` or `.ipynb`.