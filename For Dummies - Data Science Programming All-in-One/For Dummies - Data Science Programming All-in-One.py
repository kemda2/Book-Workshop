####################################################################################################
# About This Book
####################################################################################################

# Jupyter Notebook also relies on the literate programming strategy first proposed by
# Donald Knuth (see http://www.literateprogramming.com/) to make your coding efforts 
# significantly easier and more focused on the data.

####################################################################################################

# You must know how to work with Python or R. You can find a wealth of Python tutorials online (see
# https://www.w3schools.com/python/ and
# https://www.tutorialspoint.com/python/ as examples). 

# R, likewise, provides a wealth of online tutorials (see
# https://www.tutorialspoint.com/r/index.htm,
# https://docs.anaconda.com/anaconda/navigator/tutorials/rlang/, 
# and https://www.statmethods.net/r-tutorial/index.html as examples).

####################################################################################################
# Chapter 1 Considering the History and Uses of Data Science
####################################################################################################

# Veri yönetimi (bkz. Kitap 2), 
# istatistiksel analiz (bkz. Kitap 3), 
# yapay zeka, makine öğrenimi, derin öğrenme (bkz. Kitap 4), 
# pratik veri bilimi uygulaması (bkz. Kitap 5) 
# hem veri hem de kod sorunlarını giderme (bkz. Kitap 6).

####################################################################################################

# Demografi toplarken AI'lar için sıklıkla atıfta bulunulduğunu gördüğünüz yöntemler şunlardır:

# » Geçmiş: Bir yapay zeka, önceki eylemlere dayanarak gelecekte gerçekleştirebileceğiniz eylemleri 
# genelleştirir.

# » Geçerli etkinlik: Şu anda gerçekleştirdiğiniz eyleme ve belki de cinsiyet gibi diğer 
# özelliklere bağlı olarak, bir bilgisayar bir sonraki işleminizi tahmin eder.

# » Özellikler: Cinsiyet, yaş ve yaşadığınız bölge gibi sizi tanımlayan özelliklere dayanarak, 
# bir bilgisayar yapma olasılığınız olan seçimleri tahmin eder.

####################################################################################################

# Demografik tahminle deneme yapmak istiyorsanız, çevrimiçi olarak bir dizi API bulabilirsiniz. 
# Örneğin, https://deepai.org/machine-learning-model/demographic- adresindeki DeepAI API'si Tanıma, 
# bir kişinin videodaki görünümüne göre yaş, cinsiyet ve kültürel arka planı tahmin etmenize 
# yardımcı olmayı vaat eder. Çevrimiçi API'lerin her biri uzmanlaşmıştır, bu nedenle API'yi 
# sağlayabileceğiniz giriş verilerinin türüne dikkat ederek seçmeniz gerekir.

####################################################################################################

# Derin öğrenme tarafından yönetilen veriler, insanların zihinlerini karıştıran son derece ince 
# kalıpları aramak için araçlar sağlar. Bu kalıplar, Google'ın 
# http://www.digitaljournal.com/tech-and-science/technology/google-to-use-ai-to-predict-natural-disasters/article/533026
# adresindeki çözümüyle ilgili makaleye göre, doğal bir felaketi tahmin etmeye yardımcı olabilir. 
# Yazılımın herhangi bir felaketi tahmin edebilmesi gerçeği tek kelimeyle şaşırtıcı. 
# Bununla birlikte, http://theconversation.com/ai-could-help-us-manage-natural-disasters-but-only-to-an-extent-90777 
# adresindeki makale, yalnızca bu tür yazılımlara güvenmenin bir hata olacağı konusunda uyarmaktadır.

####################################################################################################

# Renk üç öğeden oluşur: ton (gerçek renk (hue) ); değer (rengin koyuluğu veya açıklığı(value)); ve doygunluk 
# (rengin yoğunluğu(saturation)). Bu öğeler hakkında daha fazla bilgiyi 
# http://learn.leighcotnoir.com/artspeak/elements-color/hue-value-saturation/ adresinde bulabilirsiniz. 
# Bununla birlikte, AI bu süreci https://emerj.com/ai-future-outlook/ai-is-colorizing-and-beautifying-the-world/ 
# bölümünde açıklandığı gibi Evrişimli Sinir Ağları (CNN'ler) kullanarak otomatikleştirdi.

# CNN'i renklendirme için kullanmanın en kolay yolu, size yardımcı olacak bir kütüphane bulmaktır. 
# https://demos.algorithmia.com/colorize-photos/'daki Algorithmia sitesi böyle bir kütüphane sunuyor 
# ve bazı örnek kodlar gösteriyor. Sağlanan alana bir URL yapıştırarak da uygulamayı deneyebilirsiniz. 
# https://petapixel.com/2016/07/14/app-magically-turns-bw-photos-color-ones/  adresindeki makale, 
# bu uygulamanın ne kadar iyi çalıştığını açıklamaktadır. Kesinlikle şaşırtıcı!

####################################################################################################

# Neyse ki, en azından bugün https://github.com/tensorflow/tfjs-models/tree/master/posenet adresindeki 
# tfjs-models (PoseNet) kütüphanesini kullanarak kişi pozlarıyla çalışmaya başlayabilirsiniz. 
# Bunu, kaynak koduyla tamamlanmış bir web kamerasıyla çalışırken https://ml5js.org/docs/posenet-webcam 
# görebilirsiniz. Örneğin yüklenmesi biraz zaman alır, bu nedenle sabırlı olmanız gerekir.

####################################################################################################

# Sanat ve eğlence sağlamak
# Kitap 5, Bölüm 4, derin öğrenmenin gerçek dünyadaki bir resmin içeriğini ve mevcut bir usta ressamın 
# (canlı veya ölü) içeriğini ikisinin bir kombinasyonunu oluşturmak için stil için nasıl kullanabileceği 
# konusunda bazı iyi fikirler sunar. Aslında, bu yaklaşım kullanılarak üretilen bazı sanat eserleri, 
# açık artırma bloğunda yüksek fiyatlara hükmediyor. Bu özel sanat kuşağı hakkında her türlü makaleyi 
# bulabilirsiniz, örneğin https://www.wired.com/story/we-made-artificial-intelligence-art-so-can-you/ 
# adresindeki Wired makalesi gibi.
# Bununla birlikte, resimler duvara asmak için güzel olsa da, başka sanat türleri üretmek isteyebilirsiniz. 
# Örneğin, Smoothie 3-D gibi ürünleri kullanarak resminizin 3B sürümünü oluşturabilirsiniz. 
# https://styly.cc/tips/smoothie-3d/ ve https://3dprint.com/38467/smoothie-3d-software/'daki makaleler 
# bu yazılımın nasıl çalıştığını açıklamaktadır. Bir heykel yaratmakla aynı şey değildir; bunun yerine, 
# resminizin 3B sürümünü oluşturmak için bir 3B yazıcı kullanırsınız. 
# https://thenextweb.com/artificial-intelligence/2018/03/08/try-this-ai-experiment-that-converts-2d-images-to-3d/
# sürecin nasıl çalıştığını görmek için gerçekleştirebileceğiniz bir deney sunar.

####################################################################################################

# Dünyadaki mevcut programlama dillerinin hiçbiri her şeyi yapamaz. Böyle bir dil çabası olan Ada, 
# sınırlı bir başarı elde etmiştir, çünkü dilin öğrenilmesi inanılmaz derecede zordur 
# (ayrıntılar için https://www.nap.edU/read/5463/chapter/3 ve 
#  https://news.ycombinator.com/item?id=7824570 bakınız). Sorun şu ki, bir dili her şeyi yapacak 
# kadar sağlam hale getirirseniz, herhangi bir şey yapmak için çok karmaşıktır. Sonuç olarak, bir veri 
# bilimcisi olarak, her biri veri bilimi gelişiminin belirli bir yönüyle ilgili bir güce sahip olan 
# bir dizi dile maruz kalmanız gerekebilir. Aşağıdaki bölümler, bu kitap tarafından desteklenen 
# diller olan Python ve R'ye özel bir vurgu yaparak, veri bilimi için kullanılan dilleri daha iyi
# anlamanıza yardımcı olur.

####################################################################################################

