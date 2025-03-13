# PASSO A PASSO - FLASK WEB SERVER

---

## Estrutura do Projeto

```
 app.py - Boas práticas
 /static
	  /css
	  /img
    /js - JavaScript
/templates - modelo ou layout pronto
	  index.html
		add produto
		del produto...
---

## Arquivo Principal: `app.py`

Este arquivo inicializa o servidor Flask e define as rotas principais do sistema:

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
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
```

---

## Estrutura de Arquivos Estáticos

A pasta `static` contém três subpastas:

- `/css`: Arquivos CSS para estilização.
- `/img`: Imagens utilizadas no site.
- `/js`: Arquivos JavaScript para interatividade.

Os estilos são organizados por funcionalidade:

- `styleAddProduto.css`: Estilização da página de adição de produto.
- `styleDelProduto.css`: Estilização da página de deleção de produto.
- `styleNav.css`: Estilização do menu de navegação.
- `styleFooter.css`: Estilização do rodapé.

---

## Templates HTML

Os templates são armazenados na pasta `templates`, seguindo o padrão de herança do Jinja2.

### `index.html`

Arquivo base para todas as páginas:

```
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/styleNav.css')}}">
    <link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/styleFooter.css')}}">

    {% block link %}
    {% endblock %}

    <title>MEU SERVER</title>
</head>
<body>
    {% include "nav.html" %}

    {% block body %}
    {% endblock %}

    {% include "footer.html" %}
</body>
</html>
```

### `add_produtos.html`

```
{% extends "index.html" %}

{% block link %}
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/styleAddProduto.css') }}">
{% endblock %}

{% block body %}
    <h1>ADICIONAR PRODUTO</h1>
{% endblock %}
```

### `del_produtos.html`

```
{% extends "index.html" %}

{% block link %}
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/styleDelProduto.css') }}">
{% endblock %}

{% block body %}
    <h1>DELETAR PRODUTOS</h1>
{% endblock %}
```

### `nav.html`

```
<nav>
    <ul>
        <li>homepage</li>
        <li>adicionar</li>
        <li>deletar</li>
        <li>atualizar</li>
    </ul>
</nav>
```

---

## Inicialização do Servidor

Para iniciar o servidor Flask, execute o seguinte comando no terminal:

```
python app.py
```

O servidor rodará no endereço `http://0.0.0.0:5000`.
