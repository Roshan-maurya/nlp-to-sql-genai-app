# utils/rag_engine.py
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import sqlite3
import json
from config import CHROMA_PERSIST_DIR, EMBEDDING_MODEL
import os


# def extract_schema_text(db_path: str) -> str:
#     conn = sqlite3.connect(db_path)
#     c = conn.cursor()

#     schema_items = []
#     c.execute("SELECT name FROM sqlite_master WHERE type='table'")
#     tables = [r[0] for r in c.fetchall()]
#     print(tables,'dddddddddddddddddddddd')
#     for t in tables:
#         if t.startswith('sqlite_'):
#             continue
#         c.execute(f'PRAGMA table_info({t})')
#         cols = c.fetchall()
#         cols_text = ', '.join([f"{col[1]}({col[2]})" for col in cols])
#         schema_items.append(f'Table: {t} -> {cols_text}')

#     conn.close()
#     return '\n'.join(schema_items)
def extract_schema_text(db_path: str) -> str:
    import sqlite3
    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    schema_items = []
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [r[0] for r in c.fetchall()]
    for t in tables:
        if t.startswith('sqlite_'):
            continue
        c.execute(f'PRAGMA table_info({t})')
        cols = c.fetchall()
        cols_text = ', '.join([f"{col[1]} ({col[2]})" for col in cols])
        schema_items.append(f"Table: {t}\nColumns: {cols_text}")

    conn.close()
    return '\n\n'.join(schema_items)

def build_schema_vectorstore(db_path, persist_directory="vectorstore/chroma"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT sql FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    docs = [t[0] for t in tables if t[0] is not None]

    # Embeddings
    embeddings = OpenAIEmbeddings()

    vectorstore = Chroma.from_texts(
        texts=docs,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    # vectorstore = Chroma.from_texts(
    #     texts=docs,
    #     embedding_function=embeddings,  # ← correct argument
    #     persist_directory=persist_directory
    # )

    # ❌ DO NOT CALL persist() in Chroma 0.4.x
    # vectorstore.persist()

    return vectorstore
