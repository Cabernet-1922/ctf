# john_pollard [Medium] (by Samuel S) - picoCTF 2019
> Sometimes RSA <a href='//jupiter.challenges.picoctf.org/static/c882787a19ed5d627eea50f318d87ac5/cert'>certificates</a> are breakable

```python
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from base64 import b64decode

pem_cert = """-----BEGIN CERTIFICATE-----
MIIB6zCB1AICMDkwDQYJKoZIhvcNAQECBQAwEjEQMA4GA1UEAxMHUGljb0NURjAe
Fw0xOTA3MDgwNzIxMThaFw0xOTA2MjYxNzM0MzhaMGcxEDAOBgNVBAsTB1BpY29D
VEYxEDAOBgNVBAoTB1BpY29DVEYxEDAOBgNVBAcTB1BpY29DVEYxEDAOBgNVBAgT
B1BpY29DVEYxCzAJBgNVBAYTAlVTMRAwDgYDVQQDEwdQaWNvQ1RGMCIwDQYJKoZI
hvcNAQEBBQADEQAwDgIHEaTUUhKxfwIDAQABMA0GCSqGSIb3DQEBAgUAA4IBAQAH
al1hMsGeBb3rd/Oq+7uDguueopOvDC864hrpdGubgtjv/hrIsph7FtxM2B4rkkyA
eIV708y31HIplCLruxFdspqvfGvLsCynkYfsY70i6I/dOA6l4Qq/NdmkPDx7edqO
T/zK4jhnRafebqJucXFH8Ak+G6ASNRWhKfFZJTWj5CoyTMIutLU9lDiTXng3rDU1
BhXg04ei1jvAf0UrtpeOA6jUyeCLaKDFRbrOm35xI79r28yO8ng1UAzTRclvkORt
b8LMxw7e+vdIntBGqf7T25PLn/MycGPPvNXyIsTzvvY/MXXJHnAqpI5DlqwzbRHz
q16/S1WLvzg4PsElmv1f
-----END CERTIFICATE-----"""

cert_data = pem_cert.replace('-----BEGIN CERTIFICATE-----', '')
cert_data = cert_data.replace('-----END CERTIFICATE-----', '')
cert_data = cert_data.replace('\n', '')


cert_bytes = b64decode(cert_data)
cert = x509.load_der_x509_certificate(cert_bytes, default_backend())
public_key = cert.public_key()


from factordb.factordb import FactorDB
f = FactorDB(public_key.public_numbers().n)
f.connect()
factor = f.get_factor_list()
print("picoCTF{"+str(factor[1])+","+str(factor[0])+"}")
```

flag: `picoCTF{73176001,67867967}`