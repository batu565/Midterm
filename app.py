
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQLdb

app = Flask(__name__,template_folder='template')

# def search_in_database(search_term):
#     conn = MySQLdb.connect(host="3306", user="root", passwd="123456", db="toy_store")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM search_data WHERE content LIKE %s", ('%' + search_term + '%',))
#     rows = cursor.fetchall()
#     conn.close()
#     return rows


def search_results():
    
    items = [
        {
            "name": "Blue Car",
            "price": 10.99,
            "image_url": "C:\Users\batuh\OneDrive\Masaüstü\new\template\images\format_webp.png"
        },
        {
            "name": "Item 2",
            "price": 19.99,
            "image_url": "path/to/item2.png"
        },
        {
            "name": "Item 3",
            "price": 15.49,
            "image_url": "path/to/item3.png"
        },
        # Add more items with their details as needed
    ]
    return render_template('search_results.html', items=items)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == 'POST':
#         search_term = request.form.get('search', '')
#         return render_template(url_for('search_results', search=search_term))
#     return redirect(url_for('home'))  # Redirect to home page if accessed via GET request

# @app.route('/search_results')
# def search_results():
#     search_term = request.args.get('search', '')
#     if search_term:
#         products = search_in_database(search_term)
#         return render_template('search_results.html', search_term=search_term, products=products)
#     else:
#         return redirect(url_for('home'))  # Redirect to home page if no search term provided


if __name__ == '__main__':
    app.debug= True
    app.run()
