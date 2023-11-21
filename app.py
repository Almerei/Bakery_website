from flask import Flask, render_template, jsonify
from database import load_bakers_from_db

app = Flask(__name__)

@app.route("/")
def  hello_world():
  bakers = load_bakers_from_db()
  return render_template('bakery.html',
                        jobs=bakers,
                        company_name='Lana_bakery')


@app.route("/api/jobs")
def list_jobs():
  bakers = load_bakers_from_db()
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)