This code performs classification using three different classification algorithms, namely Naive Bayes, Decision Tree, and K-Nearest Neighbors (KNN), on a red wine dataset.

Here are the explanations of the steps:

    First, the necessary libraries and modules are imported: pandas for data manipulation, scipy.stats for calculating z-scores, sklearn.naive_bayes for Naive Bayes classifier, sklearn.tree for Decision Tree classifier, and sklearn.neighbors for KNN classifier.

    The calculate_z_scores function calculates the z-scores of the dataset. It uses the stats.zscore function on the given dataset to compute the z-scores and prints them.

    The dataset (winequality-red.csv) is loaded using the pd.read_csv function, and the independent variables (X) and the target variable (y) are set. Then, the z-scores of the independent variables are calculated by calling the calculate_z_scores function on X.

    The dataset is split into training and test data using the train_test_split function. The training data and labels (X_train and y_train) and the test data and labels (X_test and y_test) are obtained.

    The Naive Bayes classifier (GaussianNB) is trained, and predictions are made on the test data (y_pred_nb).

    The Decision Tree classifier (DecisionTreeClassifier) is trained, and predictions are made on the test data (y_pred_dt). Additionally, the generated tree model (dt_classifier) is visualized using the tree.plot_tree function.

    The KNN classifier (KNeighborsClassifier) is trained, and predictions are made on the test data (y_pred_knn).

    Accuracy rates (accuracy_nb, accuracy_dt, accuracy_knn) are calculated and printed for each classification algorithm.

    Classification reports are printed using the classification_report function for each classification algorithm.

    Confusion matrices (cm_nb, cm_dt, cm_knn) are created and printed for each classification algorithm using the confusion_matrix function.

This code loads the dataset, calculates the z-scores, splits the data into training and test sets, makes predictions using three different classification algorithms, calculates accuracy rates, and creates Confusion Matrices for evaluation.



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