# Veri bilimi dillerine genel bir bakış elde etme
# Birçok farklı programlama dili vardır ve çoğu, görevleri belirli bir şekilde yerine getirmek veya 
# hatta belirli bir mesleğin işini yapmayı kolaylaştırmak için tasarlanmıştır. Doğru aracı seçmek 
# hayatınızı kolaylaştırır. Bir vidayı sürmek için tornavida yerine çekiç kullanmaya benzer. Evet, 
# çekiç çalışıyor, ancak tornavidanın kullanımı çok daha kolay ve kesinlikle daha iyi bir iş çıkarıyor. 
# Veri bilimcileri, verilerle çalışmayı kolaylaştırdıkları için genellikle yalnızca birkaç dil 
# kullanırlar. Bu fikri göz önünde bulundurarak, tercih sırasına göre veri bilimi çalışmaları için 
# en iyi diller şunlardır:

# » Python (genel amaçlı): Birçok veri bilimcisi, veri bilimi görevlerini önemli ölçüde kolaylaştırmak 
# için NumPy, SciPy, MatPlotLib, pandas ve Scikit-learn gibi zengin kütüphaneler sağladığı için Python 
# kullanmayı tercih eder. Python ayrıca büyük veri kümelerinde çoklu işlem kullanımını kolaylaştıran 
# ve böylece bunları analiz etmek için gereken süreyi azaltan hassas bir dildir. Veri bilimi topluluğu, 
# veri bilimi hesaplamalarıyla çalışmayı önemli ölçüde kolaylaştıran Jupyter Notebook kavramını 
# uygulayan Anaconda gibi özel IDE'lerle de hızlandı. (Bu mini kitabın 3. Bölümü, Jupyter Not Defteri'nin 
# nasıl kullanılacağını göstermektedir, bu nedenle bu bölümde endişelenmeyin.) Python'un lehine olan tüm 
# bu yönlere ek olarak, C / C ++ ve Fortran gibi dillerle tutkal kodu (mevcut çeşitli kod öğelerini uyumlu 
# bir bütüne bağlamak için kullanılan kod) oluşturmak için mükemmel bir dildir. Python belgeleri aslında 
# gerekli uzantıların nasıl oluşturulacağını gösterir. Çoğu Python kullanıcısı, bir robotun bir piksel 
# grubunu nesne olarak görmesine izin vermek gibi kalıpları görmek için dile güvenir. Ayrıca her türlü 
# bilimsel görev için kullanım görür.

# » R (özel amaçlı istatistik): Birçok açıdan, Python ve R aynı tür işlevleri paylaşır, ancak farklı 
# şekillerde uygularlar. Hangi kaynağı görüntülediğinize bağlı olarak, Python ve R yaklaşık olarak 
# aynı sayıda savunucuya sahiptir ve bazı insanlar Python ve R'yi birbirinin yerine (veya bazen birlikte) 
# kullanır. Python'un aksine, R kendi ortamını sağlar, bu nedenle Anaconda gibi üçüncü taraf bir ürüne 
# ihtiyacınız yoktur. Ancak, bu mini kitabın 3. Bölümü, tüm ihtiyaçlarınız için tek bir IDE kullanabilmeniz 
# için Jupyter Not Defteri'nde R'yi nasıl kullanabileceğinizi gösterir. Ne yazık ki, R, Python'un sağladığı 
# kolaylık ile diğer dillerle karışmıyor gibi görünüyor.

# » SQL (veritabanı yönetimi): Yapılandırılmış Sorgu Dili (SQL) hakkında hatırlanması gereken en önemli şey, 
# görevlerden ziyade verilere odaklanmasıdır. (Bu ayrım, onu bir veri bilimcisi için tam teşekküllü bir dil 
#                                              haline getirir, ancak bir bilgisayar bilimcisi için çözümün 
#                                              yalnızca bir parçasıdır.) İşletmeler iyi veri yönetimi olmadan 
# çalışamazlar - veriler iştir. Büyük kuruluşlar, verilerini depolamak için normalde SQL ile erişilebilen bir 
# tür ilişkisel veritabanı kullanır. Çoğu Veritabanı Yönetim Sistemi (DBMS) ürünü ana dili olarak SQL'e dayanır 
# ve DBMS genellikle çok sayıda veri analizine ve yerleşik diğer veri bilimi özelliklerine sahiptir. Verilere 
# yerel olarak eriştiğiniz için, veri bilimi görevlerini bu şekilde gerçekleştirirken genellikle önemli bir 
# hız artışı yaşarsınız. Veritabanı Yöneticileri (DBA'lar) genellikle ayrıntılı bir analiz yapmak yerine verileri 
# yönetmek veya işlemek için SQL kullanır. Bununla birlikte, veri bilimcisi SQL'i çeşitli veri bilimi görevleri 
# için de kullanabilir ve elde edilen komut dosyalarını DBA'ların ihtiyaçları için kullanılabilir hale getirebilir.

# » Java (genel amaçlı): Bazı veri bilimcileri, genel amaçlı, yaygın olarak uyarlanmış ve popüler bir dil 
# gerektiren başka programlama türleri gerçekleştirir. Java, çok sayıda kütüphaneye erişim sağlamanın yanı sıra 
# (çoğu aslında veri bilimi için o kadar da yararlı değildir, ancak diğer ihtiyaçlar için çalışır), nesne 
# yönlendirmeyi bu listedeki diğer dillerden daha iyi destekler. Ek olarak, güçlü bir şekilde yazılmıştır 
# ve oldukça hızlı çalışma eğilimindedir. Sonuç olarak, bazı insanlar nihai kod için tercih eder. Java, 
# deneme veya geçici sorgular için iyi bir seçim değildir. İşin garibi, Jupyter Notebook için bir Java 
# uygulaması var, ancak rafine edilmemiş ve şu anda veri bilimi çalışmaları için kullanılamıyor. 
# (https://blog.frankel.ch/teaching-java-jupyter-notebooks/, https://github.com/scijava/scijava-jupyter-kernel, 
# and https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)

# » Scala (genel amaçlı): Scala, Java Sanal Makinesi'ni (JVM) kullandığından, Java'nın bazı avantaj ve 
# dezavantajlarına sahiptir. Bununla birlikte, Python gibi, Scala da lambda hesabını temel olarak kullanan 
# fonksiyonel programlama paradigması için güçlü bir destek sağlar (ayrıntılar için John Paul Mueller [Wiley] 
# tarafından yazılan Functional Programmming For Dummies'e bakınız). Ayrıca, Apache Spark Scala'da yazılmıştır, 
# yani bu dili kullanırken küme bilgi işlem için iyi bir desteğe sahip olursunuz. Büyük veri kümesi desteğini 
# düşünün. Scala'yı kullanmanın tuzaklarından bazıları, doğru şekilde kurulmasının zor olması, dik bir öğrenme 
# eğrisine sahip olması ve kapsamlı bir veri bilimine özgü kütüphane kümesinden yoksun olmasıdır.

####################################################################################################

# Python'un kütüphaneleri ana satış noktasıdır; ancak, Python yeniden kullanılabilir koddan daha fazlasını sunar. 
# Python ile göz önünde bulundurulması gereken en önemli şey, dört farklı kodlama stilini desteklemesidir:

# » İşlevsel: Her ifadeyi matematiksel bir denklem olarak ele alır ve herhangi bir durum veya değiştirilebilir 
# veri biçiminden kaçınır. Bu yaklaşımın temel avantajı, dikkate alınması gereken hiçbir yan etkiye sahip 
# olmamasıdır. Ek olarak, bu kodlama stili kendisini paralel işlemeye diğerlerinden daha iyi ödünç verir, 
# çünkü dikkate almanız gereken bir durumunuz yoktur. Birçok geliştirici özyineleme ve lambda hesabı için 
# bu kodlama stilini tercih eder.

# » Zorunluluk: Hesaplamaları program durumuna doğrudan bir değişiklik olarak gerçekleştirir. Bu stil özellikle 
# veri yapılarını işlerken ve zarif ama basit kod üretirken kullanışlıdır.

# » Nesne yönelimli: Nesne olarak kabul edilen ve yalnızca öngörülen yöntemlerle işlenen veri alanlarına dayanır. 
# Python bu kodlama formunu tam olarak desteklemez çünkü veri gizleme gibi özellikleri uygulayamaz. Ancak bu, 
# kapsülleme ve polimorfizmi desteklediği için karmaşık uygulamalar için kullanışlı bir kodlama stilidir. Bu 
# kodlama stili aynı zamanda kodun yeniden kullanılmasını da destekler.

