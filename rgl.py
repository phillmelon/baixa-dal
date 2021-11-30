#!/usr/bin/python3
#coding: utf-8
#author fgomes
import os, glob, datetime, math
from platform import system #, sys
from PyPDF2 import PdfFileReader #, PdfFileMerger
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
import re

#Variáveis
rglnum = 1
rglano = datetime.datetime.now().year
alternePaginas = True
paginas = 1
folhas = 1
data = str(datetime.datetime.now().day-1).zfill(2) + "/" + str(datetime.datetime.now().month).zfill(2) + "/" + str(datetime.datetime.now().year)

#Esta função o carimbo um único arquivo RGL
def geraCarimbos(rglnum, rglano, alternePaginas, paginas, mydata):
    if (mydata != ""):
        data = mydata

    if alternePaginas:
        folhas = int(math.ceil(int(paginas) / 2) + 0.5)
    else:
        folhas = math.ceil(int(paginas) + 1)

    print("################################")
    print("RGL: " + str(rglnum) + "/" + str(rglano))
    print(str(paginas) + " págs, " + str(folhas) + " folhas.")
    if alternePaginas:
        print("Alternar páginas em branco: Sim.")
    else:
        print("Alternar páginas em branco: Não.")
    print("################################")

    ######### gerar o pdf ##########
    ### página 1: carimbo RGL
    filename = "rgl" + rglnum + "-carimbo.pdf"
    esq = 510
    topo = 835
    linha = 11

    canvas = Canvas(filename, pagesize=A4)
    canvas.setFont("Courier-Bold", 10)
    canvas.drawString(esq, topo, "--DEPAR-DAMD--")
    canvas.drawString(esq, (topo - (linha)), "RGL " + str(rglnum).zfill(7) + "/" + str(rglano))
    canvas.drawString(esq, (topo - (linha*2)), "De: " + data + "  ")
    canvas.drawString(esq, (topo - (linha*3)), "Aut c/ " + str(folhas).zfill(3) + " fls")
    canvas.drawString(esq, (topo - (linha*4)), "--------------")
    #canvas.save()

    ### loop das páginas
    folhaAtual = 1
    esq = esq + 10
    for pagina in range(2, int(paginas)+1):
        #print(">Página: " + str(pagina))
        
        ### gerar página impar em branco
        if alternePaginas and pagina % 2 == 0:
            #print("em branco")
            canvas.showPage()
        else:    
            #print("carimbo de folha")
            folhaAtual = folhaAtual + 1

            canvas.showPage()
            canvas.setFont("Courier-Bold", 10)
            canvas.drawString(esq, topo, "-DEPAR-DAMD-")
            canvas.drawString(esq, (topo - (linha)), "RGL " + str(rglnum).zfill(5) + "/" + str(rglano))
            canvas.drawString(esq, (topo - (linha*2)), "Folha:   " + str(int(folhaAtual)).zfill(3))
    ### gerar página par com carimbo de folha
    ### gera uma última página em branco: para evitar pdf de carimbo mais curto que o arquivo orginal
    canvas.showPage()

    canvas.save()

def converteDocumentosComArrobasParaPDF():
    for file in glob.glob("rgl*@.doc"):
        os.system("doc2pdf " + file)
    for file in glob.glob("rgl*@.docx"):
        os.system("doc2pdf " + file)
    for file in glob.glob("rgl*@.odt"):
        os.system("odt2pdf " + file)
    for file in glob.glob("rgl*@.jpg"):
        os.system("jpg2pdf " + file)
    for file in glob.glob("rgl*@.jpeg"):
        os.system("jpg2pdf " + file)
    for file in glob.glob("rgl*@.JPG"):
        os.system("jpg2pdf " + file)

def juntaPDFsArrobaEmUmUnicoPDFNaoCarimbado():
    #Lista os pdfs com arroba, a serem juntados
    rgl = 0
    cmd = ""
    first = True
    for file in sorted(glob.glob("rgl*@.pdf")):
        meuRGL = re.findall("\d+|$", file)[0]
        if(str(rgl) != str(meuRGL)):
            #junta os arquivos do RGL anterior
            if(first):
                cmd = "pdftk"
            else:
                first = False
                cmd = cmd + " cat output rgl" + str(rgl) + "-.pdf"
                print(cmd)
                os.system(cmd)

            #acerta a variável para o novo RGL
            rgl = meuRGL
            cmd = "pdftk"

        cmd = cmd + " " + file
        print(">>>" + file + ", RGL:" + str(rgl))
        

def carimbaRGLEPaginaFolhasEmNovoArquivoPDF():
    rglano = str(datetime.datetime.now().year)[-2:]
    data = str(datetime.datetime.now().day).zfill(2) + "/" + str(datetime.datetime.now().month).zfill(2) + "/" + str(datetime.datetime.now().year)
    paginas = 1000
    pastaDeTrabalho = "rgl*-.pdf"
    
    d = input("Data (" + data + "): ")
    if (d != ""):
        data = d

    #Lista todos os arquivos RGLs PDFs da pasta
    for file in glob.glob(pastaDeTrabalho):
        filename = os.path.basename(file)
        paginas = PdfFileReader(open(filename,'rb')).getNumPages()
        print(file + ". Nº de páginas: " + str(paginas))

        rglnum = str(re.findall("\d{4,5}", filename)[0])
        geraCarimbos(rglnum, rglano, True, paginas, data)
        filenameCarimbo = "rgl" + str(rglnum) + "-carimbo.pdf"
        filenameCarimbado = "rgl" + str(rglnum) + "-carimbado.pdf"
        print(filenameCarimbo + " ** " + filenameCarimbado)

        pdftk = "pdftk " + filename + " multistamp " + filenameCarimbo + " output " + filenameCarimbado
        #print(pdftk)
        os.system(pdftk)

#Essa função é executada por padrão.
#1) converte todos os arquivos que comecem com "rgl" e terminem com "@.doc" para pdf
#2) junta todos os arquivos "rgl...@.pdf" em um único arquico "rgl...-.pdf"
#3) carimba o rgl e as folhas dos arquvios "rgl...-.pdf"
if __name__ == '__main__':
    print("****** Carimbando RGLs (DAMD-ALESP) ******")
    converteDocumentosComArrobasParaPDF()
    juntaPDFsArrobaEmUmUnicoPDFNaoCarimbado()
    carimbaRGLEPaginaFolhasEmNovoArquivoPDF()
