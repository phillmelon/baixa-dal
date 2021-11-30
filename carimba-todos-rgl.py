#!/usr/bin/python3
#coding: utf-8
#author fgomes
from rgl import hello, geraCarimbos
import os, glob, sys, datetime
from PyPDF2 import PdfFileMerger, PdfFileReader
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
import argparse
import re
#Padrão de nomes de arquivos
#rgl-00000-.pdf             (hifem no fim: propositura a ser carimbada)
#rgl-00000-carimbo.pdf      (carimbo a ser sobreposto na propositura)
#rgl-00000-carimbada.pdf    (propositura com o carimbo)

#Variáveis
rglano = str(datetime.datetime.now().year)[-2:]
data = str(datetime.datetime.now().day).zfill(2) + "/" + str(datetime.datetime.now().month).zfill(2) + "/" + str(datetime.datetime.now().year)
paginas = 1000
pastaDeTrabalho = "rgl*-.pdf"
print("****** Carimbando RGLs ******")

d = input("Data (" + data + "): ")
if (d != ""):
    data = d

#Converte documentos para pdf
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

for file in glob.glob("rgl*@.pdf"):
    print(">>>" + file)

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
