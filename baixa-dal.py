#!/usr/bin/python
#coding: utf-8
#author fgomes
import os, glob, sys, datetime
from urllib2 import urlopen, URLError, HTTPError
from PyPDF2 import PdfFileMerger, PdfFileReader
import argparse

#Data da edicao de hoje
AGORA = datetime.datetime.now()
ANO=str(AGORA.year)
#MESES=["Janeiro","Fevereiro","MarÃ§o","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
MESES=["Janeiro","Fevereiro","Mar%C3%A7o","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
MES=AGORA.month
DIA=str(AGORA.day)

#Informar a pagina inicial e final mÃ¡ximos
PG1=1
PG2=9999

#url da navegacao do DOE, onde podemos pegar o numero de paginas do DOE
#http://diariooficial.imprensaoficial.com.br/nav_v4/header.asp?txtData=27/09/2017&cad=12&cedic=&pg=&acao=&edicao=&secao=

###########################
# Prepara o diretorio e   #
# apaga pdfs antigos.     #
###########################
def preparaDiretorio(dirmes):
  if not os.path.exists(dirmes):
    os.makedirs(dirmes)

  #apaga pdfs antigos
  files = glob.glob(os.getcwd() + os.sep + "*.pdf")
  for f in files:
    os.remove(f)

######################
# Funcao de download #
######################
def dlfile(url):
  # Open the url
    #try:
      f = urlopen(url)
      #print "downloading " + url

      # Open our local file for writing
      with open(os.path.basename(url), "wb") as local_file:
        local_file.write(f.read())

###########################
# Baixa as paginas do DOE #
###########################
def baixaPaginas(ano, mes, dia):
  try:
    #print("Downloading..." + str(ano) + str(mes) + str(dia))
    print("Download do DOE, pag: "),
    sys.stdout.flush()
    for page in range(PG1, (PG2+1)):
      print(str(page) + ","),
      sys.stdout.flush()
      nomedoarquivo = "pg_" + str(page).zfill(4) + ".pdf"
      urldapagina = "http://diariooficial.imprensaoficial.com.br/doflash/prototipo/" + ano + "/" + MESES[mes-1] + "/"+str(dia).zfill(2)+"/legislativo/pdf/pg_" + str(page).zfill(4) + ".pdf"
      print(urldapagina)
      dlfile(urldapagina)
  except URLError, e:
    print "Feito."

###################################
# Cria um diretÃ³rio para o mÃªs.   #
# Junta as paginas em um arquivo. #
# Apaga os pdfs originais.        #
###################################
def juntaOsArquivos(ano, mes, dia):
  #Cria o diretÃ³rio para o mÃªs
  dirmes = os.getcwd() + os.sep + ano + "." + str(mes).zfill(2) + os.sep
  if not os.path.exists(dirmes):
    os.makedirs(dirmes)

  #lista os pdfs salvos
  files = sorted(glob.glob(os.getcwd() + os.sep + "*.pdf"))

  if files:
    merger = PdfFileMerger()

    #files = glob.glob("*.pdf")
    #files.sort
    for file in files:
      merger.append(file)

    finalpdfname = dirmes + "DOE " + ano + "." + str(mes).zfill(2) + "." + str(dia).zfill(2) + " - DAL.pdf"

    os.system("ln " + dirmes + "DOE\ " + ano + "." + str(mes).zfill(2) + "." + str(dia).zfill(2) + "\ -\ DAL.pdf" + " dal.pdf")

    merger.write(finalpdfname)

    for f in files:
      os.remove(f)

########################
# O programa principal #
########################
def main():
  ano = ANO
  mes = MES
  dia = DIA

  #Processa os argumentos
  parser = argparse.ArgumentParser(prog="Baixa DAL",usage='Informe o ano, mÃªs e dia desejado no formato "AAAA MM DD", ou deixe em branco para baixar o DOE de hoje.',description='Baixa o DiÃ¡rio da Assembleia Legislativa de SP.')
  parser.add_argument('ano', type=int, choices=range(int(ANO)-1, 2051), nargs='?', help='Informe o ano com 4 digitos. Este programa consegue recuperar ediÃ§Ãµes de um espaÃ§o da Imprensa Oficial onde ficam guardados as ediÃ§Ãµes dos Ãºltimos 5 ou 6 meses. Ã“bviamente este programa nÃ£o funciona para obter ediÃ§Ãµes de datas futuras :-p')
  parser.add_argument('mes', type=int, choices=range(1, 13), nargs='?', help='O mÃªs desejado com 1 ou 2 digitos.')
  parser.add_argument('dia', type=int, choices=range(1, 32), nargs='?', help='O dia do mÃªs, com 1 ou 2 digitos.')
  args = parser.parse_args()
  if args.ano:
    ano = str(args.ano)
  if args.mes:
    mes = args.mes
  if args.dia:
    dia = str(args.dia)

  #apaga pdfs antigos
  if os.path.isfile("dal.pdf"):
    os.remove("dal.pdf")
  files = glob.glob(os.getcwd() + os.sep + "*.pdf")
  for f in files:
    os.remove(f)

  print("Baixando o DiÃ¡rio do Legislativo do Estado de SP")
  print("Data da ediÃ§Ã£o: " + ano + str(mes).zfill(2) + str(dia).zfill(2) + " (AAAAMMDD)")

  baixaPaginas(ano, mes, dia)
  juntaOsArquivos(ano, mes, dia)

if __name__ == '__main__':
  main()

