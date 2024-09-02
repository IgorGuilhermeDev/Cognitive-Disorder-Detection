import os
import cv2
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

greater_equal_26_folder = "../greaterEquals26"
lesser_26_folder = "../lesser26"

def load_images_from_folder(folder):
    images = []
    labels = []
    for subdir in os.listdir(folder):
        subdir_path = os.path.join(folder, subdir)
        if os.path.isdir(subdir_path):
            image_set = []
            for file_name in os.listdir(subdir_path):
                if file_name.endswith(".png") or file_name.endswith(".jpg"):
                    img_path = os.path.join(subdir_path, file_name)
                    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                    img = cv2.resize(img, (128, 128))
                    image_set.append(img.flatten())
            if len(image_set) == 3:
                avg_image = np.mean(image_set, axis=0)
                images.append(avg_image)
                if folder == greater_equal_26_folder:
                    labels.append(1)
                else:
                    labels.append(0)
    return np.array(images), np.array(labels)

images_greater_equal_26, labels_greater_equal_26 = load_images_from_folder(greater_equal_26_folder)
images_lesser_26, labels_lesser_26 = load_images_from_folder(lesser_26_folder)

X = np.concatenate((images_greater_equal_26, images_lesser_26), axis=0)
y = np.concatenate((labels_greater_equal_26, labels_lesser_26), axis=0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

svm_model = SVC(kernel='linear', gamma='scale') 
svm_model.fit(X_train, y_train)

y_pred_svm = svm_model.predict(X_test)
print("Report:")
print(classification_report(y_test, y_pred_svm))
print("Accuracy:", accuracy_score(y_test, y_pred_svm))

directory_path = '../model_and_scaler/'
os.makedirs(directory_path, exist_ok=True)

with open(os.path.join(directory_path, 'svm_model.pkl'), 'wb') as model_file:
    pickle.dump(svm_model, model_file)

with open(os.path.join(directory_path, 'scaler.pkl'), 'wb') as scaler_file:
    pickle.dump(scaler, scaler_file)

print("Model and scaler have been saved as 'svm_model.pkl' and 'scaler.pkl'.")
