from flask import Flask, request, send_file, render_template
import os
import PyPDF2

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('hub.html')

@app.route('/fusionner', methods=['POST'])
def fusionner():
    fichiers = request.files.getlist('fichiers[]')
    nom_sortie = fusionner_pdf([fichier for fichier in fichiers])
    return send_file(nom_sortie, as_attachment=True)

def fusionner_pdf(fichiers):
    fusionneur = PyPDF2.PdfMerger()

    for fichier in fichiers:
        if fichier.filename.endswith(".pdf"):
            fusionneur.append(fichier)

    nom_sortie = 'fusion.pdf'

    with open(nom_sortie, 'wb') as fichier_sortie:
        fusionneur.write(fichier_sortie)

    return nom_sortie

if __name__ == '__main__':
    app.run(debug=True)
