# Flower Clustering Challenge Guide

## Challenge Overview
Bu challenge, çiçek görüntülerini analiz edip benzer özelliklerine göre kümelere ayırarak makine öğrenimi becerilerinizi geliştirmenizi amaçlamaktadır. Hedefiniz, farklı çiçek türlerini ayırt edebilen bir model kurmak ve veriyi kümelere ayırarak orijinal sınıflara mümkün olduğunca yakın sonuçlar elde etmektir.

## Goal
Çiçek veri setindeki görüntüleri belirlediğiniz model ve algoritmalarla işleyerek kümelere ayırmak ve orijinal sınıflara yakın doğruluğa ulaşmak. Challenge, esnek bir çalışma sunarak model seçimi ve özellik çıkarma yöntemlerinde özgürlük tanır, böylece farklı yaklaşımlar ve çözümler keşfetmenizi sağlar.

## Success Criteria
Başarı ölçütü, ayırdığınız kümelerin orijinal veri kümesindeki çiçek türleriyle olan benzerliğine göre değerlendirilecektir. Orijinal etiketler ile oluşturduğunuz kümeler arasındaki örtüşme oranı dikkate alınacaktır.

### Puanlama Sistemi
- %50 - %60 arası benzerlik: 1 puan
- %60 - %70 arası benzerlik: 2 puan
- %70 - %80 arası benzerlik: 3 puan
- %80 - %90 arası benzerlik: 4 puan
- %90 - %100 arası benzerlik: 5 puan

Toplamda en fazla 25 puan toplanabilir.

### Önerilen Performans Metrikleri
- **Silhouette Score**: Kümelerin ayrım kalitesini ölçmek için kullanabilirsiniz. Yüksek silhouette skoru, kümelerin net bir şekilde ayrıldığını gösterir.
- **Accuracy**: Sonuçları orijinal veri kümesiyle kıyaslayarak doğru sınıflandırılan görüntülerin oranını hesaplayabilirsiniz.

## Instructions

Aşağıdaki adımlar, challenge boyunca izleyebileceğiniz genel bir süreci göstermektedir. Ancak, katılımcılar istedikleri model ve algoritmaları seçmekte özgürdür ve adımlar isteğe bağlı olarak değiştirilebilir.

### 1. Veriyi Yükleme
- `model/` klasöründe sağlanan `.npy` dosyalarını **numpy** ile yükleyin.
- Örnek kod veya detaylı açıklama için notebook dosyasına bakabilirsiniz.

### 2. Veri Ön İşleme
- Yüklenen özellikleri `StandardScaler` kullanarak ölçeklendirin. Bu, veri setini standardize ederek kümeleme algoritmalarının daha iyi performans göstermesine yardımcı olacaktır.

### 3. PCA ile Boyut İndirgeme (Opsiyonel)
- Veri setinin boyutunu azaltmak için **Principal Component Analysis (PCA)** uygulayabilirsiniz. Önerilen bileşen sayısı 9’dur.
- PCA ile veri boyutunu indirgedikten sonra, açıklanan varyans oranını kontrol ederek ne kadar bilgi kaybı yaşandığını değerlendirin.
  
### 4. Kümeleme Algoritması Seçimi ve Uygulaması
- **Gaussian Mixture Model (GMM)** ile kümeleme yapılması önerilmiştir, ancak farklı kümeleme algoritmalarını kullanmakta serbestsiniz.
- Küme sayısını veri setindeki çiçek türü sayısına göre 5 olarak belirleyebilirsiniz, ancak bu sayı katılımcıların inisiyatifine bırakılmıştır.
  
### 5. Model ve Özellik Çıkarma (Serbest)
- Veriyi kümelere ayırmak için kullanacağınız model ve algoritmalar tamamen sizin tercihinize bağlıdır.
- **Özellik çıkarma (feature extraction)** işlemi için dilediğiniz modeli kullanabilirsiniz. **PCA kullanmak zorunlu değildir**; farklı özellik çıkarma yöntemleri kullanarak da analiz yapabilirsiniz.

### Sonuçların Değerlendirilmesi
Orijinal veri kümesi ile ayırdığınız kümeler arasındaki benzerliği ölçerek, belirlenen kriterler doğrultusunda puanınızı hesaplayın. Orijinal veri setindeki çiçek türleri ile oluşturduğunuz kümeler arasındaki benzerlik oranı üzerinden puanlama yapılacaktır.

## Submission Requirements
- **Kümelenmiş Veri Klasörleri**: Her küme için bir klasör olacak şekilde çıktı klasörünüzü hazırlayın. Bu klasör yapısını orijinal veri setiyle kıyaslanabilir hale getirin.
- **Notebook veya Script Dosyası**: Tüm süreci anlatan bir Jupyter notebook (`.ipynb`) veya Python script (`.py`) dosyası sunun. Kodunuzun anlaşılır ve açıklayıcı olması önemlidir.
- **Sonuç Raporu (Optional)**: Sonuçlarınızı özetleyen kısa bir rapor sunabilirsiniz. Bu raporda, elde ettiğiniz benzerlik yüzdesi ve toplam puanınızı belirtin. Ayrıca, kümeleme süreci boyunca karşılaştığınız zorluklar ve geliştirme önerilerinizi de ekleyebilirsiniz.
