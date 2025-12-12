# app.py
from flask import Flask, render_template, request, jsonify
from utils.rag_engine import extract_schema_text
from utils.sql_executor import run_select
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import PromptTemplate
from config import EMBEDDING_MODEL, CHAT_MODEL
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv(override=True)

app = Flask(__name__)

# Load embeddings (not really needed for full schema, but keep if you want future RAG)
embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)

# SQL generation prompt template
SQL_PROMPT = PromptTemplate(
    input_variables=['query', 'schema'],
    template="""
You are an assistant that converts natural language into a SQL SELECT query.
You MUST use ONLY the table names and column names listed below. 
Do NOT invent any new column or table names.

Always make string comparisons case-insensitive (e.g., using UPPER() or LOWER()).
For example: WHERE UPPER(column_name) = 'VALUE'

Schema:
{schema}

User request:
{query}

Return ONLY a single SQL SELECT statement. Do NOT add explanations or backticks.
"""
)


# LLM model for generating SQL
chat_model = ChatOpenAI(model=CHAT_MODEL, temperature=0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schema')
def schema():
    db_path = os.path.join('data', 'employees.db')
    s = extract_schema_text(db_path)
    return jsonify({'schema': s})

@app.route('/ask', methods=['POST'])
def ask():
    payload = request.json or {}
    if 'prompt' in payload.keys():
        user_prompt = payload.get('prompt', '')

        # === FIX HERE ===
        # Get full DB schema instead of partial RAG
        db_path = os.path.join('data', 'employees.db')
        schema_text = extract_schema_text(db_path)

        # Build final prompt with full schema
        final_prompt = SQL_PROMPT.format(query=user_prompt, schema=schema_text)

        # Generate SQL using ChatOpenAI
        sql_text = chat_model([HumanMessage(content=final_prompt)]).content.strip()
        # Execute SQL safely
        result = run_select(sql_text)
    else:
        sql_text = payload.get('sql', '')
        result = run_select(sql_text)

    # Ensure consistent output for frontend
    response = {
        'sql': sql_text,
        'columns': result.get('columns', []),
        'rows': result.get('rows', []),
        'error': result.get('error', '')
    }
    return jsonify(response)
    # return jsonify({'sql': sql_text, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)
