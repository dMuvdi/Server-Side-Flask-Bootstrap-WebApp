from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/document', methods=['GET', 'POST'])
def document():
    return render_template('document.html')


@app.route('/document_detail', methods=['POST'])
def document_detail():
    id_doc = request.form['id_doc']
    title = request.form['title']
    pag_num = request.form['pag_num']
    categ = request.form['categ']
    id_person = request.form['id_person']
    name = request.form['name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=name, last_name=last_name)
    d = Document(id_doc=id_doc, title=title, pag_num=pag_num, categ=categ, authors=p)
    model.append(d)
    return render_template('document_detail.html', value=d)


@app.route('/documents')
def documents():
    data = [(i.id_doc, i.title, i.pag_num, i.categ, i.authors.id_person, i.authors.name, i.authors.last_name) for i in model]
    print(data)
    return render_template('documents.html', value=data)


@app.route('/document_deleted/<id>', methods=['POST'])
def delete(id):
    for doc in model:
        if doc.id_doc == id:
            model.remove(doc)
            break
    return render_template('document_deleted.html')

@app.route('/about')
def about_us():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug = True)