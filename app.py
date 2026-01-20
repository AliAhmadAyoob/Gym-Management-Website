from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/membership')
def membership():
    # Example of dynamic content: Passing a list of plans to the template
    plans = [
        {'name': 'Basic', 'price': 29, 'features': ['Gym Access', 'Locker Room']},
        {'name': 'Pro', 'price': 59, 'features': ['Gym Access', 'Group Classes', 'Guest Pass'], 'featured': True},
        {'name': 'Elite', 'price': 99, 'features': ['All Pro Features', 'Personal Trainer', 'Sauna']}
    ]
    return render_template('membership.html', plans=plans)

if __name__ == '__main__':
    app.run(debug=True)