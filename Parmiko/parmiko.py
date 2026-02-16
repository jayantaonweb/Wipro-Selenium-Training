import paramiko

host = "localhost"
port = 22
username = "Jayant Pandey"
password = "admin"

# create an object and connect to remote machines
client = paramiko.SSHClient()

# set the rules to handel unknown host keys, or the first time connecting host key
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname=host,
    port=port,
    username=username,
    password=password
)

stdin, stdout, stderr = client.exec_command("whoami")
print(stdout.read().decode())

client.close()