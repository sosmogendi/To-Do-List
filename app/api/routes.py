from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models import Task
from app.forms import TaskForm, UpdateTaskForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = TaskForm()
    tasks = Task.query.all()

    if form.validate_on_submit():
        new_task = Task(title=form.title.data)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('index.html', tasks=tasks, form=form)

@main.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    form = UpdateTaskForm()

    if form.validate_on_submit():
        task.is_complete = form.is_complete.data
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'danger')
    return redirect(url_for('main.index'))

