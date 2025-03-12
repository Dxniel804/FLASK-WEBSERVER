from flask import Flask, render_template

app = Flask(__name__)

@app.route('/homepage')
def homepage():
    context = {}
    return render_template("homepage.html", context=context)

@app.route('/add_produto')
def add_produto():
    context = {}
    return render_template("add_produtos.html", context=context)

@app.route('/del_produto')
def del_produto():
    context = {}
    return render_template("del_produtos.html", context=context)

@app.route('/up_produto')
def up_produto():
    context = {}
    return render_template("up_produtos.html", context=context)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
