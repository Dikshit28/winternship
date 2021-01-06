from flask import Flask, render_template, url_for, flash, redirect
from wtforms import Form, TextAreaField, TextField, validators, SubmitField

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
class ReviewForm(Form):
    fname = TextField('First Name*', validators=[validators.DataRequired()])
    product = TextField(
        'Product Name*', validators=[validators.DataRequired()])
    review = TextAreaField('Review*', validators=[validators.DataRequired()])
    submit = SubmitField('Publish Review')


def review():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('Review Sumbitted', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
