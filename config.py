# config.py
import os


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SQLITE_DB_PATH = 'data/employees.db'
CHROMA_PERSIST_DIR = 'vectorstore/chroma'
EMBEDDING_MODEL = 'text-embedding-3-small' # or your chosen model
CHAT_MODEL = 'gpt-4o-mini' # adjust if needed


# Only allow read-only SELECT statements from generated SQL
ALLOWED_SQL_PREFIXES = ['SELECT']