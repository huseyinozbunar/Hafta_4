paragraf="""Son dakika haberi: Milyonlarca emeklinin merakla beklediği emekli bayram 
ikramiyesi zammı belli oldu. AK Parti Grup Başkanvekili Abdullah Güler yeni bayram 
ikramiyesi rakamını açıkladı. Emekli ikramiyesi 3 bin TL\'den 4 bin TL\'ye yükseltildi.
İkramiyenin 4 bin TL\'ye çıkarılmasıyla birlikte her iki bayram için emeklilere 8 bin TL,
 toplamda ise 134.5 milyar TL ödenecek. Ekonomi kurmayları ile bürokratlarının geçen haftaki 
 yaptığı toplantıda ikramiyede gerçekleştirilecek artışın bütçeye getireceği ek maliyete ilişkin 
 etki analizi ortaya koydu. Emekli ikramiyesine hiç zam yapılmaması halinde oluşacak maliyetin 99 
 milyar TL olduğu bilgisi paylaşıldı."""
kelimeler=paragraf.split(' ')

def donustur(a):
    sayac = []
    for kelime in a:
       print(kelime)
       sayici = 0
       for harf in range(len(kelime)):
        sayici+=1
       print(sayici)
       sayac.append(sayici)
    return sayac
b = donustur(kelimeler)
print(b)