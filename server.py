from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'denvernuggets'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(name) < 1:
        flash(f"Name cannot be empty!")
        return redirect('/')
    if len(comment) < 1:
        flash(f"Comment cannot be empty!")
        return redirect('/')
    if len(comment) > 120:
        flash(f"Comment is too long, must be less than 120 characters!")
        return redirect('/')
    else:
        flash(f"Thank you {name} for filling up the survey!")
        return render_template('results.html', name = name, location = location, language = language, comment = comment)

if __name__ == "__main__":
    #run our server
    app.run(debug=True)