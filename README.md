AI-Powered SQL Query Generator – Project Overview
📌 Project Summary

This project is a GenAI-powered SQL Query Generator built using:

Python Flask

LangChain

OpenAI Chat Models

SQLite3

The system accepts a natural-language question, converts it into SQL using an LLM, executes it on a SQLite database, and returns clean tabular results on the UI.

🚀 Key Features
1. Automatic Schema Extraction

Reads all tables and columns dynamically from the SQLite DB.

Injects the full schema into the LLM prompt—no need for manual definitions.

2. Natural Language → SQL Conversion

Converts user questions like
“Show employee name, salary, and department name”
into valid, accurate SQL.

3. SQL Execution + Output Rendering

Executes generated or user-written SQL.

Returns clean rows + columns to the UI.

4. Flask Web Application

Simple UI with a prompt box and SQL editor.

Backend API for SQL generation and execution.

📁 Project Structure
project_root/
│── app.py                  # Main Flask app
│── run.py                  # Entry point to set up DB + start app
│── utils/
│     ├── db_setup.py       # Creates SQLite DB + tables in /data/
│     ├── rag_engine.py     # Fetches table schema
│     └── sql_executor.py   # Executes SQL safely
│── data/employees.db       # SQLite database
│── templates/index.html    # Frontend UI
│── static/                 # JS + CSS files
│── config/                 # Model names + DB path config
│── requirements.txt
│── .env                    # OpenAI API Key

⚙️ Local Setup Instructions
1. Clone Repository
git clone https://github.com/Roshan-maurya/nlp-to-sql-genai-app.git

2. Create Virtual Environment
python -m venv venv


Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Create SQLite Database
python utils/db_setup.py

5. Auto-Setup Database With Data
python run.py

6. Run the Flask App
python app.py

Then open in browser:
👉 http://127.0.0.1:5000

Then open in browser:

👉 http://127.0.0.1:5000

If you'd like, I can also:

✅ Add screensh
