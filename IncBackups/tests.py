import json
import configparser

CurrentContent = """[testsftp]
type = sftp
host = example.com
user = testuser
pass = REDACTED
shell_type = unix
md5sum_command = md5sum
sha1sum_command = sha1sum

[testgdrive]
type = drive
client_id = ""
client_secret = ""
scope = drive
root_folder_id = ""
service_account_file = ""
token = {"access_token":"REDACTED_ACCESS_TOKEN","token_type":"Bearer","refresh_token":"REDACTED_REFRESH_TOKEN"}
"""

# Read the configuration string
config = configparser.ConfigParser()
config.read_string(CurrentContent)

# Get the refresh token
refresh_token = json.loads(config.get('testgdrive', 'token'))['refresh_token']
old_access_token = json.loads(config.get('testgdrive', 'token'))['access_token']
print(refresh_token)

new_token ="jdskjkvnckjdfvnjknvkvdjc"
new_string = CurrentContent.replace(str(old_access_token), new_token)

print(new_string)