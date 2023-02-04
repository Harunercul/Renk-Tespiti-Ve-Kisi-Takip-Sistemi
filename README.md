# Renk-Tespiti-Ve-Kisi-Takip-Sistemi
Projemizin amacı kişilerin üstüne giydikleri kıyafetlerin renklerini tespit edip devamında bu kişilerin farklı mekanlarda veya aynı mekanlarda person1,2,3 ve kaç adet insan varsa üstündeki ve dış görünüş özelliklerine göre takip etmemizi sağlar
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Projemizin Genel Amaçları

-Kişilerin üstüne giydiği kıyafetlerin renk tespiti

-Kişilerin giydiği renge göre kişi takip sistemi

-Kişi tespitleri ve sırayla adlandırılması

-Aynı mekanlarda veya farklı mekanlarda kişi takip sistemi

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Kurulum

İlk olarak opencv kullanarak contour kavramından faydalanıyoruz. Contour kavramını kişinin üstüne giydiği kıyafetin rengini ele alarak areasını ortalama bize veriyor bu areayı kullanarak kişinin sadece üstündeki rengi tespit etmemizde sağlamaktadır. Contour.py dosyasında kodu bulunmaktadır
![image](https://user-images.githubusercontent.com/105969081/216791851-4c0e9a46-7a77-4cc9-9b7e-ac2b327237c9.png)

Sonraki adım olarak hangi renkleri tespit etmek istiyorsak özel olarak HSV renk değerlerini tespit etmemiz lazım. 
