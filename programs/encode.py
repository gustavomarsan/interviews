# pip install PyJWT
import jwt

secret = "My_secret_key"

payload = {
    "user_id": 123,
    "username": "test_usesr",
    "role": "admin",
}
# Encode the payload to create a JWT
token = jwt.encode(payload, secret, algorithm="HS256")
print("Encoded JWT:", token)

#decode the JWT to retrieve the payload
decoded_payload = jwt.decode(token, secret, algorithms=["HS256"])
print("Decoded Payload:", decoded_payload)
