# app.py: Main Flask application file

from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

app = Flask(__name__) # _Flask(__name__) creates the Flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # Database configuration
db = SQLAlchemy(app)  # SQLAlchemy initializes the database connection

class Todo(db.Model):
    id = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    completed = Column(Integer, default=0)
    date_created = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/', methods=['POST', 'GET']) # @app.route('/') connects the home URL (/) to a function
def index():
    if request.method == 'POST':  
        task_content = request.form.get('content')  # Usar .get para evitar erros
        new_task = Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'Houve um problema ao adicionar a tarefa: {e}'
         
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)  # Renders the index.html template

#@app.route('/testelayout')
#def testelayout():
#    return render_template('testelayout.html')  # Renders the testelayout.html template

@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f'Houve um problema ao deletar a tarefa: {e}'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    
    if request.method == 'POST':
        task_to_update.content = request.form.get('content')
        
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f'Houve um problema ao atualizar a tarefa: {e}'
    
    else:
        return render_template('update.html', task=task_to_update)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()    


if __name__  == "__main__":
    app.run(debug=True)  # app.run() starts the local server
    
    # if __name__ == "__main__":
    # app.run(debug=True, port=<desired port>)