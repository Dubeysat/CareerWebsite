from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'Salary': 'Rs. 10,00,000',
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Bengaluru, India',
    'Salary': 'Rs. 15,00,000',
  },
  {
    'id': 3,
    'title': 'General labour',
    'location': 'Bengaluru, India',
    'Salary': 'Rs. 2,50,000',
  },
  {
    'id': 4,
    'title': 'CARE TAKER',
    'location': 'Bengaluru, India',
  },
]


@app.route("/")
def hello_world():
  return render_template('Home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
