from numpy import expand_dims
from numpy import asarray

# FaceNet을 이용하여 한 이미지 마다 embedding(128D 벡터)를 계산하는 함수
def get_embedding(model, face_pixels):
  # scale pixel values
  face_pixels = face_pixels.astype('float32')
  # standardize pixel values across channels (global)
  mean, std = face_pixels.mean(), face_pixels.std()
  face_pixels = (face_pixels - mean) / std

  # transform face into one sample
  samples = expand_dims(face_pixels, axis=0)
  # make prediction to get embedding
  yhat = model.predict(samples)
  yhat = yhat.reshape(1, -1) # (,128)형태인 벡터로 모양을 바꿈

  return yhat