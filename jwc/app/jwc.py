from flask import jsonify, url_for, request, redirect
from app import app
from app.scraping import Scraping
from app.form import FormData


scrap = Scraping()


@app.route('/check_code')
def check_code():
    scrap.crow_check_code()
    return app.send_static_file('check_code.jpg')


@app.route('/scraping')
def scraping():
    form_data = FormData().get_data(request)
    data = scrap.crow_date(form_data)
    return jsonify(data)

