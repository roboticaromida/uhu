from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Base de datos de ejemplo (esto luego irá en una DB real)
licencias = {
    "123456": {"usuario": "Cliente1", "expiracion": "2025-12-31"},
    "ABCDEF": {"usuario": "Cliente2", "expiracion": "2024-06-30"},
}

# Ruta para verificar la licencia
@app.route("/verificar_licencia", methods=["POST"])
def verificar_licencia():
    datos = request.json
    licencia = datos.get("licencia")

    if licencia in licencias:
        exp_date = datetime.datetime.strptime(licencias[licencia]["expiracion"], "%Y-%m-%d")
        dias_restantes = (exp_date - datetime.datetime.now()).days

        return jsonify({
            "status": "valida" if dias_restantes > 0 else "expirada",
            "usuario": licencias[licencia]["usuario"],
            "expira_en": licencias[licencia]["expiracion"],
            "dias_restantes": dias_restantes
        })
    
    return jsonify({"status": "invalida"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
