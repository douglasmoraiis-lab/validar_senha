from flask import Flask, render_template, request

app = Flask(__name__)

def validar_senha(senha):
    erros = []
    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")
    if not any(c.isupper() for c in senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")
    if not any(c.islower() for c in senha):
        erros.append("A senha deve conter pelo menos uma letra minúscula.")
    if not any(c.isdigit() for c in senha):
        erros.append("A senha deve conter pelo menos um número.")
    if not any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in senha):
        erros.append("A senha deve conter pelo menos um caractere especial.")
    return erros

@app.route("/", methods=["GET", "POST"])
def index():
    erros = []
    senha = ""
    if request.method == "POST":
        senha = request.form.get("senha", "")
        erros = validar_senha(senha)
    return render_template("index.html", erros=erros, senha=senha)

if __name__ == "__main__":
    app.run(debug=True)
