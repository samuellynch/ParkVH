from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Samuel'} '#fakeuser'
    return '''
<html>
    <head>
        <title>Home page</title>
    </head>
    <body>
        <h1>Hello, ''' + user['nickname'] + '''</h1>
</html>
'''

