# Arkantus - AI Code Assistant

Arkantus is an AI-powered code assistant that uses Google's Gemini API to analyze, fix, and execute Python code. Now with a simple and modern frontend built with Streamlit!

## Features

- Dynamic function calls to manipulate files and execute code  
- Agent loop with feedback to improve responses  
- Friendly and minimalistic interface built with Streamlit  
- Environment and dependency management using Astral.sh's `uv`  

## Installation

1. Clone the repository:  
```bash
git clone https://github.com/HigorChagas/arkantus.git
cd arkantus
```

2. Install dependencies and create a virtual environment with `uv`:  
```bash
uv install
uv venv
```

3. Activate the virtual environment:  
```bash
source .venv/bin/activate
```

4. Set up your Gemini API key in the `.env` file:  
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Run the backend (command line)

```bash
uv run main.py "Your prompt here"
```

### Run the frontend with Streamlit

```bash
streamlit run app.py
```

## License

This project is licensed under the [MIT License](LICENSE).