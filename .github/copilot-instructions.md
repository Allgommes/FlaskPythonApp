# Copilot Instructions - FlaskPythonApp

## Project Overview
Simple Flask-based TODO list application using SQLAlchemy ORM with SQLite database. Single-file monolithic architecture in `app.py` with Jinja2 templating.

## Architecture Patterns

### Application Structure
- **Single-file app**: All routes, models, and database config in [app.py](../app.py)
- **Database**: SQLite (`test.db`) configured via `SQLALCHEMY_DATABASE_URI`
- **Template inheritance**: [base.html](../templates/base.html) provides layout with `{% block head %}` and `{% block body %}` blocks
- **Static assets**: CSS in [static/css/main.css](../static/css/main.css), linked via `url_for('static', filename='css/main.css')`

### Database Model Pattern
```python
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)  # Note: uses Integer (0/1) not Boolean
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
```
**Important**: The `completed` field uses Integer type (0/1) instead of Boolean - maintain this pattern.

### Route Conventions
- Combined GET/POST handlers: Use `methods=['POST', 'GET']` on single route
- Form handling: Access via `request.form['field_name']`
- Redirects: Always `return redirect('/')` after POST operations (PRG pattern)
- Error handling: Currently uses bare `except` - when adding error handling, catch specific exceptions

## Development Workflow

### Environment Setup
```powershell
# Activate virtual environment (Windows)
.\env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py  # Runs on http://localhost:5000
```

### Database Initialization
The database (`test.db`) is created automatically on first run. To reset:
1. Delete `test.db` file
2. In Python shell: `from app import db; db.create_all()`

### Running the Application
- Default port: 5000 (configurable in `app.run()` call)
- Debug mode is enabled in development
- Templates auto-reload in debug mode

## Code Conventions

### Template Rendering
- Use Portuguese for UI labels (e.g., "Task Master" title)
- Date formatting: `{{ task.date_created.date() }}` to show date only
- Jinja2 loops: `{% for task in tasks %}` pattern for displaying lists

### Database Operations
```python
# Add pattern
new_task = Todo(content=task_content)
db.session.add(new_task)
db.session.commit()

# Query pattern
tasks = Todo.query.order_by(Todo.date_created).all()
```

### Styling Approach
- Centered content layout: `.content { margin: 0 auto; width: 400px; }`
- Light blue background (`lightblue`)
- Tables with collapsed borders (`border-collapse: collapse`)

## Known Issues & Patterns

### Incomplete Features
- Delete/Update links in [index.html](../templates/index.html) are placeholders (`href=""`) - not implemented
- Conditional rendering check (`{% endif %}`) without matching `{% if %}` - template syntax error exists

### Dependencies
Uses older Flask 1.1.2 stack (archived project). When updating:
- Pin compatible versions for Flask-SQLAlchemy, Werkzeug, Jinja2
- Test database migrations after major SQLAlchemy upgrades

## Adding New Features

### Adding Routes
Place new routes in [app.py](../app.py) before the `if __name__ == "__main__"` block.

### Adding Templates
1. Create in `templates/` directory
2. Extend base: `{% extends 'base.html' %}`
3. Override blocks: `{% block head %}` for title, `{% block body %}` for content

### Database Schema Changes
After modifying `Todo` model or adding new models, reinitialize the database (no migrations configured).
