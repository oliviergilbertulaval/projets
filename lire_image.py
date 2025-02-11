from PIL import Image
import pytesseract
import matplotlib.pyplot as plt

pytesseract.pytesseract.tesseract_cmd = r'c:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the uploaded image
image_path = 'text_example.png'
image_path = 'dave_abrege.png'

# Open the image and apply OCR
image = Image.open(image_path)

extracted_text = pytesseract.image_to_string(image, lang='fra')  # 'fra' for French language

# Output the extracted text
print(extracted_text)

plt.imshow(image)
plt.show()

#from ProGPT import Generative

#access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJzZXNzaW9uX2lkIjoicnNJWFFzeXg4bS13dDVneHpaYWVyalViSUM2cERxVWQiLCJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJwaWFub2cueXRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWV9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsicG9pZCI6Im9yZy11ejZTRUI2WkRmVUt6UDFRS2lIMjE5dmkiLCJ1c2VyX2lkIjoidXNlci1HUGQ4ZllWdDdVZGwxMk9PanU5Y0ZBUVYifSwiaXNzIjoiaHR0cHM6Ly9hdXRoMC5vcGVuYWkuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMjgwMjUzNzg5ODI0OTAyMjUwIiwiYXVkIjpbImh0dHBzOi8vYXBpLm9wZW5haS5jb20vdjEiLCJodHRwczovL29wZW5haS5vcGVuYWkuYXV0aDBhcHAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTczNzIxOTM2MCwiZXhwIjoxNzM4MDgzMzYwLCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIG1vZGVsLnJlYWQgbW9kZWwucmVxdWVzdCBvcmdhbml6YXRpb24ucmVhZCBvcmdhbml6YXRpb24ud3JpdGUgb2ZmbGluZV9hY2Nlc3MiLCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyJ9.0RN1x9cfaEpPl0urrWV4s2nMWGcc29VJnZgV65TKClIDhyth8NxbIc432qBaM0iOXEWklWfwVcvIB7LdydM3IONQ82EPFxkaz0xUxpkTxKU2lUB9Qeja4grWBVFLPhbRbDFCuF5F3vICTaYP1Uk2KnWDYiv1M0XFD6f-hIBVuaBfyxO1RyA9_5zJ-gcF3EQl98uKEyy_wjJcv10v8LSzBXebERQMXGYAM6VZPoODYbT8KqRGA1ev7hzIebYoSflQEvJ_K4h7fey-9rI6DYZs5kkQncAZIiZjZOJCSiXxcUTfQ-MNlbVms8sLKiAeGtl6etGLwos3qxneTuzBFdj_QA"

#bot = Generative(access_token)

#print(bot.prompt("who invented electricity?"))


def wien(lam):
    return 2.898E-3/lam

print(wien(480E-9))
print(wien(580E-9))