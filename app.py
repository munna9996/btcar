from flask import Flask, render_template, request

app = Flask(_name_)

# Sample data for available cabs
available_cabs = [
    {"type": "Sedan", "price": 10},
    {"type": "SUV", "price": 15},
    {"type": "Luxury", "price": 20}
]

@app.route('/', methods=['GET', 'POST'])
def explore_cabs():
    if request.method == 'POST':
        pickup_location = request.form['pickup_location']
        drop_location = request.form['drop_location']
        pickup_date = request.form['pickup_date']

        # Perform any necessary processing based on user input

        # Pass available cabs data to the template
        return render_template('explore_cabs.html', available_cabs=available_cabs)

    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)
