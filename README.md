# Online-Program
Online toplantı veya dersler için otomatik link açan saatli bomba misali ders programı

Kurulum:


*openpyxl kütüphanesini indirmek için cmd ye "pip install openpyxl" yazın excel dosyalarını okumak için lazım bu.


*Zoom toplantı linklerinizi ve ders isimlerinizi ders_link.txt nin içindeki örnek düzende olduğu gibi Ders\nLink(Ders 'Enter' Link şeklinde) giriniz.
  UYARI: ders_link.txt ye ders isimlerini ve linkleri girdikten sonra en sonda boş satır kalmamasına dikkat edin, python oralarıda satırmış gibi okuyor ki buda tahmin        edersiniz ki bizim hiç istemiyeceğiz bir şey.


*Ders programınızı programa işlemek için program_ornek.xlsx e girmeniz gerekmekte, şayet bilgisiyarınızda excel yoksa internette online edit yapabileceğiniz siteler mevcut ordan gerekli düzenlemeleri yapabilirsiniz. eğer bunu başardıysanız ders programınızı excel in içinde örneklerden feyz alarak giriniz. Kabaca anlatıcak olursam ilk columnda günler var, her günün yanında 2 tane bölüm var üstteki bölüme ders saatini alt bölümede dersin ismini girmeniz gerekli.(excel dosyasına girdiğinizde dediklerim daha anlamlı olacaktır
YENİ ÖZELLİKLER:
* Artık ders_link.txt'deki dersler için link yerine "empty" yazarak o dersin pas geçilmesini sağlıyabilirsiniz.
* Programda derslerin arasına kafanıza göre boşluk bırakabilirsiniz.


*Bütün bu aşamalar tamamsa artık online_program.py yi çalıştırabilirsiniz çalıştırdığınızda size excel dosyasının ismini(uzantısıyla birlikte girin) ve sonrasında derse kasıtlı geç girme süresini yazmanızı istiyecektir(her hocanın dersi tam zamanında açmaması yüzünden eklediğim bir özellik, tavsiyem 120 saniye) sonrasında arkanıza yaslanıp programın tam saatinde online derslerinize otomatik girmesini izleyin, yada izlemeyin uyuyun banane fark etmez.


*Zoom ayarlarından mikrofonun otomatik kanala katılmasını falan ayarlayın kameranızı kapatın (işinizi size öğreticek değilim sadece hatırlatıyorum) ki taklaya gelmeyin.


ÖNEMLİ NOT:
ders_link.txt deki ders adları ile excel programındaki ders adları nın aynı olması gerektiğini umarım söylememe gerek yoktur(büyük harflere duyarlı). Burda sihir yapmıyoruz elinizdeki verileri kullanıyorum.


Bu Arada:
Programı direk githubtan klonladığınız gibi test etmek istiyorsanız yükledikten sonra py dosyasını cmd üzerinden çalıştırın size excel dosyasını soracak program_ornek.xlsx yazın sonra kasıtlı bekleme süresinede bir şeyler sallayın ve programın nasıl bir çıktı verdiğini görün sonra kafanıza göre takılın kendi programınızı ordaki excel programına benzicek şekilde uyarlayın.


Sağlıcakla kalın hepinize selam olsun, umarım işinize yarar...
