from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    search_query = request.args.get('q')
    sort = request.args.get('sort', 'name')  # default sort by name

    valid_sorts = {'name': 'b.name', 'avg_weight': 'b.avg_weight'}
    order_by = valid_sorts.get(sort, 'b.name')

    conn = get_db_connection()
    if search_query:
        birds = conn.execute(f'''
            SELECT b.id, b.name, b.avg_weight, d.description
            FROM birds b
            LEFT JOIN bird_descriptions d ON b.id = d.bird_id
            WHERE b.name LIKE ?
            ORDER BY {order_by} COLLATE NOCASE
        ''', (f'%{search_query}%',)).fetchall()
    else:
        birds = conn.execute(f'''
            SELECT b.id, b.name, b.avg_weight, d.description
            FROM birds b
            LEFT JOIN bird_descriptions d ON b.id = d.bird_id
            ORDER BY {order_by} COLLATE NOCASE
        ''').fetchall()
    conn.close()
    return render_template('index.html', birds=birds)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    description = request.form['description']
    avg_weight = request.form.get('avg_weight', type=float)

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO birds (name, avg_weight) VALUES (?, ?)", (name, avg_weight))
    bird_id = cur.lastrowid
    cur.execute("INSERT INTO bird_descriptions (bird_id, description) VALUES (?, ?)", (bird_id, description))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM birds WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        avg_weight = request.form.get('avg_weight', type=float)
        conn.execute("UPDATE birds SET name = ?, avg_weight = ? WHERE id = ?", (name, avg_weight, id))
        conn.execute("UPDATE bird_descriptions SET description = ? WHERE bird_id = ?", (description, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        bird = conn.execute('''
            SELECT b.id, b.name, b.avg_weight, d.description
            FROM birds b LEFT JOIN bird_descriptions d ON b.id = d.bird_id
            WHERE b.id = ?
        ''', (id,)).fetchone()
        conn.close()
        return render_template('edit.html', bird=bird)

if __name__ == '__main__':
    app.run(debug=True)
