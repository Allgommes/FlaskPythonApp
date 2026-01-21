# app.py: Main Flask application file

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # _Flask(__name__) creates the Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # Database configuration
db = SQLAlchemy(app)  # SQLAlchemy initializes the database connection

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET']) # @app.route('/') connects the home URL (/) to a function
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
         
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)  # Renders the index.html template

#@app.route('/testelayout')
#def testelayout():
#    return render_template('testelayout.html')  # Renders the testelayout.html template

if __name__  == "__main__":
    app.run(debug=True)  # app.run() starts the local server
    
    # if __name__ == "__main__":
    # app.run(debug=True, port=<desired port>)