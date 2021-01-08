import miio
from micloud import MiCloud
import time

vacuum_ip = "YOUR_VACUUM_CLEANER_IP"
vacuum_token = "YOUR_TOKEN"
cloud_user_id = "YOUR_MI_ACCOUNT_ID"
cloud_user_password = "YOUR_MI_ACCOUNT_PASSWORD"

map_link = "retry"
if not (vacuum_ip == "" or vacuum_token == ""):
    vacuum = miio.Vacuum(vacuum_ip, vacuum_token)
    counter = 10
    while map_link == "retry" and counter > 0:
        print("Invalid map: " + map_link)
        time.sleep(0.2)
        map_link = vacuum.map()[0]
        counter = counter - 1

if map_link == "retry":
    raise ValueError('Can not obtain the map link')

print("Retrieved map: " + map_link)

mc = MiCloud(cloud_user_id, cloud_user_password)
mc.login()
cloud_token = mc.get_token()
device_list = mc.get_devices()
mc.download_vacuum_map(country="ru", map_id=map_link)
