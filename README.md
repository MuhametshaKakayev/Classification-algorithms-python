# Classification-algorithms-python
Bu kod, bir kırmızı şarap veri seti üzerinde üç farklı sınıflandırma algoritması olan Naive Bayes, Decision Tree ve K-Nearest Neighbors (KNN) algoritmalarını kullanarak sınıflandırma gerçekleştirir.

İşlemlerin açıklamalarını aşağıda bulabilirsiniz:

---İlk olarak, gerekli kütüphaneler ve modüller içe aktarılır: pandas veri seti işlemleri için, scipy.stats z-skorları hesaplamak için, sklearn.naive_bayes Naive Bayes sınıflandırıcısı için, sklearn.tree Decision Tree sınıflandırıcısı için, ve sklearn.neighbors KNN sınıflandırıcısı için.

---calculate_z_scores fonksiyonu, veri setinin z-skorlarını hesaplar. Verilen bir veri seti üzerinde stats.zscore fonksiyonunu kullanarak z-skorlarını hesaplar ve yazdırır.

----Veri seti (winequality-red.csv) pd.read_csv fonksiyonuyla yüklenir ve bağımsız değişkenler (X) ve hedef değişken (y) olarak ayarlanır. Daha sonra, bağımsız değişkenler üzerinde calculate_z_scores fonksiyonu çağrılarak z-skorları hesaplanır ve X'e atanır.

---train_test_split fonksiyonu kullanılarak veri seti eğitim ve test verilerine bölünür. Eğitim verileri ve etiketleri (X_train ve y_train) ile test verileri ve etiketleri (X_test ve y_test) elde edilir.

---Naive Bayes sınıflandırıcısı (GaussianNB) eğitilir ve test verileri üzerinde tahminler yapılır (y_pred_nb).

----Decision Tree sınıflandırıcısı (DecisionTreeClassifier) eğitilir ve test verileri üzerinde tahminler yapılır (y_pred_dt). Ayrıca, oluşturulan ağaç modeli (dt_classifier) tree.plot_tree fonksiyonuyla görselleştirilir.

---KNN sınıflandırıcısı (KNeighborsClassifier) eğitilir ve test verileri üzerinde tahminler yapılır (y_pred_knn).

---Her bir sınıflandırma algoritması için doğruluk oranları (accuracy_nb, accuracy_dt, accuracy_knn) hesaplanır ve yazdırılır.

----classification_report fonksiyonu kullanılarak her bir sınıflandırma algoritması için sınıflandırma raporları yazdırılır.

---confusion_matrix fonksiyonu kullanılarak her bir sınıflandırma algoritması için Confusion Matrix'ler (cm_nb, cm_dt, cm_knn) oluşturulur ve yazdırılır.

Bu kod, veri setini yükler, z-skorlarını hesaplar, veriyi eğitim ve test verilerine böler, üç farklı sınıflandırma algoritması ile eğitim ve test verilerini tahmin eder, doğruluk oranlarını hesaplar ve Confusion Matrix'leri oluşturur.
