from flask import Flask, jsonify, render_template
import speedtest

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

def rodar_teste_de_velociadade():
    #executa o teste de velocidade e devolve os resultados em Mbps
    teste = speedtest.Speedtest()

    download_bps = teste.download()  # velocidade de download em bits por segundo
    upload_bps = teste.upload()      # velocidade de upload em bits por segundo

    return {
        "download_mbps": round(download_bps / 1_000_000,2),
        "upload_mbps": round(upload_bps / 1_000_000,2),
        }

@app.route("/api/speedtest", methods=['GET'])

def speedtest_endpoint():
    try:
        resultado = rodar_teste_de_velociade()
        return jsonify(resultado), 200
    except Exception as erro:
        return jsonify({"erro": f"Falha ao rodar o teste: {type(erro).__name__}: {erro}"}), 503

@app.route("/api/health", methods=['GET'])
def helth():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
                        