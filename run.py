# run.py
import os
from utils.db_setup import create_and_seed_db
from utils.rag_engine import build_schema_vectorstore
import subprocess
import webbrowser
import time
from dotenv import load_dotenv
load_dotenv(override=True)

if __name__ == '__main__':
    # Ensure environment variable
    if 'openai_api_key' not in os.environ:
        print('Please set OPENAI_API_KEY as an environment variable before running.')
        print('On Linux/Mac: export OPENAI_API_KEY="sk-..."')
        print('On Windows (Powershell): $env:OPENAI_API_KEY="sk-..."')
        exit(1)

    db_path = os.path.join('data', 'employees.db')
    os.makedirs('data', exist_ok=True)
    os.makedirs('vectorstore', exist_ok=True)

    print('Creating and seeding SQLite database...')
    create_and_seed_db(db_path)

    print('Building schema vectorstore (Chroma) from DB schema...')
    build_schema_vectorstore(db_path, persist_directory='vectorstore/chroma')

    # print('Starting Flask app...')
    # # Start app.py
    # proc = subprocess.Popen(['python', 'app.py'])

    # # give flask some time and open browser
    # time.sleep(2)
    # webbrowser.open('http://127.0.0.1:5000')
    # proc.wait()