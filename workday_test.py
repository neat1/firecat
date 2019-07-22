import requests
import workday

apis = {
'talent': 'https://workday.com/tenant/434$sd.xml',
'hcm': 'https://workday.com/tenant/hcm$sd.xml'
}
client = workday.WorkdayClient(
wsdls=apis,
authentication=...
)

users = client.hcm.Get_Users()
print(workday.client)