# » Yordamsal: Görevleri, ortak görevlerin gerektiğinde çağrılan işlevlere yerleştirildiği adım adım yinelemeler 
# olarak ele alır. Bu kodlama stili yinelemeyi, sıralamayı, seçimi ve modülerleştirmeyi destekler.

####################################################################################################

# RStudio Masaüstü sürümü (https://www.rstudio.eom/products/rstudio/#Desktop), R ile çalışma görevini 
# daha da kolaylaştırabilir. Bu ürün ücretsiz olarak indirilebilir ve Linux (Debian / Ubuntu, RedHat / 
# CentOS ve SUSE Linux), Mac ve Windows sürümlerinde edinebilirsiniz. Kitap, ürünün ücretli sürümünde 
# bulunan gelişmiş özellikleri kullanmaz ve örnekler için RStudio Server özelliklerine ihtiyacınız olmaz.
# Jupyter Notebook veya RStudio'yu sevmediğinizi fark ederseniz diğer R dağıtımlarını deneyebilirsiniz. 
# En yaygın alternatif dağılımlar 
# StatET (http://www.walware.de/goto/statet), 
# Red-R (https://decisionstats.com/2010/09/28/red-r-1-8-groovy-gui/ veya http://www.red-r.org/) 
# ve Rattle'dır (http://rattle.togaware.com/). 

# Hepsi iyi ürünlerdir, ancak RStudio en güçlü takibe sahip gibi görünmektedir ve Jupyter Notebook 
# dışında kullanılacak en basit üründür. Çeşitli seçimlerle ilgili tartışmaları çevrimiçi olarak 
# aşağıdaki gibi yerlerde okuyabilirsiniz:
# https://www.quora.com/What-are-the-best-choices-for-an-R-IDE.

####################################################################################################

# For example, you might be involved in a type of data mining that doesn’t rely on AI but rather on 
# specific sorts of filtering, sorting, and the use of statistical analysis. The articles at 
# https://www.innoarchitech.com/blog/data-science-big-dataexplained-non-data-scientist and 
# https://www.northeastern.edu/graduate/blog/what-does-adata-scientist-do/ give you some other ideas 
# about how data scientists create and use data pipelines.

####################################################################################################

# Whatever the reason for the analysis, the results you achieve depend on these issues:
# * The reliability of the data
# * The quality of the data
# * The quantity of the data
# * Selection of the right algorithm
# * Presentation of the result in the correct manner
# * Interpretation of the result
# * Tuning of the result

####################################################################################################

# İnsanlar zekayı birçok farklı şekilde tanımlar. Ancak zekanın aşağıdaki eylemlerden oluşan belirli zihinsel faaliyetleri içerdiğini söyleyebilirsiniz: 

# * Öğrenme: Yeni bilgileri elde etme ve işleme yeteneğine sahip olma 
# * Akıl Yürütme: Bilgileri çeşitli şekillerde manipüle edebilme 
# * Anlama: Bilgi manipülasyonunun sonucunu dikkate alma 
# * Doğruları kavrama: Belirleme manipüle edilmiş bilginin geçerliliği 
# * İlişkileri görme: Doğrulanmış verilerin diğer verilerle nasıl etkileşime girdiğini tahmin etme 
# * Anlamları dikkate alma: Gerçekleri ilişkileriyle tutarlı bir şekilde belirli durumlara uygulama 
# * Gerçeği inançtan ayırma: Verinin kanıtlanabilir kaynaklar tarafından yeterince desteklenip desteklenmediğini belirleme tutarlı bir şekilde geçerli olduğu kanıtlanmıştır

####################################################################################################

# Zeka genellikle bir bilgisayar sisteminin bir simülasyonun parçası olarak taklit edebileceği bir süreci takip eder: 

# 1. İhtiyaçlara veya isteklere dayalı bir hedef belirleyin. 
# 2. Hedefi desteklemek için halihazırda bilinen herhangi bir bilginin değerini değerlendirin. 
# 3. Hedefi destekleyebilecek ek bilgiler toplayın. 
# 4. Verileri, mevcut bilgilerle tutarlı bir biçim elde edecek şekilde işleyin. 
# 5. Mevcut ve yeni bilgiler arasındaki ilişkileri ve doğruluk değerlerini tanımlayın. 
# 6. Hedefe ulaşılıp ulaşılmadığını belirleyin. 
# 7. Yeni veriler ve bunun başarı olasılığı üzerindeki etkisi ışığında hedefi değiştirin. 
# 8. Hedefe ulaşılana (doğru bulunana) veya hedefe ulaşma olasılıkları tükenene (yanlış bulunana) kadar 2'den 7'ye kadar olan Adımları gerektiği kadar tekrarlayın.

####################################################################################################

# As part of deciding what intelligence actually involves, categorizing intelligence is also helpful. 
# Humans don’t use just one type of intelligence, but rather rely on multiple intelligences to perform tasks. 
# Howard Gardner of Harvard has defined a number of these types of intelligence 
# (see http://www.pz.harvard.edu/projects/multipleintelligences for details), 
# and knowing them helps you to relate them to the kinds of tasks that a computer can simulate as intelligence. 
# Here is a modified version of these intelligences with additional description:

# Visual-spatial: Physical environment intelligence used by people like sailors and architects (among many others). 
# To move at all, humans need to understand their physical environment — that is, its dimensions and characteristics. 
# Every robot or portable computer intelligence requires this capability, but the capability is often difficult to simulate 
# (as with self-driving cars) or less than accurate (as with vacuums that rely as much on bumping as they do on moving intelligently).

# Bodily-kinesthetic: Body movements, such as those used by a surgeon or a dancer, require precision and body awareness. 
# Robots commonly use this kind of intelligence to perform repetitive tasks, often with higher precision than humans, 
# but sometimes with less grace. It’s essential to differentiate between human augmentation, such as a surgical device that provides a surgeon 
# with enhanced physical ability, and true independent movement. The former is simply a demonstration of mathematical ability 
# in that it depends on the surgeon for input.

# Creative: Creativity is the act of developing a new pattern of thought that results in unique output in the form of art, music, and writing. 
# A truly new kind of product is the result of creativity. An AI can simulate existing patterns of thought and even combine them to create
# what appears to be a unique presentation but is really just a mathematically based version of an existing pattern. In order to create, 
# an AI would need to possess self-awareness, which would require intrapersonal intelligence.

# Interpersonal: Interacting with others occurs at several levels. The goal of this form of intelligence is to obtain, exchange, give, 
# and manipulate information based on the experiences of others. Computers can answer basic questions because of keyword input, not understanding. 
# The intelligence occurs while obtaining information, locating suitable keywords, and then giving information based on those keywords. 
# Cross-referencing terms in a lookup table and then acting upon the instructions provided by the table demonstrates logical intelligence, 
# not interpersonal intelligence.

# Intrapersonal: Looking inward to understand one’s own interests and then setting goals based on those interests is currently a human-only kind of intelligence. 
# As machines, computers have no desires, interests, wants, or creative abilities. An AI processes numeric input using a set of algorithms and provides 
# an output — it isn’t aware of anything that it does, nor does it understand anything that it does.

# Linguistic: Working with words is an essential tool for communication because spoken and written information exchange is far faster than any other form. 
# This form of intelligence includes understanding spoken and written input, managing the input to develop an answer, and providing an understandable answer as output. 
# In many cases, computers can barely parse input into keywords, can’t actually understand the request at all, and output responses that may not be understandable at all. 
# In humans, spoken and written linguistic intelligence come from different areas of the brain 
# (https://releases.jhu.edu/2015/05/05/say-what-how-thebrain-separates-our-ability-to-talk-and-write/), which means that even with humans, 
# someone who has high written linguistic intelligence may not have similarly high spoken linguistic intelligence. 
# Computers don’t currently separate written and spoken linguistic ability.

# Logical-mathematical: Calculating a result, performing comparisons, exploring patterns, and considering relationships are all areas in which computers currently excel. 
# When you see a computer beat a human on a game show, this is the only form of intelligence, out of seven, that you’re actually seeing. 
# Yes, you might see small bits of other kinds of intelligence, but this one is the focus. 
# Basing an assessment of human versus computer intelligence on just one area isn’t a good idea.

####################################################################################################

