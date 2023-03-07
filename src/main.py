

import flask 
app = flask.Flask(__name__)  
@app.route('/') 
def home():     
    return '<h1>Welcome to Patrick's House Website</h1>'   if __name__ == "__main__":     app.run()