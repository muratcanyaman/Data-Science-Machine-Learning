# Veri Bilimi ve Makine Öğrenmesi Çalışmalarım

Bu depoyu, Veri bilimi ve Makine Öğrenmesi alanında öğrendiğim konuları düzenli ve kalıcı bir kaynakta toplamak amacıyla oluşturdum. Amacım; teorik bilgileri Python kodları, örnek veri setleri ve uygulamalarla pekiştirmek, gelişimimi takip etmek ve ihtiyaç duyduğumda yeniden başvurabileceğim kişisel bir çalışma arşivi oluşturmak.

Notlarımın büyük bölümü Türkçe anlatımlardan oluşuyor. Konuları mümkün olduğunca temel kavramlardan başlayarak teori, kodlama, model kurma, tahmin, değerlendirme ve model iyileştirme adımlarıyla ele alıyorum.

## İçerik

| Bölüm | Konular |
|---|---|
| [Python Temelleri](./Fundamentals%20of%20Python) | Veri tipleri, koleksiyonlar, fonksiyonlar, koşullar, döngüler, nesne yönelimli ve fonksiyonel programlama, modüller ve hata yönetimi |
| [NumPy](./Numpy) | Diziler, indeksleme, dilimleme, veri tipleri, şekillendirme, birleştirme, filtreleme, rastgele sayı üretimi ve olasılık dağılımları |
| [Pandas](./Pandas) | Series yapısı, eleman ve değişken seçimi, `loc`–`iloc`, birleştirme, gruplama, toplulaştırma, pivot tablolar ve veri okuma |
| [Veri Bilimi için İstatistik](./Statistics%20for%20Data%20Science) | Betimsel istatistikler, güven aralıkları, olasılık dağılımları, hipotez testleri, t-testleri, varyans ve korelasyon analizi ile iş uygulamaları |
| [Veri Ön İşleme](./Data%20Preprocessing) | Aykırı ve eksik değer analizi, silme ve değer atama yöntemleri, tahmine dayalı doldurma, standartlaştırma, dönüşüm ve one-hot encoding |
| [Keşifçi Veri Analizi ve Görselleştirme](./EDA%20and%20Data%20Visualization) | Veri setini tanıma, kategorik ve sürekli değişken analizi; bar, histogram, yoğunluk, box, violin, scatter, ısı haritası ve zaman serisi grafikleri |
| [Veritabanı Yönetimi](./Database%20Management) | SQLite, SQL sorguları, tablo işlemleri ve SQL–Pandas birlikte kullanımı |
| [Veri Bilimi Proje Yönetimi](./Data%20Science%20Project%20Management) | Veri bilimi proje yaşam döngüsü ve proje yönetimi yaklaşımı |
| [Makine Öğrenmesine Giriş](./Machine%20Learning%20I) | Temel kavramlar, öğrenme türleri, iş akışı, model doğrulama, performans ölçümü, bias–variance dengesi ve model performansını artırma |
| [Doğrusal Regresyon](./Machine%20Learning%20II%20-%20Linear%20Regression) | Basit ve çoklu doğrusal regresyon, PCR, PLS, Ridge, Lasso ve ElasticNet; teori ve model uygulamaları |
| [Doğrusal Olmayan Regresyon](./Machine%20Learning%20III%20-%20Nonlinear%20Regression) | KNN, SVR, yapay sinir ağları, CART, Bagged Trees, Random Forest, GBM, XGBoost, LightGBM ve CatBoost |
| [Sınıflandırma Modelleri](./Machine%20Learning%20IV%20-%20Classification%20Models) | Lojistik regresyon, Naive Bayes, KNN, SVC/RBF SVC, yapay sinir ağları, ağaç ve boosting tabanlı yöntemler |
| [Gözetimsiz Öğrenme](./Machine%20Learning%20V%20-%20Unsupervised%20Learning) | K-Means, hiyerarşik kümeleme ve temel bileşen analizi (PCA) |
| [NLP ve Metin Madenciliği](./NLP%20%26%20Text%20Mining) | Metin ön işleme, tokenization, stemming, lemmatization, duygu analizi, kelime frekansları ve kelime bulutu |
| [Büyük Veri Analitiği](./Big%20Data%20Analytics) | Büyük veri kavramları, Hadoop, Spark, PySpark DataFrame ve Spark SQL uygulamaları |

## Kullandığım Araçlar

Çalışmalarımda ağırlıklı olarak Python ve Jupyter Notebook kullanıyorum. NumPy, Pandas, SciPy, Statsmodels, Matplotlib, Seaborn ve Scikit-learn temel araç setini; XGBoost, LightGBM ve CatBoost ileri modelleme çalışmalarını; NLTK, TextBlob ve WordCloud metin analizini; SQLite, Hadoop, Spark ve PySpark ise veritabanı ve büyük veri çalışmalarını destekliyor.

## Noteook'ları Çalıştırma

Depoyu bilgisayarınıza klonlayıp Jupyter Notebook veya JupyterLab ile ilgili dosyayı açabilirsiniz:

```bash
git clone https://github.com/muratcanyaman/Data-Science-Machine-Learning.git
cd Data-Science-Machine-Learning
jupyter lab
```

Notebook'ların ihtiyaç duyduğu kütüphaneler konuya göre değişebilir. İlgili notebook'taki import satırlarını kontrol ederek eksik paketleri kurabilirsiniz.

## Not

Bu depo, tamamlanmış tek bir projeden ziyade öğrenme sürecimle birlikte büyüyen kişisel bir bilgi ve uygulama arşividir. Yeni konular öğrendikçe mevcut notları geliştirmeye ve yeni çalışmalar eklemeye devam ediyorum.