# Discovering four ways to define AI
# As described in the previous section, the first concept that’s important
# to understand is that AI doesn’t really have anything to do with
# human intelligence. Yes, some AI is modeled to simulate human
# intelligence, but that’s what it is: a simulation. When thinking about
# AI, notice an interplay between goal seeking, data processing used to
# achieve that goal, and data acquisition used to better understand the
# goal. AI relies on algorithms to achieve a result that may or may not
# have anything to do with human goals or methods of achieving those
# goals. With this understanding in mind, you can categorize AI in four
# ways:
# Acting humanly: When a computer acts like a human, it best
# reflects the Turing test, in which the computer succeeds when
# differentiation between the computer and a human isn't possible
# (see https://www.turing.org.uk/scrapbook/test.html for
# details). This category also reflects what the media would have
# you believe AI is all about. You see it employed for technologies
# such as natural language processing, knowledge representation,
# automated reasoning, and machine learning (all four of which
# must be present to pass the test).
# Thinking humanly: When a computer thinks as a human, it
# performs tasks that require intelligence (as contrasted with rote
# procedures) from a human to succeed, such as driving a car. To
# determine whether a program thinks like a human, you must have
# some method of determining how humans think, which the
# cognitive modeling approach defines. This model relies on three
# techniques that are used to create a model, which forms the basis
# for a simulation:
# Introspection: Detecting and documenting the techniques
# used to achieve goals by monitoring one’s own thought
# processes.
# Psychological testing: Observing a person’s behavior and
# adding it to a database of similar behaviors from other
# persons given a similar set of circumstances, goals,
# resources, and environmental conditions (among other
# things).
# Brain imaging: Monitoring brain activity directly through
# various mechanical means, such as Computerized Axial
# Tomography (CAT), Positron Emission Tomography
# (PET), Magnetic Resonance Imaging (MRI), and
# Magnetoencephalography (MEG).
# Thinking rationally: Applying some type of standard to studying
# how humans think enables the creation of guidelines that describe
# typical human behaviors. A person is considered rational when
# following these behaviors within certain levels of deviation. A
# computer that thinks rationally relies on the recorded behaviors to
# create a guide as to how to interact with an environment based on
# the data at hand. The goal of this approach is to solve problems
# logically, when possible. In many cases, this approach would
# enable the creation of a baseline technique for solving a problem,
# which would then be modified to actually solve the problem. In
# other words, the solving of a problem in principle is often
# different from solving it in practice, but you still need a starting
# point.
# Acting rationally: Studying how humans act in given situations
# under specific constraints enables you to determine which
# techniques are both efficient and effective. A computer that acts
# rationally relies on the recorded actions to interact with an
# environment based on conditions, environmental factors, and
# existing data. As with rational thought, rational acts depend on a
# solution in principle, which may not prove useful in practice.
# However, rational acts do provide a baseline upon which a
# computer can begin negotiating the successful completion of a
# goal.

####################################################################################################

# At the Anaconda Prompt, type conda create -n R_env r-essentials rbase and press Enter. 
# This command creates a new Anaconda environment called R_env. Whenever you want to work with R code,
# you use the R_env environment. Within this environment, conda, the Anaconda command-line utility, 
# installs R essentials and base packages. 

# After the installation process completes, you're still in the  (base) environment. 
# To work with the (R_env), you must type  conda activate R_env at the Anaconda Prompt. 
# You can how  use whatever directory command your platform supports to see a  list of the files that conda installed. 
# To leave the (R_env)  environment and go back to the (base) environment, you type  conda deactivate and press Enter.

####################################################################################################

# SciPy kullanarak bilimsel araçlara erişim

# SciPy yığını (http://www.scipy.org/), ayrıca indirebileceğiniz bir dizi başka paket içerir. 
# Bu paketler matematik, fen ve mühendislik alanlarında destek sağlar. 
# SciPy'yi edindiğinizde, çeşitli türde uygulamalar oluşturmak üzere birlikte çalışmak üzere tasarlanmış bir dizi pakete sahip olursunuz. 
# 
# Bu paketler;
# NumPy 
# SciPy 
# matplotlib 
# Jupyter 
# SymPy 
# pandas
# 
# Elbette bunlar sadece SciPy ana sayfasında listelenen paketler.
# 
# https://www.scipy.org/about.html adresinde bulunan ayrıntılara daha fazla inerseniz, 
# SciPy ekosistemi adı verilen ve SciPy üzerine veya çevresinde oluşturulmuş diğer paketleri keşfedersiniz. 
# Örneğin veri ve hesaplama söz konusu olduğunda şu paketleri bulabilirsiniz: 
# 
# Scikit-image 
# Scikit-learn 
# h5py 
# PyTables
# SciPy 
# 
# paketinin kendisi sayısal entegrasyon ve optimizasyon rutinleri gibi sayısal rutinlere odaklanır. 
# SciPy, birden fazla sorunlu alan için işlevsellik sağlayan genel amaçlı bir pakettir. 
# Ayrıca Scikit-learn, Scikit-image ve statsmodels gibi alana özel paketler için de destek sağlar. 
 


# R, SciPy işlevselliğinin çoğunu dilin bir parçası olarak sağlar. R ile SciPy işlevselliğini 
# karşılaştıran tartışmaları çevrimiçi olarak bulabilirsiniz. Örneğin, R optim ile SciPy optimizasyonunun 
# karşılaştırmasını şu adreste bulabilirsiniz: https://stackoverflow.com/questions/51813317/r-optim-vs-scipy-optimize. 
# İşlevsellik tam olarak aynı olmasa da R ve Python'un SciPy ile eşdeğer sonuçlar üretebileceğini görüyorsunuz.

####################################################################################################

# Conda ve PIP'i güncellemek için şu komutları kullanırsınız:
# conda update 
# conda python -m pip install --upgrade pip 
# 
# Hepsini güncellemek için
# conda update --all 
# 
# Evn için 
# conda create -n TF_env python=3.6 anaconda=2019.03 tensorflow=1.11.0 keras=2.2.4 nb_conda 
# conda activate TF_env 
# python -m pip install --upgrade pip 
# 
# conda deactivate root env dönmek için

# pip freeze | %{$_.split('==')[0]} | %{pip install --upgrade $_} bütün kütüphaneleri güncellemek için

# Notice that this installation is actually using Python 3.6. 
# The Python 3.7.3 version used for the other examples in the book is incompatible with the current version of TensorFlow. 
# 
# This step can require some time to execute because your system will have to download TensorFlow 1.11.0 and Keras 2.2.4 from an online source. 
# After the download is complete, the setup needs to create a complete installation for you. 
# You see the Anaconda prompt return after all the required steps are complete. 
# In the meantime, reading a good technical article or getting coffee can help pass the time. 

####################################################################################################
# Book 2 Interacting with Data Storage 
####################################################################################################

####################################################################################################
# Listeler 
####################################################################################################

# # alist değişir
# def DoChange(aList): 
#     aList.append(4) 
#     return aList 

# aList = [1, 2, 3] 
# print(aList) 
# print(DoChange(aList)) 
# print(aList)


# # alist değişmez
# def DoChange(aList): 
#     newList = aList.copy() 
#     newList.append(4) 
#     return newList 

# aList = [1, 2, 3] 
# print(aList) 
# print(DoChange(aList)) 
# print(aList)

# a = [1, 2, 3, 4]
# b = list(range(1, 13)) 

# print(b) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# c = [a * 2 for a in range(1,5)] 

# print(c) # [2, 4, 6, 8]

# To interact with lists in Python, you use modifications of an index, as shown here: a[0]: Obtains the head of the list, which is 1 in this case a[1:]: Obtains the tail of the list, which is [2,3,4,5,6] in this case
# a[:-1]: Obtains all but the last element, which is [1,2,3,4,5] in this case 
# a[-1:]: Obtains just the last element, which is 6 in this case 
# a[:-3]: Requires the number of elements you want to see as input and then shows that number from the beginning of the list, which is [1,2,3] in this case 
# a[-3:]: Requires the number of elements you don't want to see as input and then shows the remainder of the list after dropping the required elements, which is [4,5,6] in this case 

# len(a): Returns the number of elements in a list. 
# not a: Checks for an empty list. This check is different from a is None, which checks for an actual null value — a not being defined. 
# min(a): Returns the smallest list element. 
# max(a): Returns the largest list element. 
# sum(a): Adds the numbers of the list together.

# a = [1, 2, 3, 4, 5, 6]
# from functools import reduce 

# # print(reduce(lambda x, y: x * y, a)) # hepsinin çarpımı 720

