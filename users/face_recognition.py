import numpy as np
from numpy import expand_dims
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import Normalizer
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import classification_report

# 두 벡터 간 거리를 구하기 위한 알고리즘
def classification(face_embeddings, labels, n_neighbors):
  face_embeddings = normalization2(face_embeddings)
  labels = labeling(labels)

  # fit model
  # classifier = SVC(kernel='linear', probability=True)
  # classifier = MLPClassifier(solver='adam', activation='relu', random_state=1, hidden_layer_sizes=(100, ))
  classifier = KNeighborsClassifier(n_neighbors, p=1, weights='distance', metric='euclidean') #finetuning해야할 수 있음
  classifier.fit(face_embeddings, labels) # n_neighbors에 representation값이 존재하는 회원 합계를 연동

  return classifier

def normalization(face_embeddings, face_to_predict_embedding):
  # normalize input vectors
  input_encoder = Normalizer(norm='l2')
  face_embeddings = input_encoder.transform(face_embeddings)
  face_to_predict_embedding = input_encoder.transform(face_to_predict_embedding)

  return face_embeddings, face_to_predict_embedding

def normalization2(face_embeddings):
  # normalize input vectors
  input_encoder = Normalizer(norm='l2')
  face_embeddings = input_encoder.transform(face_embeddings)

  return face_embeddings

def labeling(labels):
  # label encoding targets
  output_encoder = LabelEncoder()
  output_encoder.fit(labels)
  labels = output_encoder.transform(labels)

  return labels

def predict_label(face_to_predict_embedding, face_embeddings, labels, classifier):
  # label encoding targets
  output_encoder = LabelEncoder()
  output_encoder.fit(labels)
  labels = output_encoder.transform(labels)
  #test_labels = output_encoder.transform(test_labels)

  face_embeddings, face_to_predict_embedding = normalization(face_embeddings, face_to_predict_embedding)

  face_emb = face_to_predict_embedding[0]

  # prediction for the labels
  samples = expand_dims(face_emb, axis=0)
  yhat_class = classifier.predict(samples)
  print(yhat_class)

  yhat_prob = classifier.predict_proba(samples)
  print(yhat_prob)

  class_index = yhat_class[0]
  class_probability = yhat_prob[0, class_index] * 100

  predicted_names = output_encoder.inverse_transform(yhat_class)[0]

  return predicted_names, class_probability