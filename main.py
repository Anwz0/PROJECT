import requests

def Domain():
    domain = (input("Enter your domain: "))
    return domain
Domain= str(Domain())
filename="SubDomainsList.txt"
Report = {}
with open(filename, 'r') as SDlist:
    for subdomain in SDlist:
        subdomain_url = "https://"+str(subdomain).strip()+"."+Domain
        try:
            Req = requests.get(subdomain_url)
            Status="Status Code :"+str(Req.status_code)
            Report[subdomain_url]= Status
        except:
            Report[subdomain_url]= "Not Found !!"
print("\n------------"+" SUBDOMAIN REPORT FOR :"+Domain+" ------------\n")
for key,value in Report.items():
    print(key,':',value)
print("\n------------ END OF REPORT ------------\n")