# # prod = lambda z: reduce(lambda x, y: x * y, z) 
# # print(prod(a))

# # avg = lambda x: sum(x) // len(x) 
# # print(avg(a))

# # reverse = lambda x: x[::-1] 
# # b = reverse(a) 
# # print(b)

####################################################################################################
# Sözlükler ve Setler
####################################################################################################

# myDict = {"First": 1, "Second": 2, "Third": 3}

####################################################################################################

#frozenset

# myFSet = frozenset([1, 2, 3, 4, 5, 6])
# for entry in myFSet: 
#     if entry == 1: 
#         print(True)

####################################################################################################

# print ("My name is %s and weight is %d kg!" % ('Zara', 21)) # My name is Zara and weight is 21 kg!

# Format Symbol	Conversion
# %c	            character
# %s	            string conversion via str() prior to formatting
# %i	            signed decimal integer
# %d	            signed decimal integer
# %u	            unsigned decimal integer
# %o	            octal integer
# %x	            hexadecimal integer (lowercase letters)
# %X	            hexadecimal integer (UPPERcase letters)
# %e	            exponential notation (with lowercase 'e')
# %E	            exponential notation (with UPPERcase 'E')
# %f	            floating point real number
# %g	            the shorter of %f and %e
# %G	            the shorter of %f and %E

# Symbol	Functionality
# *	    argument specifies width or precision
# -	    left justification
# +	    display the sign
# <sp>	leave a blank space before a positive number
# #	    add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.
# 0	    pad from left with zeros (instead of spaces)
# %	    '%%' leaves you with a single literal '%'
# (var)	mapping variable (dictionary arguments)
# m.n.	m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)

# Sr.No.	Methods with Description
# 1	capitalize()
# Capitalizes first letter of string

# 2	center(width, fillchar)
# Returns a space-padded string with the original string centered to a total of width columns.

# 3	count(str, beg= 0,end=len(string))
# Counts how many times str occurs in string or in a substring of string if starting index beg and ending index end are given.

# 4	decode(encoding='UTF-8',errors='strict')
# Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.

# 5	encode(encoding='UTF-8',errors='strict')
# Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.

# 6	endswith(suffix, beg=0, end=len(string))
# Determines if string or a substring of string (if starting index beg and ending index end are given) ends with suffix; returns true if so and false otherwise.

# 7	expandtabs(tabsize=8)
# Expands tabs in string to multiple spaces; defaults to 8 spaces per tab if tabsize not provided.

# 8	find(str, beg=0 end=len(string))
# Determine if str occurs in string or in a substring of string if starting index beg and ending index end are given returns index if found and -1 otherwise.

# 9	index(str, beg=0, end=len(string))
# Same as find(), but raises an exception if str not found.

# 10	isalnum()
# Returns true if string has at least 1 character and all characters are alphanumeric and false otherwise.

# 11	isalpha()
# Returns true if string has at least 1 character and all characters are alphabetic and false otherwise.

# 12	isdigit()
# Returns true if string contains only digits and false otherwise.

# 13	islower()
# Returns true if string has at least 1 cased character and all cased characters are in lowercase and false otherwise.

# 14	isnumeric()
# Returns true if a unicode string contains only numeric characters and false otherwise.

# 15	isspace()
# Returns true if string contains only whitespace characters and false otherwise.

# 16	istitle()
# Returns true if string is properly "titlecased" and false otherwise.

# 17	isupper()
# Returns true if string has at least one cased character and all cased characters are in uppercase and false otherwise.

# 18	join(seq)
# Merges (concatenates) the string representations of elements in sequence seq into a string, with separator string.

# 19	len(string)
# Returns the length of the string

# 20	ljust(width[, fillchar])
# Returns a space-padded string with the original string left-justified to a total of width columns.

# 21	lower()
# Converts all uppercase letters in string to lowercase.

# 22	lstrip()
# Removes all leading whitespace in string.

# 23	maketrans()
# Returns a translation table to be used in translate function.

# 24	max(str)
# Returns the max alphabetical character from the string str.

# 25	min(str)
# Returns the min alphabetical character from the string str.

# 26	replace(old, new [, max])
# Replaces all occurrences of old in string with new or at most max occurrences if max given.

# 27	rfind(str, beg=0,end=len(string))
# Same as find(), but search backwards in string.

# 28	rindex( str, beg=0, end=len(string))
# Same as index(), but search backwards in string.

# 29	rjust(width,[, fillchar])
# Returns a space-padded string with the original string right-justified to a total of width columns.

# 30	rstrip()
# Removes all trailing whitespace of string.

# 31	split(str="", num=string.count(str))
# Splits string according to delimiter str (space if not provided) and returns list of substrings; split into at most num substrings if given.

# 32	splitlines( num=string.count('\n'))
# Splits string at all (or num) NEWLINEs and returns a list of each line with NEWLINEs removed.

# 33	startswith(str, beg=0,end=len(string))
# Determines if string or a substring of string (if starting index beg and ending index end are given) starts with substring str; returns true if so and false otherwise.

# 34	strip([chars])
# Performs both lstrip() and rstrip() on string.

# 35	swapcase()
# Inverts case for all letters in string.

# 36	title()
# Returns "titlecased" version of string, that is, all words begin with uppercase and the rest are lowercase.

# 37	translate(table, deletechars="")
# Translates string according to translation table str(256 chars), removing those in the del string.

# 38	upper()
# Converts lowercase letters in string to uppercase.

# 39	zfill (width)
# Returns original string leftpadded with zeros to a total of width characters; intended for numbers, zfill() retains any sign given (less one zero).

# 40	isdecimal()
# Returns true if a unicode string contains only decimal characters and false otherwise.

####################################################################################################

# » Kontrol karakteri: Sekme (\t), satırsonu (\n) ve satırbaşı (\r) gibi kontrol karakterlerine erişim sağlar. 
# \n karakterinin (\u000D değerine sahip olan) \r karakterinden (\u000A değerine sahip olan) farklı olduğunu unutmayın.
# 
# » Sayısal karakter: Sayısal değere dayalı bir karakter tanımlar. 
# Yaygın türler arasında sekizlik (\nnn), onaltılık (\xnn) ve Unicode (\unnnn) bulunur. 
# Her durumda, n'yi karakterin sayısal değeriyle değiştirirsiniz; örneğin Unicode'da büyük A harfi için \u0041. 
# Kodu doldurmak için doğru rakam sayısını girmeniz ve 0'ları kullanmanız gerektiğini unutmayın.
# 
# » Kaçan özel karakter: Düzenli ifade derleyicisinin ( veya [ gibi özel bir karakteri, 
# özel bir karakter yerine değişmez bir karakter olarak görmesi gerektiğini belirtir. 
# Örneğin, alt ifade \( bir karakterin başlangıcı yerine bir açılış parantezini belirtir) .

# Bir joker karakter bir tür karakteri tanımlayabilir ancak belirli bir karakteri asla tanımlayamaz. 
# Herhangi bir rakamı veya herhangi bir karakteri belirtmek için joker karakterleri kullanırsınız. 
# Aşağıdaki listede yaygın olarak kullanılan joker karakterler anlatılmaktadır. 
# Diliniz bu karakterlerin tamamını desteklemiyor olabilir veya listelenenlere ek olarak karakterler tanımlıyor olabilir. 
# Aşağıdaki karakterlerin eşleştiği şeyler:

####################################################################################################

# Character   Matches With
# .           Any character (with the possible exception of the newline character or other control characters)
# \w	      Any word character
# \W	      Any nonword character
# \s	      Any whitespace character
# \S	      Any non-whitespace character
# \d	      Any decimal digit
# \D	      Any nondecimal digit

####################################################################################################

# Çapalar normal bir ifadeyle nasıl etkileşime geçileceğini tanımlar. 
# Örneğin hedef verinin yalnızca başlangıcı veya bitişiyle çalışmak isteyebilirsiniz. 
# Her programlama dilinin çapalarla ilgili bazı özel koşulları uyguladığı görülmektedir, 
# ancak hepsi temel sözdizimine uyar (dil çapayı desteklediğinde). 
# Aşağıdaki tabloda yaygın olarak kullanılan ankrajlar tanımlanmaktadır:

