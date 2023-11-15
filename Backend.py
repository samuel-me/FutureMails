import time, datetime, ezgmail

"""just run it, you would get !!!!!!
also change the date to the current time"""

wait_time = 20
ct = 13

# this helps to prevent any type of escape sequence error
## so \n\r and \r dies the same thing
dic = {'\n': 'n1e2w3l4i7n8e', '\r': 'r2r4t6u8rn', '\t': 't4a5b7', '\"': 's9l5a6s3h', "\'": 's6l7aesh2',
       '\\': 't4h5r6e6es6l7a8sh', '\a': 'i6d3o4nt34kn5ow', '\b': 'm6ay7b4e', '\f': 'f4in3a90l'}
html_dic ={'\n':'<br>','\r':'<br>','\t':'&emsp;'} # for the html plane textsee line:

time_list = []

# incase if the server restarts the code
#ezgmail.send('dailoayomide@gmail.com', 'Mission report', 'i am still here ')


def send_mail():
    # TODO: pre error correction, i need to make this current function a finite loop.
    start_time = time.time()
    # mail = True
    print('the function send mail starts now ')
    while True:
        try:
            time_list.sort()
            print('time list after sorting it:')
            print(time_list)
            # this gets the subject and the message
            mail_time = time_list[0][0]
            # mail_time = datetime.datetime.strptime(send_time, '%Y-%m-%d')
            message = time_list[0][2]
            message_2 = message

            for i in dic:
                message_2 = message_2.replace(dic[i], i)  # it de encrypts the message

            #  allows me to use html formatting (intead of plane text)
            for i in html_dic:
                message_2 = message_2.replace(i,html_dic[i])

            sender_add = time_list[0][1]

            # this handles time,checks if the date is in the past or future
            time_diff = mail_time - datetime.datetime.now()

            end_time = time.time()  # this ensues that the code doesnt have multiple threads
            duration = end_time - start_time  # so it breaks after 13 seconds
            print('duration: ', time_diff.total_seconds())
            if (time_diff.total_seconds() > ct) or (duration > ct):
                print('a break')
                break

            else:
                # modified it to not use plane text so we wouldnt see any broken lines ## next time code goes down
                ezgmail.send(sender_add, 'Letter From Your Past', message_2.replace('<br><br>','<br>'),mimeSubtype='html')
                time.sleep(3)#  cancles double line
                print('i sent a message: ', message_2, ' \n to: ', sender_add)
                time_list.remove(time_list[0])  # remove the past time
                for i in time_list:
                    print('this is what is left of the list:')
                    print(i, '\n')

        except Exception as exc:
            ezgmail.send('dailoayomide@gmail.com',  'Disappointed?, a gift',exc, ['message.txt'])
            # ezgmail.send('dailoayomide@gmail.com', 'Ohayo!!!', 'Disappointed?, a gift', ['message.txt'])

    newest = open('message.txt', 'w',errors='ignore')  # i re - wrote the remainning messages , since it isnt their time yet
    yat = "',@'"
    for i in time_list:
        data = str(i[0]) + yat + i[1] + yat + i[2]  # so it csn be reusable
        print(data)
        newest.write(data + '\n')
    newest.close()

    ezgmail.send('futuremails3@gmail.com', 'Ohayo!!!', 'keep this , i would need it soon ', ['message.txt'])
    print('i just sent the file to myself')

    time_list.clear()
    print(time_list, 'this is the list(empty)')
    print('i re-wrote the .txt file and cleared the list')


def check_mail():
    """
    a function that checks my email for new emails sent from a particular email
    turn it into a tuple ,writes them as text and appends them in a list
    """

    y = []

    while True:
        unread_sms = ezgmail.unread()

        if len(unread_sms) > 0:  # checks for new emails
            for i in range(len(unread_sms)):
                if unread_sms[i].messages[0].sender == 'futuremails3@gmail.com':
                    the_file = unread_sms[i].messages[0].attachments
                    print('i am about to download')
                    unread_sms[i].messages[0].downloadAttachment(the_file[0])
                    #print(the_file[0])
                    print('i just downloaded the file ')

            for i in range(len(unread_sms)):
                if unread_sms[i].messages[0].sender == 'future2mails@gmail.com':  # the specific email
                    mail_2 = unread_sms[i].messages[0].subject  # the subject in the form (datetime,email address)
                    body = unread_sms[i].messages[0].body  # the message it self

                    #  #   # a line that fetches the 'message.txt' from the server and sends it to me
                    #   this allows me to monitor it
                    if 'message1.txt' in body:
                        ezgmail.send('dailoayomide@gmail.com', 'you asked for this !!!', ' a gift', ['message.txt'])

                    body_2 = body
                    #  removing all formatting errors
                    #  i should explain this part in a vn
                    for i in dic:
                        body_2 = body_2.replace(i, dic[i])
                        print('this is the message i got',body_2)

                    file = open('message.txt', 'a',encoding="utf-8",errors='ignore') # utf(t allow emojis)
                    # print(repr(unread_sms[i].messages[0].body))  # so i can se the \n\r and the rest
                    file.write(
                        mail_2 + "',@'" + body_2 + '\n')  # i did it like this so if the server restarts my code, it continues from where it stopped
                    file.close()

            ezgmail.markAsRead(unread_sms)  # marks the emails as read
            ##
        new_file = open('message.txt',encoding="utf-8",errors='ignore')
        for codes in new_file:
            # i want to remove the new lines '\n'
            if codes != '\n':

                y.append(codes)

        for i in y:  # did this because of the unexplainable new lines

            timer, sender_add, mms = i.split("',@'")  # ',@'

            timer = timer.replace(' 00:00:00', '')  # you get an error if you dont do it like this
            send_time = datetime.datetime.strptime(timer, '%Y-%m-%d')
            if '@gmail.com' in sender_add.lower():
                tools = (send_time, sender_add, mms.replace('\n', ''))
                #print(tools,"\nayomide")

                if tools not in time_list:
                    time_list.append(tools)
                print(time_list)

        y.clear()
        time.sleep(2)
        send_mail()
        print('i would continue in 6 hours')
        time.sleep(21600)  # wait for  6 hours


check_mail()
# threadObj = threading.Thread(target=check_mail)
# threadObj.start()

""" this code has a big bug, it duplicates the list at a certain point 
its like there are 2 SEND_MAIL functions running at the same time.
( it creates multiple threads of the same function) 
it skips the next ,clears the double list and continues
i think its because of the multiple threads 
also , an error code(index out of range),thats not meant to happen there was 2021 in the list """

# https://www.youtube.com/watch?v=wgPh3mSYf0M&pbjreload=101
