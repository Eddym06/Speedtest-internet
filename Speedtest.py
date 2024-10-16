from flask import Flask, jsonify
import speedtest

app = Flask(__name__)


@app.route('/medir_velocidad', methods=['GET'])
def medir_velocidad():
    test = speedtest.Speedtest()
    download_bps = test.download()
    upload_bps = test.upload()

    # Convertir de bits por segundo (bps) a megabytes por segundo (MBps)
    download_mbps = download_bps / (1024 * 1024) / 8
    upload_mbps = upload_bps / (1024 * 1024) / 8

    return jsonify({
        'download': download_mbps,
        'upload': upload_mbps
    })


if __name__ == '__main__':
    app.run(debug=True)