# Anchor	                What It Does
# ^	                        Looks at the start of the string.
# $	                        Looks at the end of the string.
# *                         Matches zero or more occurrences of the specified character.
# +	                        Matches one or more occurrences of the specified character. The character must appear at least once.
# ?	                        Matches zero or one occurrences of the specified character.
# {m}	                    Specifies m number of the preceding characters required for a match.
# {m,n}                     Specifies the range from m to n, which is the number of the preceding characters required for a match.
# expression|expression     Performs or searches where the regular expression  compiler will locate either one expression or the other expression and count it as a match.

# Bu çapalardan bazılarını bulmayı zor bulabilirsiniz.
# Eşleştirme fikri, bir talebi karşılayan belirli bir koşulu tanımlamak anlamına gelir. 
# Örneğin, şu modeli göz önünde bulundurun: h?t, hit ve hot ile eşleşir, ancak yuha veya heat ile eşleşmez, çünkü ? çapa yalnızca bir karakterle eşleşir. 
# Bunun yerine hoot ve heat'i de eşleştirmek istiyorsanız h*t kullanırsınız çünkü * çapası birden fazla karakterle eşleşebilir. 
# İstenilen sonucu elde etmek için doğru çapayı kullanmak çok önemlidir.

####################################################################################################

# Gruplandırma yapılarını kullanarak alt ifadeleri tanımlama

# Gruplandırma yapısı, normal ifade derleyicisine bir dizi karakteri grup olarak ele almasını söyler. 
# Örneğin, gruplandırma yapısı [a-z] normal ifade derleyicisine a ile z arasındaki tüm küçük harfleri aramasını söyler. 
# Bununla birlikte, gruplandırma yapısı [az] (a ve z arasında tire olmadan) normal ifade derleyicisine yalnızca a ve z harflerini aramasını, 
# aradaki hiçbir şeyi aramamasını söyler ve gruplandırma yapısı [^a-z] normal ifade derleyicisine bunu söyler. 
# a'dan z'ye kadar olan küçük harfler dışındaki her şeyi aramak için.
# Aşağıdaki listede yaygın olarak kullanılan gruplandırma yapıları açıklanmaktadır.
# Bu listedeki italik harfler ve kelimeler yer tutuculardır.

# Construct         What It Means
# [x]	            Look for a single character from the characters specified by x.
# [x-y]	            Search for a single character from the range of characters specified by x and y.
# [Aexpression]     Locate any single character not found in the character expression.
# (expresson)       Define a regular expression group. For example, ab{3} would match the letter a and then three copies of the letter b, that is, abbb. 
#                   However, (ab){3} would match three copies of the expression ab: ababab.

####################################################################################################

# Python'daki kalıp eşleştirme, diğer birçok dilde bulunan işlevlerle yakından eşleşir. 
# Python, düzenli ifade (yeniden) kitaplığını kullanarak güçlü kalıp eşleştirme yetenekleri sağlar (https://docs.python.org/3.6/library/re.html). 
# https://www.regular-expressions.info/python.html adresindeki kaynak şunları sağlar: Python yeteneklerine iyi bir genel bakış. 
# Aşağıdaki bölümlerde bir dizi örnek kullanılarak Python işlevselliği ayrıntılı olarak anlatılmaktadır.

# import re 
# vowels = "[aeiou]" 
# print(re.search(vowels, "This is a test sentence.").group())

# search() işlevi yalnızca ilk eşleşmeyi bulur, dolayısıyla sesli harflerdeki ilk öğe olduğundan i harfini çıktı olarak görürsünüz. 
# Gerçek bir değerin çıktısını almak için group() işlev çağrısına ihtiyacınız vardır, çünkü search(), 
# https://docs.python.org/3.6/library/re.html#match-objects 'da açıklandığı gibi bir eşleşme nesnesi döndürür.

####################################################################################################

# import re
# vowels = "[aeiou]"
# print(re.match(vowels, "This is a test sentence."))
# # sesli harflerin hiçbiri cümlenin başında görünmediğinden Yok değerini döndürür.
# print(re.match("a", "abcde").group())
# # a değerini döndürür çünkü a harfi test dizesinin başında görünür.
# print(re.findall(vowels, "This is a test sentence."))
# # bütün ünlü harfleri yazdırır.

# testSentence = "This is a test sentence." 
# m = re.search(vowels, testSentence) 
# while m: 
#     print(testSentence[m.start():m.end()]) 
#     testSentence = testSentence[m.end():] 
#     m = re.search(vowels, testSentence)

####################################################################################################

# import re
# testString = "This is\ta test string.\nYippee!" 
# whiteSpace = "[\s]" 
# print(re.split(whiteSpace, testString))

# testString = "Stan says hello to Margot from Estoria." 
# pattern = "Stan|hello|Margot|Estoria" 
# replace = "Unknown" 
# print(re.sub(pattern, replace, testString))

####################################################################################################
# Working with Recursion
####################################################################################################

# def doRep(x, n): 
#     y = [] 
#     if n == 0: 
#         return [] 
#     else: 
#         y = doRep(x, n - 1) 
#         y.append(x) 
#         return y
# print(doRep(3, 2))

####################################################################################################

# def doRep(x, n): 
#     y = [] 
#     if n == 0: 
#         return [] 
#     else: 
#         y = doRep(x, n - 1) 
#         print(y) 
#         y.append(x) 
#         return y
# print(doRep(4, 5))

####################################################################################################

# myList = [1, 2, 3, 4, 5]
# def lSum(list): 
#     if not list: 
#         return 0 
#     else: 
#         return list[0] + lSum(list[1:])
# print(lSum(myList))

# myList = [1, 2, 3, 4, 5]
# lSum2 = lambda list: 0 if not list \
#     else list[0] + lSum2(list[1:])
    
# print(lSum2(myList))

####################################################################################################

# myDic = {"A":{"A": 1, "B":{"B": 2, "C":{"C": 3}}}, "D": 4}

# def findKey(obj, key): 
#     for k, v in obj.items(): 
#         if isinstance(v, dict): 
#             findKey(v, key) 
#         else: 
#             if key in obj: 
#                 print(obj[key])
# print(findKey(myDic, "B"))

####################################################################################################

# def doAdd(x, y): 
#     return x + y 

# def doSub(x, y): 
#     return x - y

# def compareWithHundred(function, x, y): 
#     z = function(x, y) 
#     out = lambda x: "GT" if 100 > x \
#         else "EQ" if 100 == x else "LT" 
#     return out(z)

# print(compareWithHundred(doAdd, 99, 2)) 
# print(compareWithHundred(doSub, 99, 2)) 
# print(compareWithHundred(doAdd, 99, 1))


####################################################################################################

# myList = [1, 2, 3, 4, 5] 
# print(myList[:2]) 
# print(myList[2:]) 
# print(myList[2:3])

# myList2 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
# print(myList2[:2]) 
# print(myList2[2:]) 
# print(myList2[2:3])

# def dice(lst, rb, re, cb, ce): 
#     lstr = lst[rb:re] 
#     lstc = [] 
#     for i in lstr: 
#         lstc.append(i[cb:ce]) 
#     return lstc

# myList3 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
# print(dice(myList3, 1, 4, 1, 2))

####################################################################################################

# # Mapping your data

# square = lambda x: x**2 
# double = lambda x: x + x 
# items = [0, 1, 2, 3, 4] 
# # print(list(map(square, items)))
# # print(list(map(double, items)))

# funcs = [square, double]
# for i in items: 
#     value = list(map(lambda items: items(i), funcs)) 
#     print(value)

####################################################################################################

# # Filtering your data

# items = [0, 1, 2, 3, 4, 5]
# print(list(filter(lambda x: x % 2 == 1, items))) 
# print(list(filter(lambda x: x > 3, items))) 
# print(list(filter(lambda x: x % 3 == 0, items)))

####################################################################################################

# # Organizing data

# from operator import itemgetter 

# original = [(1, "Hello"), (4, "Yellow"), (5, "Goodbye"), (2, "Yes"), (3, "No")]
# print(sorted(original))
# print(sorted(original, reverse=True))
# print(sorted(original, key=lambda x: x[1]))
# original = [(1, "Hello"), (4, "Yellow"), (5, "goodbye"), (2, "Yes"), (3, "No")]
# print()
# print(sorted(original, key=lambda x: x[1]))
# print(sorted(original, key=lambda x: str.lower(x[1])))
# print(sorted(original, key=itemgetter(1)))
# print(sorted(original, key=lambda x: len(x[1])))

####################################################################################################
# Working with Scalars, Vectors, and Matrices
####################################################################################################

# Considering the Data Forms

