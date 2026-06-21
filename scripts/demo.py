from urli.urli import remove_password

url = "mysql+aiomysql://user1:secret2@127.0.0.1:123/db_name"

url = remove_password(url)

print(url)