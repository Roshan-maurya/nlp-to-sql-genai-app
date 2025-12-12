# utils/sql_executor.py
import sqlite3
from config import SQLITE_DB_PATH, ALLOWED_SQL_PREFIXES


def is_select_query(sql: str) -> bool:
    sql_stripped = sql.strip().lower()
    for p in ALLOWED_SQL_PREFIXES:
        if sql_stripped.startswith(p.lower()):
            return True
    return False


def run_select(sql: str, params: tuple = ()) -> dict:
    if not is_select_query(sql):
        return {'error': 'Only SELECT queries are permitted.'}
    conn = sqlite3.connect(SQLITE_DB_PATH)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    try:
        c.execute(sql, params)
        rows = [dict(r) for r in c.fetchall()]
        cols = [d[0] for d in c.description] if c.description else []
        return {'columns': cols, 'rows': rows}
    except Exception as e:
        return {'error': str(e)}
    finally:
        conn.close()