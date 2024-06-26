from datetime import datetime
from urllib.parse import urlparse

from flask import make_response, render_template

from ..models import HatComponent
from . import main


def extract_text_id(text_id):
    parsed_url = urlparse(text_id)
    path_parts = parsed_url.path.split('/')
    new_text_id = path_parts[-2]  # text_id is the second last part of the path
    return new_text_id

@main.route('/')
def index():
   hat_components = HatComponent.query.all()

   response = make_response(
       render_template('index.html', hat_components=hat_components))
   response.set_etag('some_etag')
   response.headers['Last-Modified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


   return response