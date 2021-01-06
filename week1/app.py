from flask import Flask, render_template, url_for, flash, redirect
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms import Form, TextAreaField, TextField, SubmitField, StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


class ReviewForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    product = StringField(
        'Product Name', validators=[DataRequired()])
    review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Publish Review')


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        flash('Review Sumbitted', 'success')
        return redirect(url_for('review'))
    else:
        flash('Unsuccessful. Please check again', 'danger')
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
