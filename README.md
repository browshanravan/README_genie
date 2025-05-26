# README_genie

This `README.md` was produced by the README_genie itself.

## About This Project  
**README_genie** is a command-line utility that automatically generates a high-quality `README.md` for any Git repository by leveraging OpenAI’s large language models. It scans your project’s directory (honoring `.gitignore` and custom exclusion patterns), aggregates code and documentation, and prompts an LLM to produce a structured, informative README.

---

## Project Description  
- **Automated README Generation**  
  • Recursively collects all files in your target repo, excluding Git-ignored files and user-specified extensions (.csv, .ipynb, etc.).  
  • Concatenates file paths and contents into a prompt payload.  
  • Uses OpenAI’s API (via the `openai` Python package) to synthesize a professional README in Markdown.  

- **Key Capabilities**  
  • Customizable exclusion rules: fine-tune which files or directories are considered.  
  • Configurable OpenAI model selection (e.g., “o4-mini-2025-04-16” or “gpt-4.1-2025-04-14”).  
  • Easy integration into CI/CD workflows to keep README content in sync with code changes.  

- **Use Cases**  
  • Bootstrapping documentation for new or legacy repositories.  
  • Maintaining up-to-date READMEs in continuously evolving codebases.  
  • Standardizing project overviews and usage instructions across teams.  

---

## Getting Started

### Prerequisites  
- Python 3.8 or higher  
- An OpenAI account with API access  
- Git repository with a well-configured `.gitignore`  

### Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/browshanravan/README_genie.git
   cd README_genie
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

### Configuration  
Before running the tool, you must:  
1. **Set environment variables** (e.g., in your shell profile or CI secrets):  
   ```bash
   export OPENAI_API_KEY="sk-..."
   export OPENAI_PROJECT_ID="your-project-id"
   export OPENAI_ORGANISATION_ID="your-org-id"
   ```  
2. **Edit `main.py` constants** to match your environment and target repository:  
   ```python
   OPEN_AI_MODEL = "o4-mini-2025-04-16"            # or "gpt-4.1-2025-04-14"
   TARGET_REPO_DIRECTORY = "/GitHub/forecast_engine"
   GIT_IGNORE = "/.gitignore"
   CUSTOM_EXCLUSIONS = [".ipynb", ".csv", ".fastq", ".fasta", ".rst"]
   GENERATIVE_README = "/GENERATIVE_README.md"
   ```  

### Quickstart  
```bash
python main.py
```
- The script will:  
  1. Gather all file paths under `TARGET_REPO_DIRECTORY`.  
  2. Filter out `.gitignore` patterns and custom exclusions.  
  3. Aggregate file contents into a temporary prompt file.  
  4. Invoke the OpenAI API to generate a markdown README.  
  5. Write the result to `GENERATIVE_README.md` in your working directory.  

---

## Project Structure  
```
README_genie/
├── LICENSE                             # MIT license
├── main.py                             # Entry point; orchestrates file collection & generation
├── requirements.txt                    # Python dependencies (openai)
└── README_genie/
    └── src/
        └── utils.py                    # Core helper functions:
                                          • authenticate_llm_model()
                                          • get_all_file_paths()
                                          • exclusion_list()
                                          • get_file_contents()
                                          • create_preprompt()
                                          • create_prompt()
                                          • readme_generator()
```

---

## Limitations & Best Practices  
- **Token Limits**: Large repositories may exceed model context windows. Ensure your `.gitignore` and `CUSTOM_EXCLUSIONS` are comprehensive to reduce prompt size.  
- **Cost & Rate Limits**: LLM invocations incur usage costs and rate restrictions—use judiciously.  
- **Quality Assurance**: Always review and tweak the generated README; the AI may misinterpret complex or domain-specific code.  

---

## Contributing  
Contributions, issues, and feature requests are welcome! Please open an issue or pull request on GitHub.

---

## License  
This project is licensed under the [MIT License](LICENSE).