# 🔹 3. Proposal Preview (Mock GSoC)
# Create a .txt or .md file with a sample GSoC proposal idea
# Flask route: /proposal
# Read and display that file content in HTML




from flask import Flask, render_template

app = Flask(__name__)

@app.route('/proposal')
def proposal():
    try:
        with open('Day 29/proposal.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        content = "Proposal file not found. Please ensure proposal.txt exists."
    return render_template('proposal.html', proposal_text=content)

if __name__ == '__main__':
    app.run(debug=True)

# python "Day 29/app3.py"
# http://127.0.0.1:5000/proposal