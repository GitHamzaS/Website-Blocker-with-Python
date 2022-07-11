import datetime
import time 



end_time = datetime.datetime(2022,7,12)
site_block = ["www.facebook.com","www.instagram.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect_number = "127.0.0.1"


while True: 
    if datetime.datetime.now() < end_time:
        print("start blocking")
        with open(host_path,'r+') as Temp_file:
                content = Temp_file.read()
                for adding_websites in site_block:
                    if adding_websites not in content :
                        Temp_file.write(redirect_number + " " + adding_websites + "\n")
                    else:
                        pass    
    else:
        with open(host_path,'r+') as Temp_file:
            content = Temp_file.readline()
            Temp_file.seek(0)
            for lines in content:
                if not any(adding_websites in lines for adding_websites in site_block):
                    Temp_file.write(lines)

            Temp_file.truncate()        
        time.sleep(5)