# Scalar

# anA = chr(65) 
# print(type(anA))

# from fractions import Fraction # kesirli sayı
# x = Fraction(2, 3) 
# print(x) 
# print(type(x))

####################################################################################################

# Python için NumPy kütüphanesi tarafından sağlanan skalerler hakkında daha fazlasını şu adreste bulabilirsiniz:
# https://www.numpy.org/devdocs/reference/arrays.scalars.html. 
# Ayrıca çoğu dilin yerel türleri genişletmenin yollarını sağladığını da göreceksiniz (Ek ayrıntılar için;
# https://docs.python.org/3/extending/newtypes.html ve http://greenteapress.com/thinkpython/thinkCSpy/html/app02.html
# ).

####################################################################################################

# import numpy as np

# myVect1 = np.array([1, 2, 3, 4]) 
# print(myVect1) 
# myVect2 = np.arange(1, 10, 2) 
# print(myVect2)
# myVect3 = np.array(np.int16([1, 2, 3, 4])) 
# print(myVect3) 
# print(type(myVect3)) 
# print(type(myVect3[0]))
# myVect4 = np.ones(4, dtype=np.int16) 
# print(myVect4) #4 tane 1 olan liste yazar
# myVect5 = [1, 2, 3, 4] 
# print(type(myVect5[0])) 
# print(type((2 ** np.array(myVect5))[0]))

# a = np.array([1, 2, 3, 4]) 
# b = np.array([2, 2, 4, 4])
# print(a == b) 
# print(a < b)

# Bu işlevler için sayısal girişi de kullanabilirsiniz. Sayısal giriş kullanıldığında 0 yanlış, 1 doğrudur. 
# Karşılaştırmalarda olduğu gibi, tek bir arama yapsanız bile işlevler öğe bazında çalışır. 
# Mantık fonksiyonları hakkında daha fazla bilgiyi şu adreste bulabilirsiniz:
# https://docs.scipy.org/doc/numpy-1.10.0/reference/routines.logic.html.

####################################################################################################

# Array

# import numpy as np
# myVect = np.array([1, 2, 3, 4])
# print(myVect * myVect) 
# print(np.multiply(myVect, myVect))
# print(myVect.dot(myVect)) # çarpımlarının toplamını verir

####################################################################################################

# Matrix

# import numpy as np

# myMatrix1 = np.array([[1,2,3], [4,5,6], [7,8,9]]) 
# print(myMatrix1)
# print()
# print()

# myMatrix2 = np.array([[[1,2], [3,4]], [[5,6], [7,8]]]) 
# print(myMatrix2)
# print(myMatrix2[0, 1, 1])

# myMatrix3 = np.ones([4,4], dtype=np.int32)
# print(myMatrix3)

# myMatrix4 = np.ones([4,4,4], dtype=np.bool_) 
# print(myMatrix4)

# Sıfırlarla dolu bir matris, birim matris oluşturma ve diğer ihtiyaçları karşılamaya yönelik işlevler de vardır. 
# Vektör ve matris dizisi oluşturma işlevlerinin tam listesini 
# https://docs.scipy.org/doc/numpy/reference/routines.array-creation.html adresinde bulabilirsiniz.

####################################################################################################

# import numpy as np

# myMatrix5 = np.mat([[1,2,3], [4,5,6], [7,8,9]]) 
# print(myMatrix5)

# myMatrix3 = np.ones([4,4], dtype=np.int32)
# print(myMatrix3)
# print(np.asmatrix(myMatrix3)) Array formunu matrix formuna çevirir. asmatrix 3 boyutlu çalışamaz.

####################################################################################################

# import numpy as np

# a = np.array([[1,2,3],[4,5,6]]) 
# b = np.array([[1,2,3],[4,5,6]])
# print(a*b) # çarpacağın her matrix aynı formda olmalı.

####################################################################################################

# import numpy as np

# a = np.array([[1,2,3],[4,5,6]]) 
# b = np.array([[1,2,3,4],[3,4,5,6],[5,6,7,8]])
# print(a.dot(b))

# [[22 28 34 40] 
#  [49 64 79 94]]

# Çıkış dizisinde 22'nin [0,0] indeksindeki değeri elde etmek için 
# a[0,0]*b[0,0] (ki bu 1), a[0,1]*b[1,0] (ki bu 6'dır) ve a[0,2]*b[2,0] (ki bu 15) ile 22 değeri elde edilir. 
# Diğer girişler tam olarak aynı şekilde çalışır.

# a = np.mat([[1,2,3],[4,5,6]]) 
# b = np.mat([[1,2,3,4],[3,4,5,6],[5,6,7,8]])
# print(a*b)

# İki matris nesnesi kullanarak öğe öğe çarpımı gerçekleştirmek için numpy multiply işlevini kullanmanız gerekir.

####################################################################################################

# import numpy as np

# changeIt = np.array([1,2,3,4,5,6,7,8])
# print(changeIt) 
# print() 
# print(changeIt.reshape(2,4)) 
# print() 
# print(changeIt.reshape(2,2,2))

# changeIt2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]]) 
# print(np.transpose(changeIt2))

# print(np.identity(4))

# a = np.array([[1,2], [3,4]]) 
# print(a)
# b = np.linalg.inv(a)
# print(b)
# print(np.allclose(np.dot(a,b), np.identity(2)))

####################################################################################################

# import numpy as np

# inputs = np.array([5, 10, 15])
# weights = np.array([[.5,.2,-1], [.3,.4,.1], [-.2,.1,.3]])
# result = np.dot(inputs, weights) 
# print(result)

####################################################################################################

# import numpy as np

# def doAdd(a, b): 
#     return a + b

# vectAdd = np.vectorize(doAdd) 
# print(vectAdd([1, 2, 3, 4], [1, 2, 3, 4])) #[2 4 6 8]
# print() 

# x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9],], 
#               [[11,12,13], [14,15,16], [17,18,19],],
#               [[21,22,23], [24,25,26], [27,28,29]]])

# print(x[1])
# print() 
# print(x[:,1])
# print() 


# print(x[1,1]) 
# print(x[:,1,1]) 
# print(x[1,:,1]) 
# print() 
# print(x[1:2, 1:2])
####################################################################################################

# import pandas as pd
# df = pd.DataFrame({'A': [2,3,1], 
#                    'B': [1,2,3],
#                    'C': [5,3,4]})
# df1 = pd.DataFrame({'A': [4], 
#                     'B': [4],
#                     'C': [4]})

# df = df._append(df1) 
# df = df.reset_index(drop=True) 
# print(df)

# df.loc[df.last_valid_index() + 1] = [5, 5, 5] 
# print() 
# print(df)
# df2 = pd.DataFrame({'D': [1, 2, 3, 4, 5]}) 
# df = pd.DataFrame.join(df, df2) 
# print() 
# print(df)

####################################################################################################

# Removing data

# import pandas as pd
# df = pd.DataFrame({'A': [2,3,1], 
#                    'B': [1,2,3],
#                    'C': [5,3,4]})
# df = df.drop(df.index[[1]]) 
# print(df)
# df = df.drop('B', axis=1)
# print() 
# print(df)

####################################################################################################

# Sorting and shuffling

# import pandas as pd 
# import numpy as np

# df = pd.DataFrame({'A': [2,1,2,3,3,5,4], 
#                    'B': [1,2,3,5,4,2,5], 
#                    'C': [5,3,4,1,1,2,3]})

# df = df.sort_values(by=['A', 'B'], ascending=[True, True]) 
# df = df.reset_index(drop=True) # Her sıralamadan sonra kullan.
# print(df)
# index = df.index.tolist() 
# np.random.shuffle(index) 
# df = df.loc[df.index[index]] 
# df = df.reset_index(drop=True) 
# print() 
# print(df)

