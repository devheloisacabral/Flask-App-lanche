from flask import Flask, render_template
from lanche import Lanche

app = Flask(__name__)

pao = Lanche(1, "Pão com Ovos", "R$7,50", "* Pão * Ovo * Manteiga * Maionese * Salada", 'img/pao-com-ovo.jpg')
sanduiche = Lanche(2, "Sanduíche natural", "R$6,00", "* Alface * Tomate * Cebola * Frango * Pão de forma integral", 'img/sanduiche.png')
hamburguer = Lanche(3, "Hamburguer Assado", "R$8,00", "* Alface * Tomate * Cebola * Maionese * Pão de hamburger", 'img/hamburguer-assado.jpg')
lanches_cardapio = [pao, sanduiche, hamburguer]


@app.route('/')
def descricao_lanche():
    return render_template('principal_lanche.html', lanches=lanches_cardapio) 

@app.route("/individual/<int:id>")
def descricao_individual(id:int):
    for lanchee in lanches_cardapio:
        if lanchee.id == id:
            return render_template("descricao_individual_lanche.html", lanche = lanchee)
    return "<h1>Ops! Lanche não encontrado!</h1>"
            
if __name__ == '__main__':
    app.run(debug=True)