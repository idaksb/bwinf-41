
# Definition eine Klasse "Book"
class Book(object):
    content = None
    start = None
    end = None
    prospects = None 

    # Konstruktor der Klasse "Book"
    def __init__(self,book_input):
        self.content = book_input
        self.start = []
        self.end = []
        self.prospects= []

    # Suche aller Möglichkeiten, wo das Startwort vorkommt
    def get_start(self,word):
        count = 0
        while count < len(self.content):
            case = str.find(self.content, word, count)
            if count == 0:
                count = 1
            if case == -1:
                break
            else:
                count = case+1
            self.start = self.start + [case]

    # gibt mir das Ende des letzen Worts für jedes Startwort auf Basis der Länge des zu suchenden Texts
    def get_end(self,ways,length):
        for i in ways:
            count = 0
            length_word = 0
            for char in self.content[i:]:
                if count < length+1:
                    length_word = length_word+1
                    if char == ' ':
                        count = count + 1
                else :
                    break
            self.end = self.end +[(i+length_word)]

    # bestimmt die Länge der Wörter
    def words(self,text):
        words_end = []
        count = 0
        for char in text:
            if  char == " ":
                words_end = words_end + [count]
            count = count + 1
        words_end = words_end + [count]
        return words_end
    
    # gibt für alle möglichen Startpositionen die Phrase und wo die Wörter enden aus
    def found(self,word,length):
        self.get_start(word)
        self.get_end(self.start,length)
        for i in range (0,len(self.start)):
            if self.content[self.end[i]-1] == " ":
                prospect = self.content[self.start[i]:self.end[i]-1]
            else:
                prospect= self.content[self.start[i]:self.end[i]]
            words_length = self.words(prospect)
            self.prospects = self.prospects + [(prospect, words_length)]
        return self.prospects


# Definition der Klasse "Cloze" (Lückentext)
class Cloze(object):
    text = None 
    book = None

    # Konstruktor der Klasse "Cloze"
    def __init__(self,cloze_input,book_input):
        self.text = cloze_input
        self.book = Book(book_input)
    
    # bestimmt, wie viele Wörter in dem Lückentext sind
    def get_length (self):
        count = 0
        for char in self.text:
            if char == " ":
                count = count + 1
        return count

    # setzt das erste Wort des Lückentexts als Startwort
    def start_word (self):
        length = str.find(self.text," ")
        start_word = self.text[:length]
        return start_word
    
    # vergleicht für jede Möglichkeit, ob alle gegebenen Wörter übereinstimmen - das ist die eigentliche Lösung der Aufgabe
    def final (self):
        cloze_words = self.book.words(self.text)
        ways_text_words = self.book.found(self.start_word(),self.get_length())
        ways_text = []
        ways_words = []

        for i in ways_text_words:
            ways_text = ways_text + [i[0]]
            ways_words = ways_words + [i[1]]
        for j in range (0,len(ways_text)):

            way_text = ways_text[j]
            way_words = ways_words[j]
            if len(cloze_words) != len(way_words):
                ways_text[j]= 0
            else:
                for i in range (0,len(cloze_words)-1):
                    if self.text[cloze_words[i]+1:cloze_words[i+1]] != "_" and self.text[cloze_words[i]:cloze_words[i+1]] != way_text[way_words[i]:way_words[i+1]]:
                        ways_text[j]= 0
                        break

        for i in ways_text:
            if i != 0:
                print(i)

# Öffnen der Buchdatei mit dem Text
book = open("Alice_im_Wunderland.txt")
book_str = ""

# umwandeln der geöffneten Datei in einen String
for line in book :
    if line != "\n":
        book_str = book_str + line
        book_str = book_str.strip("\n")
        if book_str[len(book_str)-1:len(book_str)] != " ":
            book_str = book_str + " "

# Entfernen der Sonderzeichen und überschüssige Leerzeichen und alles in Kleinschreibung umwandeln
for i in ["(",")","-","[","]","»","«",",",".","!","?"]:
    book_str = book_str.replace(i,"")
book_str= ' '.join(book_str.split())
book_str = book_str.lower()

# Öffnen der Lückentextdatei und Umwandlung in einen String
cloze = open("stoerung5.txt")
cloze_str = ""
for line in cloze :
    cloze_str = cloze_str + line

# Durchführen des Programms
test = Cloze(cloze_str,book_str)
test.final()