####################################################################################################

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({'Map': [0,0,0,1,1,2,2], 
#                    'Values': [1,2,3,5,4,2,5]})
# df['S'] = df.groupby('Map')['Values'].transform(np.sum) 
# df['M'] = df.groupby('Map')['Values'].transform(np.mean) 
# df['V'] = df.groupby('Map')['Values'].transform(np.var)
# print(df)

####################################################################################################

# class binaryTree: 
#     def __init__(self, nodeData, left=None, right=None): 
#         self.nodeData = nodeData 
#         self.left  = left 
#         self.right = right 
    
#     def __str__(self): 
#         return str(self.nodeData)
    
# tree = binaryTree("Root") 
# BranchA = binaryTree("Branch A") 
# BranchB = binaryTree("Branch B") 
# tree.left = BranchA 
# tree.right = BranchB 
# LeafC = binaryTree("Leaf C") 
# LeafD = binaryTree("Leaf D") 
# LeafE = binaryTree("Leaf E") 
# LeafF = binaryTree("Leaf F") 
# BranchA.left = LeafC 
# BranchA.right = LeafD 
# BranchB.left = LeafE 
# BranchB.right = LeafF

# def traverse(tree): 
#     if tree.left != None: 
#         traverse(tree.left) 
#     if tree.right != None: 
#         traverse(tree.right) 
#     print(tree.nodeData)
    

# traverse(tree)

####################################################################################################

# graph = {'A': ['B', 'F'], 
#          'B': ['A', 'C'],
#          'C': ['B', 'D'],
#          'D': ['C', 'E'],
#          'E': ['D', 'F'],
#          'F': ['E', 'A']}

# def find_path(graph, start, end, path=[]): 
#     path = path + [start] 
    
#     if start == end: 
#         print("Ending") 
#         return path
    
#     for node in graph[start]: 
#         print("Checking Node ", node) 
        
#         if node not in path: 
#             print("Path so far ", path) 
            
#             newp = find_path(graph, node, end, path) 
#             if newp: 
#                 return newp

# find_path(graph, 'B', 'E')

####################################################################################################

# import pandas as pd 
# color_table = pd.io.parsers.read_csv("Colors.txt", sep='\t')
# print(color_table)
# print()

# print("Fixed Width:")
# row = 0
# with open("FixedWidth.txt", "r") as FW: 
#     while True: 
#         Color = FW.read(6) 
#         if not Color: 
#             break
#         Value = FW.read(5) 
#         if row == 0: 
#             color_table2 = pd.DataFrame( 
#                 columns=[Color, Value])
#         else: 
#             color_table2 = color_table2._append( 
#                 [{'Color ': Color, 'Value': Value}], 
#                 ignore_index=True, sort=False) 
#         row=row+1
# print(color_table2)

# color_table3 = pd.read_fwf("FixedWidth2.txt", widths=[6, 5])
# print(color_table3)

####################################################################################################

# import pandas as pd 
# titanic = pd.read_csv("Titanic.csv") 
# X = titanic[['age']]
# X = titanic[['age']].values 
# print(X)

# color_table4 = pd.read_csv("Colors.csv") 
# print("Original types:\n", color_table4.dtypes, "\n")
# for col in color_table4.columns: 
#     col_split = col.split('.') 
#     color_table4 = color_table4.rename( columns={col: col_split[0]}) 
#     color_table4 = color_table4.astype( {col_split[0]: col_split[1]})
# print("New types:\n", color_table4.dtypes, "\n") 
# print(color_table4)
####################################################################################################

# from lxml import objectify 
# import pandas as pd
# xml = objectify.parse(open('XMLData.xml')) 
# root = xml.getroot()
# df = pd.DataFrame(columns=('Number', 'String', 'Boolean'))
# for i in range(0,4): 
#     obj = root.getchildren()[i].getchildren() 
#     row = dict(zip(['Number', 'String', 'Boolean'], 
#                    [obj[0].text, obj[1].text, 
#                     obj[2].text])) 
#     row_s = pd.Series(row)
#     row_s.name = i 
#     df = df._append(row_s)
# print(df)

####################################################################################################

# from lxml import objectify 
# import pandas as pd 
# from distutils import util

# xml = objectify.parse(open('XMLData.xml')) 
# root = xml.getroot() 
# df = pd.DataFrame(columns=('Number', 'Boolean'))
# for i in range(0, 4): 
#     obj = root.getchildren()[i].getchildren() 
#     row = dict(zip(['Number', 'Boolean'], 
#                    [obj[0].pyval, 
#                     bool(util.strtobool(obj[2].text))])) 
#     row_s = pd.Series(row) 
#     row_s.name = obj[1].text 
#     df = df._append(row_s)
    
# print(type(df.loc['First']['Number'])) 
# print(type(df.loc['First']['Boolean']))


####################################################################################################

# from lxml import objectify 
# import pandas as pd 
# from distutils import util

# xml = objectify.parse(open('XMLData.xml')) 
# root = xml.getroot()

# map_number = map(int, root.xpath('Record/Number')) 
# map_bool = map(str, root.xpath('Record/Boolean')) 
# map_bool = map(util.strtobool, map_bool) 
# map_bool = map(bool, map_bool) 
# map_string = map(str, root.xpath('Record/String')) 

# data = list(zip(map_number, map_bool))

# df = pd.DataFrame(data, 
#                   columns=('Number', 'Boolean'), 
#                   index = list(map_string))
# print(df)
# print(type(df.loc['First']['Number'])) 
# print(type(df.loc['First']['Boolean']))

####################################################################################################

# import pandas as pd
# xls = pd.ExcelFile("Values.xls") 
# trig_values = xls.parse('Sheet1', index_col=None, na_values=['NA'])
# print(trig_values)

####################################################################################################

# from skimage.io import imread 
# from skimage.transform import resize 
# from matplotlib import pyplot as plt 
# import matplotlib.cm as cm
# example_file = ("http://upload.wikimedia.org/" + "wikipedia/commons/7/7d/Dog_face.png") 
# image = imread(example_file, as_gray=True) 
# plt.imshow(image, cmap=cm.gray) 
# plt.show()
# print("data type: %s, shape: %s" % (type(image), image.shape))

# image2 = image[5:70,0:70] 
# plt.imshow(image2, cmap=cm.gray) 
# plt.show()

# image3 = resize(image2, (30, 30), mode='symmetric') 
# plt.imshow(image3, cmap=cm.gray) 
# print("data type: %s, shape: %s" % (type(image3), image3.shape))

# image_row = image3.flatten() 
# print("data type: %s, shape: %s" % (type(image_row), image_row.shape))

####################################################################################################

# from sklearn.datasets import fetch_california_housing 
# california = fetch_california_housing() 
# print(california.data.shape)

# from keras.datasets import imdb
# top_words = 10000 
# ((x_train, y_train), (x_test, y_test)) = imdb.load_data(num_words=top_words, seed=21) 
# print("Training examples: %i" % len(x_train)) 
# print("Test examples: %i" % len(x_test))

####################################################################################################

# import urllib.request

# url = "https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/GTSRB_Final_Training_Images.zip" 
# filename = "./GTSRB_Final_Training_Images.zip" 
# urllib.request.urlretrieve(url, filename)

####################################################################################################

# import zipfile 
# from imageio.v2 import imread 
# from skimage.transform import resize

# IMG_SIZE = 32
# TEST_SIZE = 0.2
# X, Xt, y, yt = list(), list(), list(), list()
# archive = zipfile.ZipFile( './GTSRB_Final_Training_Images.zip', 'r') 
# file_paths = [file for file in archive.namelist() 
#               if '.ppm' in file]
# for filename in file_paths: 
#     with archive.open(filename) as img_file: 
#         img = imread(img_file.read()) 
#     img = resize(img, 
#                  output_shape=(IMG_SIZE, IMG_SIZE), 
#                  mode='reflect', anti_aliasing=True) 
#     img_class = int(filename.split('/')[-2]) 
#     if (hash(filename) % 1000) / 1000 > TEST_SIZE: 
#         X.append(img)
#         y.append(img_class) 
#     else: 
#         Xt.append(img) 
#         yt.append(img_class)
# archive.close()

####################################################################################################

# from pytube import YouTube
# link = str(input('Link:\n'))
# yt=YouTube(link)
# print('Link')
# video = yt.streams.get_highest_resolution()
# print('Çözü')
# video.download()
# print('İndi')

####################################################################################################
# Working with a Relational DBMS
####################################################################################################

# from sqlalchemy import create_engine 
# engine = create_engine('sqlite:///:memory:')

####################################################################################################

# import pymongo 
# import pandas as pd 
# from pymongo import MongoClient 
# connection = MongoClient() 
# db = connection.database_name 
# input_data = db.collection_name 
# data = pd.DataFrame(list(input_data.find()))

####################################################################################################
# Manipulating Data Using Basic Algorithms
####################################################################################################



####################################################################################################



####################################################################################################



####################################################################################################



####################################################################################################



####################################################################################################

# Manipulating Data Using Basic Algorithms 319


