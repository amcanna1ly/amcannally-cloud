# Import the Flask class from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Use the route() decorator to define a route for the root URL ("/")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Start the Flask development server with debug mode enabled
    app.run(debug=True)
