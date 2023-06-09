from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    else:
        return '''
            <form method="post">
                <label for="name">Enter your name:</label>
                <input type="text" id="name" name="name">
                <input type="submit" value="Submit">
            </form>
        '''
if __name__ == "__main__":
	app.run()
