from flask import Flask, render_template, request

app = Flask(__name__)

# "banco de dados" temporário em memória
produtos = []

@app.route("/")
def index():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    produto = {
        "nome": request.form["nome"],
        "descricao": request.form["descricao"],
        "preco": request.form["preco"],
        "quantidade": request.form["quantidade"],
        "categoria": request.form["categoria"],
        "imagem": request.form["imagem"]
    }

    produtos.append(produto)

    return f"Produto cadastrado com sucesso! Total: {len(produtos)}"

if __name__ == "__main__":
    app.run(debug=True)