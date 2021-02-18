from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('splash.html')


# Example page for adding to a 'Bands' list, that lets you search bands
@app.route('/addBand/', methods=['GET', 'POST'])
def addBand():
    # If this page receives a post request...
    if request.method == 'POST':
        # Process whatever data has been received, then redirect to main page, or elsewhere as needed
        # "bands.insert(request.form['name'])
        return redirect(url_for('index'))
    else:
        # Otherwise, render the page
        return render_template('addBand.html')


@app.route('/artistPage/', methods=['GET'])
def artist():
    return render_template('artistPage.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
