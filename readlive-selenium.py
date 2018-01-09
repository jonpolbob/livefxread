from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import http.client


#lecture d'une page fxdata mise a jour
# et detection de paires qui changent

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
     "(KHTML, like Gecko) Chrome/15.0.87"
    )
dcap["phantomjs.page.settings.javascriptEnabled"] = True


driver = webdriver.PhantomJS( service_args=[
  '--ignore-ssl-errors=true'], desired_capabilities=dcap)

message = "plouf"
driver.maximize_window()
count=10
while count !=0 :
   count = count-1
   try:
       driver.get ("http://www.fxstreet.fr/rates/forex-rates")
   	

   except http.client.BadStatusLine:
       print ('echec')

   print (driver.title,'!!')

#driver.close()
driver.quit()