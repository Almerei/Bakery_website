from flask import Flask, render_template, jsonify
from database import load_bakers_from_db,load_job_from_db

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

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  
  if not job:
    return "Job not found", 404
    
  return render_template('menu.html',
                        job=job)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)