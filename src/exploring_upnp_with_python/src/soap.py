import urllib2

soap_encoding = "http://schemas.xmlsoap.org/soap/encoding/"
soap_env = "http://schemas.xmlsoap.org/soap/envelope"
service_ns = "urn:schemas-upnp-org:service:WANIPConnection:1"
soap_body = """<?xml version="1.0"?>
<soap-env:envelope soap-env:encodingstyle="%s" xmlns:soap-env="%s">
  <soap-env:body>
    <m:getexternalipaddress xmlns:m="%s">
    </m:getexternalipaddress>
   </soap-env:body>
</soap-env:envelope>""" % (soap_encoding, service_ns, soap_env)

soap_action = "urn:schemas-upnp-org:service:WANIPConnection:1#GetExternalIPAddress"
headers = {
    'SOAPAction': u'"%s"' % (soap_action),
    'Host': u'192.168.0.1:40833',
    'Content-Type': 'text/xml',
    'Content-Length': len(soap_body),
}

ctrl_url = "http://192.168.0.1:40833/ctl/IPConn"

request = urllib2.Request(ctrl_url, soap_body, headers)
response = urllib2.urlopen(request)

print response.read()
