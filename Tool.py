from tureng_api import Tureng


print("""
     ____  ___   __________  ____ 
   / __ \/   | / ____/ __ \( __ )
  / / / / /| |/ / __/ / / / __  |
 / /_/ / ___ / /_/ / /_/ / /_/ / 
/_____/_/  |_\____/\____/\____/  
                                 
""")

language = {"EN-TR":"turkce-ingilizce",
            "EN-DE":"almanca-ingilizce",
            "EN-ES":"ispanyolca-ingilizce",
            "EN-FR":"fransizca-ingilizce"}



cevirilecek_dil = input("Çevirme işlemini seçiniz: ('EN-TR','TR-EN' gibi girin.)")
cevirilecek_kelime = input("Çevirilececk kelimeyi giriniz:")


if cevirilecek_dil in language:

    sinif = Tureng(cevirilecek_kelime,cevirilecek_dil)
    sinif.translate_en_to_other()
    sinif.show_translate()

else:
    sinif = Tureng(cevirilecek_kelime,cevirilecek_dil)
    sinif.translate_other_to_en()
    sinif.show_translate()






