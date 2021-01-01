import os
from docxtpl import DocxTemplate


def check_dir(path='./files'):
    check = os.path.exists(path)

    if check == False:
        os.mkdir(path)


def create_file(name, data, yes, path='./files/'):
    check_dir(path)
    doc = DocxTemplate(path + "шаблон.docx")
    context = {'name': name, 'data': data, 'yes': yes}

    doc.render(context)
    doc.save(path + name + ".docx")