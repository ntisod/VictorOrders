import io

fn = input("skriv fnamn")
en = input("skirv enamn")

#öppna fil
f=io.open("minfil.txt", "a", encoding="utf-8")

#spra str för att skrva tll fil
text = fn + ";" + en + "\n"

#skrv tll fil
f.write(text)

#stng fil
f.close()