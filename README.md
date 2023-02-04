# Renk-Tespiti-Ve-Kisi-Takip-Sistemi

Projemizin amacı kişilerin üstüne giydikleri kıyafetlerin renklerini tespit edip devamında bu kişilerin farklı mekanlarda veya aynı mekanlarda person1,2,3 ve kaç adet insan varsa üstündeki ve dış görünüş özelliklerine göre takip etmemizi sağlar

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Projemizin Genel Amaçları

-Kişilerin üstüne giydiği kıyafetlerin renk tespiti

-Kişilerin giydiği renge göre kişi takip sistemi

-Kişi tespitleri ve sırayla adlandırılması

-Aynı mekanlarda veya farklı mekanlarda kişi takip sistemi

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Kurulum

1)Contour Kavramı
-----

İlk olarak opencv kullanarak contour kavramından faydalanıyoruz. Contour kavramını kişinin üstüne giydiği kıyafetin rengini ele alarak areasını ortalama bize veriyor bu areayı kullanarak kişinin sadece üstündeki rengi tespit etmemizde sağlamaktadır. Contour.py dosyasında kodu bulunmaktadır
![image](https://user-images.githubusercontent.com/105969081/216791851-4c0e9a46-7a77-4cc9-9b7e-ac2b327237c9.png)

2)HSV Renk Kodu Öğrenme
-----

Sonraki adım olarak hangi renkleri tespit etmek istiyorsak özel olarak HSV renk değerlerini tespit etmemiz lazım. renkkoduöğrenme.py dosyasından elde edebiliriz.

![image](https://user-images.githubusercontent.com/105969081/216792178-68d77374-f765-4dc1-a11b-392cceb98007.png)

3)Renk Tespiti
-----

Sonrasında kişilerin giydiği kıyafetlerindeki rekleri tespit ediyoruz. Renktespiti.py dosyasısında mevcut burda istenilen videonun adresini giriyorsunuz.

![image](https://user-images.githubusercontent.com/105969081/216792546-95a71190-283b-4445-aa4c-02fc0d71504a.png) 


4)Labelİmg
-----

Labelİmg kullanarak videolardan elde edilen görüntüleri data set haline getiriyoruz Yolo formatında

5)YoloV5
-----

Renk tespiti yaptıkdan sonra elde edilen video çıktımızı Google Colab ortamında kullanıyoruz. Labelİmg kullanarak elde edilen data set YoloV5 formatında eğitilir eğitildikten sonra renk tespiti video çıktımızı işliyoruz.


6)Çıktı görüntüleri
-----

Çıktı videoları farklı renk ve aynı renk için yapılmıştır.
![image](https://user-images.githubusercontent.com/105969081/216792600-81f9fe6c-56ca-45e5-955b-2c12c24ee691.png) ![image](https://user-images.githubusercontent.com/105969081/216792619-630ab7cd-18e8-474b-8526-d18e21e38f3e.png)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Yazarlar
Hamza Harun Ercul 

Tufan Yiğit Çiftçioğlu

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Lisans
Bu sistem MIT lisansı altında mevcuttur. Daha fazla bilgi için LİSANS dosyasına bakın.



