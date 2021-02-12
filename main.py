from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('splash.html')


# Example page for adding to a 'Bands' list, that lets you search bands
@app.route('/addBand/', methods=['GET', 'POST'])
def about():
    # If this page receives a post request...
    if request.method == 'POST':
        # Process whatever data has been received, then redirect to main page, or elsewhere as needed
        # "bands.insert(request.form['name'])
        return redirect(url_for('index'))
    else:
        # Otherwise, render the page
        return render_template('samplePage.html')
