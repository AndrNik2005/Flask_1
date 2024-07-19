from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('base.html')



@app.route('/category/<category_name>')
def category(category_name):
    subcategories = {
        'jumpers': ['Коллекция 2021 - 2024'],
        'cardigans': ['Коллекция 2023 - 2024'],
        'accessories': ['Коллекция 2024']
    }
    return render_template('category.html', category_name=category_name.capitalize(), subcategories=subcategories[category_name])



@app.route('/category/<category_name>/<subcategory_name>')
def subcategory(category_name, subcategory_name):

    return render_template('subcategory.html', category_name=category_name.capitalize(), subcategory_name=subcategory_name)


if __name__ == '__main__':
    app.run(debug=True)