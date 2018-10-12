import flask
import json
from flask import request
from forms import AdminForm

app = flask.Flask(__name__)
app.debug = True
app.secret_key = 'super_secret'

@app.route("/")
def main():
	content = 'This will be the menu of topics / pages'
    return flask.render_template('menu.html', content=content)


@app.route('/admin/<path:page>', methods=['GET', 'POST'])
def admin(page):

    # Successful form submission
    if request.method == 'POST':
        form = Admin()
        if form.validate_on_submit():
            data = form.data
            # Remove 'csrf_token' and 'submit' before writing to disk
            del data['csrf_token']
            del data['submit']
            data = json.dumps(data)
            # write data to file

    # Don't overwrite form if not validated
    if request.method == 'GET' or form.validate_on_submit():
    	# Read data from file
        json_data = json.loads()
        form = AdminForm(**json_data)

    return flask.render_template('form.html', form=form)

# Data in files will just be an array of key, value pairs; Maybe like this:
# [
#  { "key-one": "value-one" },
#  { "key-two": "value-two" }
# ]