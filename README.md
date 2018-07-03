Bir giriş görüntüsü alır.Görüntü siyah beyaz tona çevrilir.
Payların tutulacagı iki tane görüntü nesnesi oluşturulur.
iki matris tanımlanır ve matrisin degerleri 0 yada 255 
şeklinde tanımlanır.Bir döngü içerisinde rastgele satir 
sayisi elde edilir ve sutun sayısı belirleyerek matristen 
değer seçilir.Pikselin siyah ve beyaz olma durumuna göre 
seçilen deger paylara yerleştirilir. 

Kullanımı:
   goruntu_sifrele.py dosyasına giriş görüntüsünün yolunu verin.
   Pay1 ve Pay2 görüntüleri üretilir.
   goruntu.py dosyasına Pay1 ve Pay2 görüntülerinin 
   yolunu verin.Orijinal görüntü tekrar elde edilir.
Gereksinimler:
   import random
   from PIL import Image
