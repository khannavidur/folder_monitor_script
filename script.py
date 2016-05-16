#dependencies
import os, time, sys
from mega import Mega

#folder location
path_to_watch   = "."

#login credentials
email       = 'mail_id'
password    = 'pass'

#login once
mega    = Mega({'verbose': True})
m       = mega.login(email, password)    

#current scenario in folder
before          = dict ([(f, None) for f in os.listdir (path_to_watch)])

#begin the watch - ah reminds you of Jon Snow does it?
while 1:
        #Even jon needs rest so check for changes every 10 seconds
            time.sleep (10)

                #the latest scenario in folder structure
                    after = dict ([(f, None) for f in os.listdir (path_to_watch)])

                        #added files
                            added = [f for f in after if not f in before]

                                if added:
                                            print "Added: ", ", ".join (added)
                                                    file_names = "".join(added)
                                                            file_names.split(',')
                                                                    text_to_write = "[" +os.path.relpath(".","..") + "] " + "".join (added) + " [Size] " + str(os.stat(file_name).st_size) + " - "

                                                                            #see if file fully uploaded
                                                                                    new_size        = -1
                                                                                            current_size    = os.stat(file_name).st_size

                                                                                                    while current_size!=new_size :
                                                                                                                    current_size = new_size
                                                                                                                                time.sleep(10)
                                                                                                                                            new_size = os.stat(file_name).st_size


                                                                                                                                                    try : 
                                                                                                                                                                    #uploading file 
                                                                                                                                                                                file = m.upload(file_name)

                                                                                                                                                                                            #link of uploaded file
                                                                                                                                                                                                        file_link = m.get_upload_link(file)

                                                                                                                                                                                                                    #log text
                                                                                                                                                                                                                                text_to_write +=  file_link + "\n"
                                                                                                                                                                                                                                            print text_to_write
                                                                                                                                                                                                                                                        #log file
                                                                                                                                                                                                                                                                    log_file = 'log.txt'

                                                                                                                                                                                                                                                                                #open log file
                                                                                                                                                                                                                                                                                            target = open(log_file, 'a')

                                                                                                                                                                                                                                                                                                        #write log
                                                                                                                                                                                                                                                                                                                    target.write(text_to_write)

                                                                                                                                                                                                                                                                                                                                #close log file
                                                                                                                                                                                                                                                                                                                                            target.close()
                                                                                                                                                                                                                                                                                                                                                    except :
                                                                                                                                                                                                                                                                                                                                                                    print "Empty files can't be uploaded to server"

                                                                                                                                                                                                                                                                                                                                                                        #this is the new file scenario to watch for changes
                                                                                                                                                                                                                                                                                                                                                                            before = after
