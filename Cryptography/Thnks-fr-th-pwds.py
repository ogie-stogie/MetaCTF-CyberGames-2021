import base64

if __name__ == "__main__":
    message = "TWV0YUNURntlbmNvZGluZ19pc19OMFRfdGhlX3NhbWVfYXNfZW5jcnlwdGlvbiEhfQ=="
    message = base64.b64decode(message)
    print(message)