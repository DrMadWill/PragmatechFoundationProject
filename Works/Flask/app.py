from flask import Flask 

app=Flask(__name__)
ad='Samir'
@app.route('/')
def index():
    return f'<h1>Hello {ad}</h1>'


if __name__=='__main__':
    app.run(debug=True) 