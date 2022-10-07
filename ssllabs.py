import rpa as r
import os
import time

startTime = time.time()
basedir = os.path.abspath(os.path.dirname(__file__))

r.init(True, True)
# Change wait timout default to 2 seconds
r.timeout(2)


# Check a list of domains
domains = ["google.com", "login.saipem.com", "techviewleo.com", "ask.com", "enable.adaptivecloud.com", "ulanov.store"]

resultlist = []
for domain in domains:
    domain_ent = domain + '[enter]'

    r.url('https://www.ssllabs.com/ssltest/')
    r.wait(0.5)
    r.type('//*[@name="d"]', domain_ent)

    print(f"Checking: {domain}")
    # Look for summary
    summary = r.read('//*[@id="main"]/div[5]/div[1]/div[1]')
    multiTable = False

    while not summary:
        # Check for refresh for ongoing scan
        # Check for a multiTable with elif
        if r.read('//*[@id="refreshUrl"]'):
            print("Scanning in progress")
        elif r.read('//*[@id="multiTable"]'):
            multiTable = True
            print("Multi Table Found")
            break
        
        print("Checking for summary again, waiting 10 seconds")
        r.wait(10)
        summary = r.read('//*[@id="main"]/div[5]/div[1]/div[1]')

    if multiTable:
        r.click('//*[@id="multiTable"]/tbody/tr[3]/td[2]/span[1]/b/a')


    # Do something to get the summary
    result = r.read('//*[@id="rating"]')
    fixed = " ".join(result.split())
    resultdict = {"Domain":domain,
                "Result":fixed
                } 
    resultlist.append(resultdict)

    print(fixed)
    print("Moving on to next domain\n\n")

r.close()

for domain in resultlist:
    print(domain)

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))
