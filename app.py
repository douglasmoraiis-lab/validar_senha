from flask import Flask, render_template, request
import os

app = Flask(__name__)

# -----------------------------
# Função de validação de senha
# -----------------------------
def validar_senha(senha: str):
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

# -----------------------------
# Rota principal
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    erros = []
    senha = ""
    if request.method == "POST":
        senha = request.form.get("senha", "")
        erros = validar_senha(senha)
    return render_template("index.html", erros=erros, senha=senha)

# -----------------------------
# Execução do app
# -----------------------------
if __name__ == "__main__":
    # Define modo debug pelo ambiente
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug_mode)
