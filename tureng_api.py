from bs4 import BeautifulSoup
from requests import get

language = {"EN-TR":"turkce-ingilizce",
            "EN-DE":"almanca-ingilizce",
            "EN-ES":"ispanyolca-ingilizce",
            "EN-FR":"fransizca-ingilizce"}

language_1 = {"TR-EN" : "turkce-ingilizce",
             "DE-EN" : "almanca-ingilizce",
             "ES-EN":  "ispanyolca-ingilizce",  
             "FR-EN":  "fransizca-ingilizce"}

#Class'i tanımlarken language_ kısmına çevirmek istediğiniz değerleri vermelisiniz.
class Tureng(object):
    def __init__(self,word,language_):
        self.word = word
        self.anlam = ""
        self.kategori = ""

        if language_ in language:
            self.tureng_url = "https://tureng.com/tr/{}".format(language[language_]) + "/" + self.word
        
        elif language_ in language_1:
            self.tureng_url = "https://tureng.com/tr/{}".format(language_1[language_]) + "/" + self.word

        else:
            raise TypeError("Geçerli dil giriniz.")  

    #Url'e http isteği atabilmek için oluşturuldu.
    def request_html(self):
        return(get(self.tureng_url).content)


    #Tabloların içerisinde hidden_xs ile ilgili birçok bilgi var istediğimizi çekebilmek için oluşturuldu.
    def show_translate(self,counter = 0):
        for m in range(1,len(self.kategori),3):
            print("""
                Kategori / Anlam
                {0} :  {1}""".format(self.kategori[m].get_text(),self.anlam[counter].get_text()))
            counter += 1

    #İngilizceden başka dile çevirmek için.
    def translate_en_to_other(self):
        try:
            kelime_url = BeautifulSoup(self.request_html(),'html.parser')
            table_kelime = kelime_url.find_all('table',id = "englishResultsTable")
            self.anlam = table_kelime[0].find_all('td',class_ = 'tr ts')
            self.kategori = table_kelime[0].find_all('td',class_ = 'hidden-xs')

        #Kelime bulunmadığı zaman verilecek hata.
        except IndexError:
            print("Kelime bulunamadı.")


    #Başka dilden ingilizceye çevirmek için gerekli fonksiyon
    def translate_other_to_en(self):
      try:
          kelime_url_r = BeautifulSoup(self.request_html(),'html.parser')
          table_kelime_r = kelime_url_r.find_all('table',id = 'englishResultsTable')
          self.anlam = table_kelime_r[0].find_all('td',class_ = 'en tm')
          self.kategori = table_kelime_r[0].find_all('td',class_ = 'hidden-xs')
     
      except IndexError:
          print("Kelime bulunamadı.")

           




