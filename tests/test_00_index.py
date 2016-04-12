import webhook
from flask import request, url_for

def test_00_index(app, client, live_server):
    rv = client.get('/')
    assert 'Nothing here' in rv.data
