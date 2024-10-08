from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список для зберігання записів (поки без бази даних)
records = []

@app.route('/')
def index():
    return render_template('index.html', records=records)

@app.route('/add', methods=['POST'])
def add_record():
    income = float(request.form['income'])
    tax_rate = float(request.form['tax_rate'])
    tax = income * (tax_rate / 100)
    net_income = income - tax
    
    records.append({
        'income': income,
        'tax_rate': tax_rate,
        'tax': tax,
        'net_income': net_income
    })
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
