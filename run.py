import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from app import create_app, db, db_conn
from app.models import User
 
app = create_app(os.getenv('FLASK_CONFIG') or 'default') 

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'db_conn': db_conn}

if __name__ == "__main__":
    app.run(debug=True, port='4000')
