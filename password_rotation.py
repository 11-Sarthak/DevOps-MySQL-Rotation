import secrets
import subprocess
import string 

def generate_password(lenght=16):
    current_password=input("enter the current database password: ")
    char=string.ascii_letters+string.digits+string.punctuation
    return "".join(secrets.choice(char)for _ in range(lenght))

mysql_user = input("Enter MySQL username: ")
mysql_host = input("Enter MySQL host : ") 
mysql_password = input("Enter MySQL root password: ")

new_password=generate_password()


mysql_command=f'mysql -h {mysql_host} -u root -p"{mysql_password}" -e "ALTER USER \'{mysql_user}\'@\'localhost\' IDENTIFIED BY \'{new_password}\';"'
subprocess.run(mysql_command,shell=True,check=True)

file_path="C:/Users/sarth/Downloads/password rotation/mysql_secret-password.txt"
with open (file_path,'w') as fp: 
    fp.write(new_password)
   
print(f"New MYsql password stored in: {file_path}")
