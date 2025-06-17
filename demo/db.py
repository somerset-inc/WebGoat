import os
from flask import Flask, request, g
import sqlite3
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)
app.config['DATABASE'] = 'database.db'

# Initialize the OpenAI client with the API key from environment variables
# It's crucial to securely manage your API key. Using environment variables is recommended.
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route('/users')
def index():
    """
    Main route that displays the form and shows the constructed SQL query.
    """
    username = request.args.get('username') 
    password = request.args.get('password') 
    query = "INSERT INTO users (username, password) VALUES (?, ?)"

    db = sqlite3.connect(
            app.config['DATABASE'],
            detect_threads=False 
        )
    
    # execute query
    cursor = db.cursor()
    cursor.execute(query, (username, password))
    db.commit()
    return {"msg": "success"}
