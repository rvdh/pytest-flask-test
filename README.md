# pytest-flask-test

```
$ py.test
================================= test session starts ==================================
platform darwin -- Python 2.7.10 -- py-1.4.30 -- pytest-2.7.2
rootdir: /Users/rick/Documents/test, inifile:
plugins: cov, flask, mock
collected 1 items

tests/test_00_index.py F

======================================= FAILURES =======================================
____________________________________ test_00_index _____________________________________

app = <Flask 'webhook'>, client = <FlaskClient <Flask 'webhook'>>
live_server = <LiveServer listening at http://localhost:60070>

    def test_00_index(app, client, live_server):
        rv = client.get('/')
>       assert 'Nothing here' in rv.data
E       assert 'Nothing here' in '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>\n'
E        +  where '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>404 Not Found</title>\n<h1>Not Found</h1>\n<p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>\n' = <<class 'pytest_flask.plugin.JSONResponse'> 233 bytes [404 NOT FOUND]>.data

tests/test_00_index.py:6: AssertionError
-------------------------------- Captured stderr setup ---------------------------------
 * Running on http://127.0.0.1:60070/ (Press CTRL+C to quit)
127.0.0.1 - - [12/Apr/2016 22:05:59] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [12/Apr/2016 22:06:00] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [12/Apr/2016 22:06:01] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [12/Apr/2016 22:06:02] "GET / HTTP/1.1" 404 -
127.0.0.1 - - [12/Apr/2016 22:06:03] "GET / HTTP/1.1" 404 -
=============================== 1 failed in 5.09 seconds ===============================
$
```
