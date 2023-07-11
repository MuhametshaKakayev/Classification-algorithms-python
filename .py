import pandas as pd
from scipy import stats
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# Veri setinin z-skorlarını hesapla
def calculate_z_scores(data):
  z_scores = stats.zscore(data)
  print("Veri setinin z-skorları:")
  print(z_scores)
  return z_scores

# Veri setini yükle ve z-skorlarını hesapla
df = pd.read_csv("/content/winequality-red.csv")
X = df.drop("quality", axis=1)
y = df["quality"]
X = calculate_z_scores(X)



# Veri setini eğitim ve test verilerine böl
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Naive Bayes sınıflandırıcısını eğit ve test verilerini tahmin et
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)
y_pred_nb = nb_classifier.predict(X_test)

# Decision Tree sınıflandırıcısını eğit ve test verilerini tahmin et
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(X_train, y_train)
y_pred_dt = dt_classifier.predict(X_test)
#agac modeli
from sklearn import tree
model = dt_classifier
tree.plot_tree(model);


# KNN sınıflandırıcısını eğit ve test verilerini tahmin et
knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train, y_train)
y_pred_knn = knn_classifier.predict(X_test)

# Doğruluk oranlarını hesapla
accuracy_nb = np.mean(y_pred_nb == y_test)
accuracy_dt = np.mean(y_pred_dt == y_test)
accuracy_knn = np.mean(y_pred_knn == y_test)

print("Naive Bayes doğruluk oranı:", accuracy_nb)
print(classification_report(y_test, y_pred))
print("---------------------------")
print("Decision Tree doğruluk oranı:", accuracy_dt)
print(classification_report(y_test, y_pred))
print("---------------------------")
print("KNN doğruluk oranı:", accuracy_knn)
print(classification_report(y_test, y_pred))


# Confusion Matrix'leri oluştur ve yazdır
from sklearn.metrics import confusion_matrix

# Naive Bayes Confusion Matrix'i
cm_nb = confusion_matrix(y_test, y_pred_nb)
print("Naive Bayes Confusion Matrix:")
print(cm_nb)

# Decision Tree Confusion Matrix'i
cm_dt = confusion_matrix(y_test, y_pred_dt)
print("Decision Tree Confusion Matrix:")
print(cm_dt)

# KNN Confusion Matrix'i
cm_knn = confusion_matrix(y_test, y_pred_knn)
print("KNN Confusion Matrix:")
print(cm_knn)
