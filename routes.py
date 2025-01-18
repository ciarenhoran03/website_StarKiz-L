from flask import Flask, render_template
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():  # Pastikan ada fungsi yang terkait dengan rute ini
    return render_template('about.html')

@app.route('/business')
def business():
    # Mungkin tambahkan data usaha di sini
    return render_template('business.html')

if __name__ == '__main__':
    app.run(host='192.168.18.102', port=5000)
