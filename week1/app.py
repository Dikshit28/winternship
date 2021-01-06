from flask import Flask, render_template, request


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
posts = [
    {
        'Name': 'abcd',
        'Product Name': 'cooler',
        'Review': 'nice'
    },
    {
        'Name': 'efgh',
        'Product Name': 'heater',
        'Review': 'lmao'
    },
    {
        'Name': 'ijkl',
        'Product Name': 'machine',
        'Review': 'lol'
    }
]


@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form)
        posts.insert(
            0,
            {
                'Name': request.form.get('name'),
                'Product Name': request.form.get('product'),
                'Review': request.form.get('review')
            }
        )
    return render_template('index.jinja2', reviews=posts)


if __name__ == "__main__":
    app.run(debug=True)
