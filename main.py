from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample data for tasks
tasks = ["Add your task"]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    new_task = request.form.get('task')
    if new_task:
        tasks.append(new_task)
    return redirect('/')

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_task(index):
    if request.method == 'POST':
        updated_task = request.form.get('edited_task')
        if updated_task:
            tasks[index] = updated_task
        return redirect('/')
    else:
        return render_template('edit.html', index=index, task=tasks[index])

@app.route('/remove/<int:index>')
def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
