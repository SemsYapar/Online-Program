# Online-Program
Online toplantı veya dersler için otomatik link açan saatli bomba misali ders programı

Kurulum:

*Zoom toplantı linklerinizi ve ders isimlerinizi ders_link.txt nin içindeki örnek düzende olduğu gibi Ders\nLink(Ders 'Enter' Link) giriniz.

*Program_taslak.xlsx e girmeniz gerekmekte, şayet bilgisiyarınızda excel yoksa internette online edit yapabileceğiniz siteler mevcut ordan gerekli düzenlemeleri yapabilirsiniz. eğer bunu başardıysanız ders programınızı excel in içinde örneklerden feyz alarak giriniz. Kabaca anlatıcak olursam ilk columnda günler var, her günün yanında 2 tane bölüm var üstteki bölüme ders saatini alt bölümede dersin ismini girmeniz gerekli.(excel dosyasına girdiğinizde dediklerim daha anlamlı olacaktır)

*Bütün bu aşamalar tamamsa artık online_program.py yi çalıştırabilirsiniz çalıştırdığınızda size excel dosyasının ismini(uzantısıyla birlikte girin) ve sonrasında derse kasıtlı geç girme süresini yazmanızı istiyektir(her hocanın dersi tam zamanında açmaması yüzünden eklediğim bir özellik, tavsiyem 120 saniye) sonrasında arkanıza yaslanıp programın tam saatinde online derslerinize otomatik girmesini izleyin, yada izlemeyin uyuyun banane fark etmez.

*Zoom ayarlarından mikrofonun otomatik kanala katılmasını falan ayarlayın kameranızı kapatın (işinizi size öğreticek değilim sadece hatırlatıyorum) ki taklaya gelmeyin.

ÖNEMLİ NOT:

zoom_link.txt deki ders adları ile excel programındaki ders adları aynı olması gerektiğini umarım söylemem gerekmez(büyük harflere duyarlı). Burda sihir yapmıyoruz elinizdeki verileri kullanıyorum saçmalamayınız nütfen.

UYARI:

*Excel dosyası çok hassas, eğer dosyayla fazla oynaşırsanız (mesela derslerinizi ve saatlerinizi güzel güzel girerken yanlışlıkla hiç doldurmıyacağınız bir column a yazı yazdınız tıkladınız ve bunun sonucundada programın hata verdiğini gözlemlediniz. Çözüm önerim her ne kadar yanlışlıkla yazı yazdığınız yeri silmeye çalışmış olsanızda bunun program tarafından algılanması için column a sağ tık-> sil yapmanız gerekmekte ancak böyle excele orda bir veri olmadığını ifade edebilirsiniz bu dediğimi unutmayın) column sayısı programım tarafından yanlış hesaplanıcak ve büyük ihtimal program hata vericektir. O yüzden excel dosyasına yumuşak davranmanızı tavsiye ederim.(benim bu mesela yüzünden burnum biraz sürttü programı kodlama aşamasında)

*ders_link.txt ye ders isimlerini ve linkleri girdikten sonra en sonda boş satır kalmamasına dikkat edin, python oralarıda satırmış gibi okuyor ki buda tahmin edersiniz ki bizim hiç istemiyeceğiz bir şey.

EK NOT:
Programı direk gitten klonladığınız gibi test etmek için yükledikten sonra py dosyasını cmd üzerinden çalıştırın size excel dosyasını soracak program_ornek.xlsx yazın sonra kasıtlı bekleme süresinede bir şeyler sallayın ve programın nasıl bir çıktı verdiğini falan görün sonra kafanıza göre tkaılın kendi progrmaınızı ordaki exce progrmına benzicek şekilde uyarlayın falan

KAPANIŞ:
Sağlıcakla kalın hepinize selam olsun, umarım işinize yarar...
