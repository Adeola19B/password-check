from flask import Flask, render_template, request

# Create an object of the class Flask

app = Flask(__name__)


# url/
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods = ['GET', 'POST'])
def check():
    password = request.form.get('passkey')
    cat1 = False
    cat2 = False
    cat3 = False
    cat4 = False
    cat5 = False
    if len(password) >=8:
        cat1 = True
    for i in password:
        special = ["@", "$", "_", "#", "^", "&", "*", "%", "!", "+", "="]
        if i.islower():
            cat2 = True
        if i.isupper():
            cat3 = True
        if i.isdigit():
            cat4 = True
        for s in special:
            if i == s:
                cat5 = True
    if (cat1 == True) and (cat2 == True) and (cat3 == True) and (cat4 == True) and (cat5 == True):
        message = "Valid Password"
    else:
        message = "Invalid Password"
    return render_template('index.html',passkey= message)

if __name__ == '__main__':
    app.run(debug=True)