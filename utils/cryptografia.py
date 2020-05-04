import bcrypt

senha =b"Minha Senha"

hash =bcrypt.hashpw(senha,bcrypt.gensalt())

print(hash)
