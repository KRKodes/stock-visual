from dotenv import load_dotenv
import os
import requests
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from datetime import datetime
from help import error, lookup, usd
from alpha_vantage.techindicators import TechIndicators

# Configure application
app = Flask(__name__)

load_dotenv('trying.env')


# Custom filter
app.jinja_env.filters["usd"] = usd

db = SQL("sqlite:///finance.db")

# Function to get the current count


def get_count():
    result = db.execute('SELECT count FROM api_calls WHERE id = 1')
    return result[0]['count']


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    today = datetime.now().date()
    result = db.execute('SELECT count, date FROM api_calls WHERE id = 1')
    if not result:
        return error("Failed to retrieve data from the database.", 500)
    else:
        count = result[0]['count']
        last_date = result[0]['date']

        if last_date != str(today):
            # Reset count if the date is different
            db.execute('UPDATE api_calls SET count = 0, date = ? WHERE id = 1', today)
            count = 0

        if count >= 10:
            return render_template("index.html", message="Only 10 API calls allowed per day, come back tomorrow.")
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    if not api_key:
        return error("API key is missing.", 400)
    return render_template("index.html", api_key=api_key, message=None)


@app.route("/increment-count", methods=["POST"])
def increment_count():
    today = datetime.now().date()
    result = db.execute('SELECT count, date FROM api_calls WHERE id = 1')

    if result:
        count = result[0]['count']
        last_date = result[0]['date']

        if last_date == str(today):
            count += 1
            db.execute('UPDATE api_calls SET count = ? WHERE id = 1', count)
        else:
            count = 1
            db.execute('UPDATE api_calls SET count = ?, date = ? WHERE id = 1', count, today)

    return jsonify({"count": count})


@app.route("/fetch", methods=["POST"])
def fetch():
    indicator = request.form.get("indicator")
    symbol = request.form.get("symbol")
    interval = request.form.get("interval")
    time_period = request.form.get("time_period")
    series_type = request.form.get("series_type")
    if not indicator or not symbol or not interval or not time_period or not series_type:
        return error("Missing or invalid form data.", 400)
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

    url = f"https://www.alphavantage.co/query?function={indicator}&symbol={symbol}&interval={interval}&time_period={time_period}&series_type={series_type}&apikey={api_key}"

    response = requests.get(url)
    if response.status_code != 200:
        return error("Failed to fetch data from the API.", 500)
    data = response.json()

    print(data)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
