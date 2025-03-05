import copy #CREARE UNA COPIA DELL'OGGETTO
import random
from idlelib.iomenu import encoding # ENCODING NELLA LETTURA FILE
from operator import truediv, attrgetter # ORDINARE UNA LISTA
from random import randint #LIBRERIA RANDOM

class Giocatore:
    def __init__(self,nickname,punti): # I SELF
        self.nickname=nickname
        self.punti=int(punti)
    def __str__(self):
        return f"{self.nickname} {self.punti}" #I SELF I SELF RICORDATI STI CAZZO DI SELF COGLIONE

class Domanda:
    def __init__(self,testo,livello,corretta,sbagliate=[]):
        self.testo=testo
        self.livello=int(livello)
        self.corretta=corretta
        self.sbagliate=sbagliate
        self.numeroGiusto=0
    def __str__(self):
        d= f"Livello {self.livello}) {self.testo}\n"
        ordine=[]

        while len(ordine)!=4:
            numero=random.randint(0,3) #GENERA UN NUMERO
            if numero not in ordine:
                ordine.append(numero)

        count=1
        for i in ordine:
            if i==0:
                d+=f"{count}. {self.corretta}\n"
                self.numeroGiusto=count # RICORDATI I PORCODDIO DI SELF
                count+=1
            if i==1:
                d+=f"{count}. {self.sbagliate[0]}\n"
                count+=1
            if i==2:
                d+=f"{count}. {self.sbagliate[1]}\n"
                count+=1
            if i==3:
                d+=f"{count}. {self.sbagliate[2]}\n"
                count+=1
        return d.strip()

domande=[] # LISTA DI DOMANDE

try: #BLOCCO TRY-CATCH PER LA LETTURA FILE
    with open("domande.txt","r",encoding="utf-8") as file: # "r" MODALITA' READER E UTILIZZARE L'ENCODING
        righe=file.readlines()

        #PROCESSA IL FILE RIGA PER RIGA
        for i in range(0,len(righe),7): #OGNI DOMANDA E' FORMATA DA 7 RIGHE range(start,stop,step)
            testo=righe[i].strip() #TESTO DELLA DOMANDA
            livello=righe[i+1].strip() # .strip() RIMUOVE GLI SPAZI INIZIALI E FINALI DELLA RIGA
            corretta=righe[i+2].strip()
            sbagliate=[righe[i+3].strip(),righe[i+4].strip(),righe[i+5].strip()]

            domanda=Domanda(testo,livello,corretta,sbagliate) #CREO LA VARIABILE DOMANDA
            domande.append(copy.copy(domanda)) #LA AGGIUNGO ALLA LISTA DI DOMANDE

    file.close()
except FileNotFoundError:
    print("Nome file ERRATO")
except Exception as e:
    print("ERRORE durante la lettura del file")


def DomandaCasualeLivello(liv):
    domandeLivello=[]
    for i in domande:
        if i.livello==liv:
            domandeLivello.append(i)

    return domandeLivello[random.randint(0,len(domandeLivello)-1)]

livello=0
livelloMax=0
for d in domande:
    if d.livello>livelloMax:
        livelloMax=d.livello

punti=0

while livello!=livelloMax+1:
    d=DomandaCasualeLivello(livello)
    print(d)
    t1=int(input("Inserisci la risposta: "))
    if t1==d.numeroGiusto:
        punti+=1
        livello+=1
        print()
    else:
        print(f"Risposta sbagliata! La risposta corretta era: {d.numeroGiusto}")
        break

with open("punti.txt","r") as file:
    righe=file.readlines()
    giocatori=[]
    for riga in righe:
        g=Giocatore(riga.split(" ")[0],riga.split(" ")[1])
        giocatori.append(g)
    nuovo=Giocatore(nick,punti)
    giocatori.append(nuovo)
    gOrdinati=sorted(giocatori,key=attrgetter("punti"),reverse=True) #ORDINE DESCRESCENTE

print()
print(f"Hai totalizzato {punti} punti!")
nick=input("Inserisci il tuo nickname: ")

with open("punti.txt","w") as file:
    for g in gOrdinati:
        file.write(f"{g.__str__()}\n")

