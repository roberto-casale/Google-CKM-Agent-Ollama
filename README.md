# Complete Beginner's Guide: Google Agent ADK with Ollama

Welcome! This tutorial will walk you through creating and running your first AI agent using Google's Agent Development Kit (ADK) with Ollama. If you're completely new to AI agents, Python, or both, don't worry—this guide explains everything step by step.

## Table of Contents

1. [What is This Project?](#what-is-this-project)
2. [Understanding the Technologies](#understanding-the-technologies)
3. [What This Project Does](#what-this-project-does)
4. [Prerequisites](#prerequisites)
5. [Installation Guide](#installation-guide)
6. [Understanding the Project Files](#understanding-the-project-files)
7. [Understanding the Code](#understanding-the-code)
8. [Running Your Agent](#running-your-agent)
9. [Troubleshooting](#troubleshooting)
10. [Next Steps](#next-steps)

---

## What is This Project?

This project is a **complete, working example** of an AI agent that can:
- 🎲 Roll dice (with any number of sides you want)
- 🔢 Check if numbers are prime
- 🧮 Perform basic mathematical calculations

Think of it as a smart assistant that lives on your computer and can do these specific tasks when you ask it. The agent uses a large language model (LLM) running locally on your machine through Ollama, so everything happens on your computer—no data is sent to external servers.

---

## Understanding the Technologies

Before we dive in, let's understand what each piece of technology does:

### Google Agent Development Kit (ADK)

**What it is:** A framework (a set of tools and rules) created by Google that makes it easy to build AI agents. Think of it like a recipe book that tells you how to combine different ingredients (AI models, tools, instructions) to create a working agent.

**Why we use it:** Instead of writing hundreds of lines of complex code from scratch, ADK provides pre-built components that we can simply connect together. It handles all the complicated parts like:
- Managing conversations
- Calling tools (functions) when needed
- Formatting responses
- Handling errors

### Ollama

**What it is:** A tool that lets you run large language models (LLMs) on your own computer. LLMs are the "brain" of AI agents—they understand language and can generate responses.

**Why we use it:** 
- **Privacy:** Everything runs on your computer, so your data never leaves your machine
- **Free:** No API costs or usage limits
- **Offline:** Works without internet (after initial setup)
- **Flexible:** You can use different models for different purposes

### LiteLLM

**What it is:** A library that acts as a "translator" between different AI model providers. It provides a unified interface so you can use Ollama models with ADK.

**Why we use it:** ADK expects models in a certain format, and LiteLLM converts Ollama's format into what ADK understands. It's like a universal adapter for AI models.

### ministral-3:14b

**What it is:** This is the specific AI model we're using. It's a 14-billion parameter model (the "14b" part) that's been optimized for efficiency. The model is what actually "thinks" and generates responses.

**Why this model:** It's a good balance between:
- **Performance:** Smart enough to understand complex requests
- **Speed:** Fast enough to respond quickly
- **Size:** Small enough to run on most modern computers

---

## What This Project Does

This project creates an AI agent that you can talk to. When you ask it to do something, it:

1. **Understands your request** using the ministral-3:14b model
2. **Decides which tool to use** (roll dice, check prime, or calculate)
3. **Calls the appropriate tool** to perform the action
4. **Returns a friendly response** explaining what it did

For example, if you say "Roll a 20-sided die," the agent will:
- Understand you want to roll dice
- Call the `roll_die` function with `sides=20`
- Get back a random number (like 13)
- Tell you: "You rolled a 13 on a 20-sided die!"

---

## Prerequisites

Before we start, you need a few things installed on your computer:

### 1. Python 3.10 or Higher

**What is Python?** Python is a programming language. We need it because ADK and all our code are written in Python.

**How to check if you have it:**
Open a terminal (Mac: Terminal app, Windows: Command Prompt or PowerShell, Linux: Terminal) and type:
```bash
python3 --version
```

If you see something like `Python 3.10.0` or higher, you're good! If not, or if you get an error:

**Install Python:**
- **Mac:** Download from [python.org](https://www.python.org/downloads/) or use Homebrew: `brew install python3`
- **Windows:** Download from [python.org](https://www.python.org/downloads/) (make sure to check "Add Python to PATH" during installation)
- **Linux:** Usually pre-installed, but if not: `sudo apt install python3` (Ubuntu/Debian) or `sudo yum install python3` (RedHat/CentOS)

### 2. Ollama

**What is Ollama?** As we explained earlier, this runs AI models on your computer.

**How to install Ollama:**

1. **Visit:** [https://ollama.ai](https://ollama.ai)
2. **Download** the installer for your operating system (Mac, Windows, or Linux)
3. **Run the installer** and follow the on-screen instructions
4. **Verify installation:** Open a terminal and type:
   ```bash
   ollama --version
   ```
   You should see a version number. If you get an error, make sure Ollama is installed and try restarting your terminal.

5. **Start Ollama:** Ollama needs to be running in the background. It usually starts automatically, but if not:
   ```bash
   ollama serve
   ```
   Leave this terminal window open—Ollama needs to keep running.

6. **Download the model:** We need to download the ministral-3:14b model. In a new terminal window, type:
   ```bash
   ollama pull ministral-3:14b
   ```
   This will download the model (it's large, so it may take several minutes depending on your internet speed). You'll see progress indicators as it downloads.

**Verify the model is installed:**
```bash
ollama list
```
You should see `ministral-3:14b` in the list.

### 3. A Code Editor (Optional but Recommended)

While you can use any text editor, having a proper code editor makes things easier:
- **VS Code:** [code.visualstudio.com](https://code.visualstudio.com/) (free, works on all platforms)
- **PyCharm:** [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/) (free community edition available)

---

## Installation Guide

Now let's set up the project step by step:

### Step 1: Navigate to the Project Directory

Open a terminal and navigate to where this project is located. If you're already in the project folder, you can skip this step.

```bash
cd /Users/admin/Desktop/ollama
```

**What this does:** The `cd` command (change directory) moves you into the project folder. All the commands we run need to be executed from inside this folder.

### Step 2: Create a Virtual Environment

**What is a virtual environment?** Think of it as a separate, isolated space for this project's Python packages. It prevents conflicts with other Python projects on your computer.

**Create the virtual environment:**
```bash
python3 -m venv venv
```

**What this does:** 
- `python3` - Uses Python 3
- `-m venv` - Creates a virtual environment
- `venv` - Names it "venv" (you'll see a folder called `venv` appear)

**Activate the virtual environment:**

- **On Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

**How to know it worked:** You should see `(venv)` at the beginning of your terminal prompt, like this:
```
(venv) user@computer:~/ollama$
```

**Important:** Every time you open a new terminal to work on this project, you need to activate the virtual environment again using the command above.

### Step 3: Install Python Dependencies

**What are dependencies?** These are Python packages (libraries) that our project needs to work. They're listed in `requirements.txt`.

**Install them:**
```bash
pip install -r requirements.txt
```

**What this does:**
- `pip` - Python's package installer
- `install` - Install packages
- `-r requirements.txt` - Read the list of packages from requirements.txt and install them all

**What gets installed:**
- `google-adk[all]` - The Google Agent Development Kit with all optional features
- `litellm` - The library that connects Ollama to ADK
- `requests` - A library for making HTTP requests (used by our verification script)

This will take a few minutes. You'll see lots of text scrolling by as packages are downloaded and installed. Don't worry if you see warnings—they're usually fine.

### Step 4: Set Up Environment Variables

**What are environment variables?** These are settings that tell programs where to find things. In our case, we need to tell LiteLLM where your Ollama server is running.

**Option 1: Export directly (temporary - lasts until you close terminal):**
```bash
export OLLAMA_API_BASE="http://localhost:11434"
```

**Option 2: Create a .env file (permanent):**

1. Create a file named `.env` in the project root (same folder as `requirements.txt`)
2. Add this line to it:
   ```
   OLLAMA_API_BASE=http://localhost:11434
   ```

**What this means:**
- `OLLAMA_API_BASE` - The name of the setting
- `http://localhost:11434` - The address where Ollama is running
  - `localhost` - Your own computer
  - `11434` - The port number (like a door number for the service)

**Note:** If your Ollama is running on a different computer or port, change the address accordingly.

### Step 5: Verify Your Setup

We've included a helpful script that checks if everything is set up correctly.

**Run the verification:**
```bash
python verify_setup.py
```

**What it checks:**
1. ✅ Are all Python packages installed?
2. ✅ Is the OLLAMA_API_BASE environment variable set?
3. ✅ Can we connect to the Ollama server?
4. ✅ Is the ministral-3:14b model available?
5. ✅ Does the agent configuration file exist?

If everything passes, you'll see:
```
✓ All checks passed! You're ready to use the agent.
```

If something fails, the script will tell you exactly what's wrong and how to fix it.

---

## Understanding the Project Files

Let's go through each file in the project and understand what it does:

### Project Structure

```
ollama/
├── src/
│   ├── __init__.py       # Makes src a Python package
│   └── agent.py          # The main agent definition
├── example.py            # Example script showing how to use the agent
├── verify_setup.py        # Script to check if everything is set up
├── requirements.txt      # List of Python packages needed
├── pyproject.toml        # Project metadata and configuration
├── root_agent.yaml       # ADK configuration file
├── .gitignore            # Files to ignore in version control
└── README.md             # This file!
```

### File-by-File Explanation

#### `src/__init__.py`

**What it is:** An empty file that makes the `src` folder a Python package.

**Why it exists:** Python needs this file to recognize `src` as a package, which allows us to import code from it using `from src.agent import root_agent`.

**Do you need to edit it?** No, leave it as is.

#### `src/agent.py` (The Main File!)

**What it is:** This is the heart of the project. It defines:
- Three tool functions (roll_die, check_prime, calculate)
- The AI agent that uses these tools

**Let's break it down section by section:**

**1. Imports (Lines 3-4):**
```python
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm
```

**What this does:**
- Imports the `Agent` class from ADK (this is what creates our agent)
- Imports `LiteLlm` which connects Ollama models to ADK

**2. The roll_die Function (Lines 7-18):**
```python
def roll_die(sides: int = 6) -> str:
    """Roll a die with the specified number of sides."""
    import random
    result = random.randint(1, sides)
    return f"You rolled a {result} on a {sides}-sided die!"
```

**What this does:**
- `def roll_die` - Defines a function named "roll_die"
- `sides: int = 6` - Takes one parameter called "sides" (an integer), defaulting to 6 if not provided
- `-> str` - This function returns a string
- `random.randint(1, sides)` - Generates a random number between 1 and the number of sides
- `return f"...{result}..."` - Returns a formatted string with the result

**3. The check_prime Function (Lines 21-37):**
```python
def check_prime(number: int) -> str:
    """Check if a number is prime."""
    if number < 2:
        return f"{number} is not a prime number."
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return f"{number} is not a prime number (divisible by {i})."
    
    return f"{number} is a prime number!"
```

**What this does:**
- Checks if a number is prime (only divisible by 1 and itself)
- `if number < 2` - Numbers less than 2 aren't prime
- `for i in range(2, int(number ** 0.5) + 1)` - Checks divisors from 2 up to the square root of the number (this is an optimization—you don't need to check beyond the square root)
- `number % i == 0` - Checks if the number is divisible by i (no remainder)
- If divisible by any number, it's not prime; otherwise, it is prime

**4. The calculate Function (Lines 40-58):**
```python
def calculate(expression: str) -> str:
    """Evaluate a simple mathematical expression safely."""
    try:
        allowed_chars = set("0123456789+-*/.() ")
        if not all(c in allowed_chars for c in expression):
            return "Error: Only basic math operations are allowed."
        
        result = eval(expression)
        return f"The result of '{expression}' is {result}."
    except Exception as e:
        return f"Error calculating '{expression}': {str(e)}"
```

**What this does:**
- Safely evaluates mathematical expressions
- `allowed_chars` - Only allows numbers and basic math operators (for security)
- `if not all(c in allowed_chars...)` - Checks if the expression contains only allowed characters
- `eval(expression)` - Evaluates the expression (e.g., "2 + 2" becomes 4)
- `try/except` - Catches any errors and returns a friendly error message

**5. Creating the Agent (Lines 63-83):**
```python
root_agent = Agent(
    model=LiteLlm(model="ollama_chat/ministral-3:14b"),
    name="demo_agent",
    description="A helpful demo agent...",
    instruction="You are a helpful assistant...",
    tools=[roll_die, check_prime, calculate],
)
```

**What this does:**
- Creates an Agent object and assigns it to `root_agent`
- `model=LiteLlm(...)` - Tells the agent to use the ministral-3:14b model via Ollama
  - `ollama_chat/` - This prefix tells LiteLLM to use the Ollama chat API (important for tool calling)
  - `ministral-3:14b` - The model name
- `name="demo_agent"` - Internal name for the agent
- `description` - What the agent does (used by ADK internally)
- `instruction` - System prompt that tells the agent how to behave
- `tools=[...]` - List of functions the agent can call. ADK automatically converts these Python functions into tools the AI can use!

**Key Point:** Notice we pass the functions directly (`roll_die`, not `roll_die()`). ADK automatically wraps them into tools—we don't need to do anything special!

#### `example.py`

**What it is:** A demonstration script showing how to use the agent programmatically (from Python code).

**Let's understand it:**

```python
from src.agent import root_agent
from google.adk.runners import Runner
```

**What this does:**
- Imports our agent from `src/agent.py`
- Imports `Runner` which executes the agent

```python
runner = Runner(root_agent)
```

**What this does:** Creates a Runner object that will execute our agent. Think of it as the "engine" that runs the agent.

```python
response = runner.run("Roll a 20-sided die")
print(f"Response: {response}")
```

**What this does:**
- `runner.run(...)` - Sends a message to the agent and gets a response
- The agent will understand the request, call the appropriate tool, and return a response
- We print the response

**How to run it:**
```bash
python example.py
```

#### `verify_setup.py`

**What it is:** A utility script that checks if everything is configured correctly.

**What it checks:**
1. Are Python packages installed?
2. Is Ollama running and accessible?
3. Is the model available?
4. Are environment variables set?

**How to run it:**
```bash
python verify_setup.py
```

You don't need to understand the code in this file—just run it to verify your setup!

#### `requirements.txt`

**What it is:** A simple text file listing all Python packages this project needs.

**Contents:**
```
google-adk[all]>=1.0.0
litellm>=1.0.0
requests>=2.31.0
```

**What each line means:**
- `google-adk[all]>=1.0.0` - Install Google ADK with all optional features, version 1.0.0 or higher
- `litellm>=1.0.0` - Install LiteLLM, version 1.0.0 or higher
- `requests>=2.31.0` - Install the requests library, version 2.31.0 or higher

**Why it exists:** This makes it easy for anyone (including you in the future) to install all dependencies with one command: `pip install -r requirements.txt`

#### `pyproject.toml`

**What it is:** A configuration file that describes the project (name, version, dependencies, etc.). This is a modern Python standard.

**Do you need to edit it?** Generally no, unless you want to change the project name or version.

#### `root_agent.yaml`

**What it is:** ADK's configuration file. ADK looks for this file to understand how to load your agent.

**Current contents:**
```yaml
# Root agent configuration for ADK
# The agent is defined in src/agent.py

# Environment variables can be set here if needed
# env:
#   OLLAMA_API_BASE: "http://localhost:11434"
```

**What it does:** 
- Tells ADK where to find the agent (in `src/agent.py`)
- Allows you to set environment variables if needed (currently commented out)

**Do you need to edit it?** Usually no. ADK automatically finds `root_agent` in `src/agent.py`.

#### `.gitignore`

**What it is:** Tells Git (version control) which files to ignore.

**Why it exists:** We don't want to commit things like:
- Virtual environment folders (`venv/`)
- Python cache files (`__pycache__/`)
- Environment files with secrets (`.env`)

**Do you need to edit it?** No, leave it as is.

---

## Understanding the Code

### How the Agent Works (The Big Picture)

1. **You send a message** (e.g., "Roll a 20-sided die")
2. **The agent receives it** and the LLM (ministral-3:14b) understands what you want
3. **The LLM decides** which tool to use (in this case, `roll_die`)
4. **ADK calls the tool** with the right parameters (`sides=20`)
5. **The tool executes** and returns a result ("You rolled a 13 on a 20-sided die!")
6. **The LLM formats the response** in a friendly way
7. **You receive the answer**

### How Tools Work

When you define a Python function with a docstring (the triple-quoted description), ADK automatically:
1. Reads the function signature (parameters and types)
2. Reads the docstring (description)
3. Converts it into a tool that the LLM can call
4. Handles calling the function when the LLM requests it

That's why we can just pass functions directly to `tools=[...]`—ADK does all the magic!

### The Model String: `ollama_chat/ministral-3:14b`

**Breaking it down:**
- `ollama_chat/` - This is the **provider**. It tells LiteLLM to use Ollama's chat API (not the OpenAI-compatible API). This is important because:
  - The chat API properly handles tool calling
  - It prevents infinite loops
  - It manages context better
- `ministral-3:14b` - This is the **model name** as it appears in Ollama

**Why not just `ministral-3:14b`?** Because LiteLLM needs to know which API to use. The prefix tells it "use Ollama's chat endpoint."

---

## Running Your Agent

Now that everything is set up, let's run the agent! There are three ways to interact with it:

### Option 1: Web Interface (Easiest for Beginners)

**Start the web server:**
```bash
adk web
```

**What happens:**
- ADK starts a web server (usually on `http://localhost:8000`)
- Your browser should open automatically
- If not, open your browser and go to the URL shown in the terminal

**How to use it:**
- Type your questions in the chat box
- Press Enter or click Send
- The agent will respond!

**Example interactions:**
- "Roll a 20-sided die"
- "Is 17 a prime number?"
- "What's 15 * 23?"
- "Roll a 12-sided die and check if the result is prime"

**To stop:** Press `Ctrl+C` in the terminal

### Option 2: Command Line Interface

**Start the CLI:**
```bash
adk run .
```

**What happens:**
- ADK loads the agent from the current directory (`.`)
- You'll see a prompt like: `user:`
- Type your questions and press Enter

**Example session:**
```
user: Roll a 20-sided die
[demo_agent]: I'll roll a 20-sided die for you.
             You rolled a 13 on a 20-sided die!

user: Is 13 a prime number?
[demo_agent]: Let me check if 13 is a prime number.
             13 is a prime number!

user: exit
```

**To quit:** Type `exit` and press Enter

### Option 3: Programmatic Usage (For Developers)

**Run the example script:**
```bash
python example.py
```

**What happens:** The script runs several example queries and prints the responses.

**Use in your own code:**
```python
from src.agent import root_agent
from google.adk.runners import Runner

# Create a runner
runner = Runner(root_agent)

# Ask a question
response = runner.run("Roll a 20-sided die and check if it's prime")
print(response)
```

---

## Troubleshooting

### Problem: "ModuleNotFoundError: No module named 'google.adk'"

**Cause:** The ADK package isn't installed or you're not in the virtual environment.

**Solution:**
1. Make sure you activated the virtual environment:
   ```bash
   source venv/bin/activate  # Mac/Linux
   # or
   venv\Scripts\activate  # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Problem: "Connection refused" or "Cannot connect to Ollama"

**Cause:** Ollama isn't running or is on a different port.

**Solution:**
1. Make sure Ollama is running:
   ```bash
   ollama serve
   ```
   Leave this terminal open!
2. Check if it's on a different port:
   ```bash
   # Test connection
   curl http://localhost:11434/api/tags
   ```
3. Update your environment variable if needed:
   ```bash
   export OLLAMA_API_BASE="http://localhost:11434"
   ```

### Problem: "Model 'ministral-3:14b' not found"

**Cause:** The model isn't downloaded in Ollama.

**Solution:**
```bash
ollama pull ministral-3:14b
```

Wait for it to finish downloading (you'll see progress indicators).

### Problem: Tools aren't being called

**Cause:** Using the wrong provider or model doesn't support tool calling.

**Solution:**
1. Make sure you're using `ollama_chat/` prefix (not `openai/`)
2. Check if the model supports tools:
   ```bash
   ollama show ministral-3:14b
   ```
   Look for "tools" in the capabilities list.

### Problem: "adk: command not found"

**Cause:** ADK CLI isn't installed or not in PATH.

**Solution:**
1. Make sure you installed `google-adk[all]`:
   ```bash
   pip install google-adk[all]
   ```
2. Make sure you're in the virtual environment
3. Try using Python module syntax:
   ```bash
   python -m google.adk.cli web
   ```

### Problem: Virtual environment not activating

**Cause:** Wrong command for your operating system.

**Solution:**
- **Mac/Linux:** `source venv/bin/activate`
- **Windows:** `venv\Scripts\activate` or `venv\Scripts\activate.bat`
- **Windows PowerShell:** `venv\Scripts\Activate.ps1` (you may need to allow scripts: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`)

---

## Next Steps

Now that you have a working agent, here are some ideas to expand it:

### 1. Add More Tools

Try adding new functions to `src/agent.py`:

```python
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    # Your code here
    return f"Weather in {city}: ..."

# Add it to the tools list:
tools=[roll_die, check_prime, calculate, get_weather]
```

### 2. Change the Model

Try different Ollama models:
```python
model=LiteLlm(model="ollama_chat/llama3.1:8b")  # Smaller, faster
# or
model=LiteLlm(model="ollama_chat/mistral:7b")   # Different model
```

### 3. Customize the Instructions

Modify the `instruction` parameter in `root_agent` to change how the agent behaves:

```python
instruction="""
You are a friendly math tutor. Always explain your reasoning
step by step and encourage the user to learn.
"""
```

### 4. Add Memory

ADK supports conversation memory. Research how to add session management to remember previous conversations.

### 5. Deploy It

Once you're happy with your agent, you can deploy it to:
- Google Cloud Run
- A local server
- Docker container

Check the ADK documentation for deployment guides.

---

## Resources

### Official Documentation

- **Google ADK:** [github.com/google/adk-python](https://github.com/google/adk-python)
- **Ollama:** [ollama.ai/docs](https://ollama.ai/docs)
- **LiteLLM:** [docs.litellm.ai](https://docs.litellm.ai/)

### Learning Resources

- **Python Basics:** [python.org/tutorial](https://docs.python.org/3/tutorial/)
- **AI Agents:** Search for "AI agent tutorials" on YouTube
- **ADK Examples:** Check out [github.com/google/adk-samples](https://github.com/google/adk-samples) for more examples

### Getting Help

- **ADK Issues:** [github.com/google/adk-python/issues](https://github.com/google/adk-python/issues)
- **Ollama Discord:** Join the Ollama community Discord
- **Stack Overflow:** Tag questions with `google-adk` or `ollama`

---

## Summary

Congratulations! You've successfully:

1. ✅ Set up a Python development environment
2. ✅ Installed and configured Ollama
3. ✅ Created an AI agent with custom tools
4. ✅ Learned how ADK, Ollama, and LiteLLM work together
5. ✅ Run your agent in multiple ways

You now have a working foundation to build more complex AI agents. The concepts you've learned here (tools, agents, models) apply to all AI agent development.

**Remember:**
- Always activate your virtual environment before working
- Keep Ollama running (`ollama serve`)
- Use `ollama_chat/` prefix for tool calling
- Functions with docstrings become tools automatically
- Check `verify_setup.py` if something isn't working

Happy agent building! 🚀
