
from Cheetah.Template import Template
def saveZone(fqdn, ns1, ns2, email, serial, zoneList):
	template = "/var/opt/pypanel/templates/bind/zone_file.tmpl"
	domain = {"fqdn": "madisonk.org", "ns1": "ns.madisonk.org", "ns2": "ns2.madisonk.org", "email": "madison.madisonk.org", "serial": "2011091901"}
	records = [{"host": "madisonk.org", "type": "A", "ttl": "1440"}]
	return Template(file = template, searchList = ({"domain": domain, "records": records}),)

