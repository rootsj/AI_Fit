from PIL import Image
from numpy import asarray

# extract a single face from a photo by a user

def extract_face(detector, filename, required_size=(160, 160)):

	# 파일에서 이미지 불러오기
	image = Image.open(filename)
	# RGB로 변환, 필요시
	image = image.convert('RGB')
	# 배열로 변환
	pixels = asarray(image)
	# 이미지에서 얼굴 감지
	results = detector.detect_faces(pixels)
	# 첫 번째 얼굴에서 경계 상자 추출
	x1, y1, width, height = results[0]['box']
	# 버그 수정
	x1, y1 = abs(x1), abs(y1)
	x2, y2 = x1 + width, y1 + height
	# 얼굴 추출
	face = pixels[y1:y2, x1:x2]
	# 모델 사이즈로 픽셀 재조정
	image = Image.fromarray(face)
	image = image.resize(required_size)
	face_array = asarray(image)
    
	return face_array