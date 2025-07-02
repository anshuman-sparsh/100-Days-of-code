from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile', methods=['POST'])
def profile():
    username = request.form.get('username')
    url = f"https://api.github.com/users/{username}"

    try:
        res = requests.get(url)
        if res.status_code == 404:
            return render_template('result.html', error="User not found.")

        data = res.json()
        return render_template('result.html', data=data)

    except Exception as e:
        return render_template('result.html', error=str(e))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=3000)
