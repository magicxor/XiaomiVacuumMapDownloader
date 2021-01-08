# XiaomiVacuumMapDownloader

(check [ekorsanov01's MiCloud fork](https://github.com/ekorsanov01/micloud), [Xiaomi Cloud Map Extractor](https://github.com/PiotrMachowski/Home-Assistant-custom-components-Xiaomi-Cloud-Map-Extractor), [standalone Xiaomi Vacuum Map Viewer](https://community.openhab.org/t/xiaomi-vacuum-map-viewer-to-find-coordinates-for-zone-cleaning/103500) or [openHAB addon](https://github.com/openhab/openhab-addons/blob/3.0.x/bundles/org.openhab.binding.miio/src/test/java/org/openhab/binding/miio/internal/RoboMapViewer.java))

To download `map.rrmap` just change

```python
vacuum_ip = "YOUR_VACUUM_CLEANER_IP"
vacuum_token = "YOUR_TOKEN"
cloud_user_id = "YOUR_MI_ACCOUNT_ID"
cloud_user_password = "YOUR_MI_ACCOUNT_PASSWORD"
```

and run `python3 download.py`
