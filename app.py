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
  return jsonify(bakers)

# Ваш код Flask-приложения

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    return render_template ('menu.html',
                           job=job)

@app.route("/cart")
def show_cart():
    # Add logic to render the cart page
    return render_template('cart.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)