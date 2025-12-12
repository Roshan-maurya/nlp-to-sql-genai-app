Natural Language → SQL Generator using LangChain, OpenAI &amp; Flask  Select Public

AI-Powered SQL Query Generator – Project Overview

Project Summary

This project is a GenAI-powered SQL query generator built using LangChain + OpenAI + Python Flask. 
The system accepts a natural-language question, interprets it using an LLM, generates SQL based on the 
SQLite database schema, executes it, and returns the results.

Key Features
1. Automatic Schema Extraction
   - Reads all table names and columns from the SQLite database.
   - Schema is dynamically inserted into the LLM prompt.

2. Natural Language → SQL Conversion
   - Converts user questions into accurate SQL queries.

3. Query Execution + Output
   - Executes SQL against SQLite and returns results.

4. Flask Web Application
   - Simple UI with backend API.

Project Folder Structure
project_root/
│── app.py                 # Main Flask application
│── run.py                 # Run entry point
│── utils/
│     ├── db_setup.py      # Creates SQLite DB + tables in /data/
│     ├── reg_engine.py  # fetch table schema 
│     └── sql_executor.py
│── data/emploees.db       # SQLite DB file
│── templates/index.html
│──static 		# js+css
│── config		# db path + model names
│── requirements.txt
│── .env 		#OpenAI API key





Setup Instructions (Local)

1. Clone Repository
   git clone <https://github.com/Roshan-maurya/nlp-to-sql-genai-app.git >
   

2. Create Virtual Environment
   python -m venv venv
   venv\Scripts\activate   (Windows)
   source venv/bin/activate  (Linux/Mac)

3. Install Dependencies
   pip install -r requirements.txt

4. Create SQLite Database
   python utils/db_setup.py

5. Automatically setup DB with table Data
   python run.py

6. Open in Browser 
   python app.py (http://127.0.0.1:5000) 




