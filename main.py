import discord
import os
import time
from keep_alive import keep_alive
from discord.ext import commands, tasks
# # from datetime.datetime import time
# from datetime import datetime
# from datetime import date
# # from datetime.datetime import timedelta
# import asyncio
# from my_timer import start_timer
# import my_scheduler as schd

client = discord.Client()


@client.event
async def on_ready():
  print('We are logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="people's queries"))

@client.event

async def on_message(message):

  #ignores the following channels

  if message.channel.id == 968901761463091232: #imp announcements in precourse
    return
  if message.channel.id == 968901761463091233: #session links in precourse
    return
  if message.channel.id == 809337381407948812: #announcements in main
    return
  if message.channel.id == 968901761018503225: #event announ precourse
    return
  if message.channel.id == 968901761463091234: #recordings precourse
    return
  if message.channel.id == 968901761463091235: #notes precourse
    return

  #Questions and answers upon $help
  
  async def adminquery():
    await message.channel.send("Congratulations you have reached Admin query portal. Here are a list of FAQs that might be similar to your question:\n")

  #questions
    await message.channel.send("*$1a* Am I eligible to join AccioJob \n*$1b* What's the minimum educational qualification to join the course? \n*$1c* When will I get joining details of my Batch?"
    )
    
  async def coursequery():
    await message.channel.send("Congratulations you have reached Course query portal. Here are a list of FAQs that might be similar to your question:\n")
    await message.channel.send("*$2a* What is the duration of the course? \n*$2b* When is the next batch starting? \n*$2c* What is the ISA (Terms and conditions agreement)? \n*$2d* Can I solve module questions and coding test in x language? \n*$2e* Is thereew rounds? \n*$2f* Does previous academic performance, field of study or gap years matter? \n*$2g* How many hours do we need to put in during the course?")

  async def interview_query():
    await message.channel.send("Congratulations you have reached Course query portal. Here are a list of FAQs that might be similar to your question:\n")
    await message.channel.send("*$3a* What questions are asked in the interview/what is the interview procedure? \n*$3b* I have scheduled my interview. When can I expect a call?")
    
  if message.author == client.user:
    return
  
  #answers
    
  if "$help" in message.content:
    await message.channel.send("How can I help you?\n*$1* - Admin query\n*$2* - course query\n*$3* - Interview based query\n*$4* - Coding Query" )
    
  if "$1"==message.content:
    await adminquery()
    
  if "$1a"==message.content:
    await message.channel.send("> You need to be a 2023 graduate or earlier to apply for AccioJob. You will be eligible for Pay after placement offer if you are a graduate between 2018 and 2023. You will be applicable for payupfront option if you are 2017 graduate or earlier.")

  if "$1b"==message.content:
    await message.channel.send("> You need to be a 2023 graduate or earlier to be eligible to join the course.")
    
  if "$1c"==message.content:
    await message.channel.send("> You will receive the joining details of your batch one day before your batch starts.")

  if "$2"==message.content:
    await coursequery()

  if "$2a"==message.content:
    await message.channel.send("> The course duration is 6 months.")

  if "$2b"==message.content:
    await message.channel.send("> The next batch is starting on April 25th.")

  if "$2c"==message.content:
    await message.channel.send("> Terms and conditions are straight forward. We have a 12 month agreement with the student. Training goes on for the first 6 months. Placements start from the 3rd month onwards and goes on till the 12th month. The student starts paying only after they get placed above 5 LPA during these 12 months.")

  if "$2d"==message.content:
    await message.channel.send("> You can use any language to solve the modules and further in the interview also but the course we have is in Java so you would have to work your skills in Java once you get selected.")

  if "$2e"==message.content:
    await message.channel.send("> You can pay the fee upfront if you don't want to clear the tests.")

  if "$2f"==message.content:
    await message.channel.send("> No, none of the above matter for course joining or even for placements. Companies coming for placement only look for your coding skills, which we, here a AccioJob teach you.")

  if "$2g"==message.content:
    await message.channel.send("> The live classes are from 8pm to 11pm on weekdays. And apart from that you need to put 2-3 hours of self-study time to solve the assignments. There will be soft-skills training, profile building, contests and reviews on the weekends.")
    
  if "$3"== message.content:
    await interview_query()
    
  if "$3a"==message.content:
    await message.channel.send("> Once you pass the coding test, you will be able to book an interview. A person from Acciojob will contact you and schedule your interview. During the interview: \n> 1. There will be some questions regarding your previous experience and some to judge your dedication and consistency. \n> 2. Then it will be followed by a coding round in which we will test your coding skills. \n\n> (Note: if you have watched our videos and completed all the questions in the modules, then you won't be facing any issues in the coding round.) \n\n> And once you pass the interview, you will be placed in the next Main Batch!")

  if "$3b"==message.content:
    await message.channel.send("> You will receive a call from our team within 48 hours. You can ping Team AccioJob here if you don't receive a call even then.")

  if "$4"==message.content:
    await message.channel.send("Your question will be solved shortly by a human!")

  #keyword trigger based response

  msg_text = message.content.strip().lower()

  # keyword_1 = ['interview', 'when']
  # keyword_1a = ['interview', 'what', 'time']
  keyword_2 = ['coding', 'test', 'times']
  keyword_2a = ['coding', 'test', 'fail']
  keyword_3 = ['eligible', 'join']
  keyword_4 = ['minimum', 'join', 'qualification']
  keyword_5 = ['when', 'joining', 'batch']
  keyword_6 = ['duration', 'course']
  keyword_7 = ['batch', 'next', 'starting']
  keyword_8 = ['what', 'isa']
  keyword_9 = ['solve', 'language']
  keyword_10 = ['join', 'without', 'clearing']
  keyword_11 = ['grade', 'gap', 'grades', 'mechanical', 'electrical', 'civil', 'distance', 'bcom', 'bba']
  keyword_12 = ['placed', 'other', 'pay']
  keyword_13 = ['what', 'timings']
  keyword_14 = ['given', 'interview', 'result']
  keyword_15 = ['commit', 'hours']
  keyword_16 = ['registration', 'fees']
  keyword_17 = ['practice', 'coding test']
  keyword_18 = ['coding test', 'difficult']
  keyword_19 = ['13th May']
  keyword_20 = ['projects']
  keyword_21 = ['educators', 'instructors']
  keyword_22 = ['curriculum']
  keyword_23 = ['how', 'many', 'questions', 'coding test']
  keyword_24 = ['webcam']
  keyword_25 = ['list', 'hiring']
  keyword_26 = ['notes']
  keyword_27 = ['recordings']
  keyword_28 = ['invite']
  keyword_29 = ['interview', 'questions']
  keyword_30 = ['register', 'marathon']
  keyword_31 = ['timings', 'weekend']
  keyword_32 = ['precourse', 'next']
  keyword_33 = ['batch manager', 'dont','didnt']
  keyword_34 = [ 'Help-bot']
  keyword_35 = ['How-bot']
  keyword_36 = ['Detail-bot']
  keyword_37 = ['hard-refresh-bot']
  keyword_38 = ['Assignment-doubts-bot']
  keyword_39 = ['DM-bot']
  keyword_40 = ['class-link-bot']
  keyword_41 = ['Details-bot']
  keyword_42 = ['Syllabus-bot']
  keyword_43 = ['Interviewer-missing-bot']
  keyword_44 = ['Cant-book-interview-bot']
  keyword_45 = ['Open-Doubt-Session-bot']
  keyword_46 = ['timing-bot']
  keyword_47 = ['Assignment-doubts-channel-bot']
  
  
  #if all(word in msg_text for word in keyword_1):
    #await message.channel.send("> Your will receive a call within 48 hours of booking your interview on the website. If you have not, then you can then ping the staff here!")
  #if all(word in msg_text for word in keyword_1a):
    #await message.channel.send("> Your will receive a call within 48 hours of booking your interview on the website. If you have not, then you can then ping the staff here!")
  if all(word in msg_text for word in keyword_2):
    await message.channel.send("> Do not worry if you fail the coding test. You will be able to give the coding test a maximum of 2 times during September 7 to 12.")
    if all(word in msg_text for word in keyword_2a):
      await message.channel.send("> Do not worry if you fail the coding test. You will be able to give the coding test a maximum of 2 times during May 13th to 17th.")
  if all(word in msg_text for word in keyword_3):
    await message.channel.send("> You need to be a 2023 graduate or earlier to apply for AccioJob. You will be eligible for Pay after placement offer if you are a graduate between 2018 and 2023. You will be applicable for payupfront option if you are 2017 graduate or earlier.")
  if all(word in msg_text for word in keyword_4):
    await message.channel.send("> You need to be a 2023 graduate or earlier to be eligible to join the course.")
  if all(word in msg_text for word in keyword_5):
    await message.channel.send("> You will receive the joining details of your batch one day before your batch starts.")
  if all(word in msg_text for word in keyword_6):
    await message.channel.send("> The course duration is 6 months.")
  if all(word in msg_text for word in keyword_7):
    await message.channel.send("> The next batch will start from 3 September")
  if all(word in msg_text for word in keyword_8):
    await message.channel.send("> Terms and conditions are straight forward. We have a 12 month agreement with the student. Training goes on for the first 6 months. Placements start from the 3rd month onwards and goes on till the 12th month. The student starts paying only after they get placed above 5 LPA during these 12 months.")
  if all(word in msg_text for word in keyword_9):
    await message.channel.send("> You can use any language to solve the modules and further in the interview also but the course we have is in Java so you would have to work your skills in Java once you get selected.")
  if all(word in msg_text for word in keyword_10):
    await message.channel.send("> You can pay the fee upfront if you don't want to clear the tests.")
  if any(word in msg_text for word in keyword_11):
    await message.channel.send("> It will not matter for course joining or even for placements. Companies coming for placement only look for your coding skills, which we, here at AccioJob teach you!")
  if all(word in msg_text for word in keyword_12):
    await message.channel.send("> Once you start the course with us and sign the ISA, you will have to pay us the course fee when you get placed in IT sector above 5 LPA. If you get placed in a non-IT company or below 5 LPA and you want to quit the Main Batch then you will have to pay the course fee.")
  if all(word in msg_text for word in keyword_13):
    await message.channel.send("> The timings for live classes are from 8 PM to 11 PM on weekdays. You will have to put in 2-3 hours of extra effort to get your assignment and learning done everyday. And we have soft skills practice sessions, contests and profile building on weekends.")
  if all(word in msg_text for word in keyword_14):
    await message.channel.send("> Please check your spam folder for the email. If you have still not received the email then you can ping a staff member here with your email ID.")
  if all(word in msg_text for word in keyword_15):
    await message.channel.send("> You will need to spend at least 5-6 hours per day throughout the duration of the course.")
  if all(word in msg_text for word in keyword_16):
    await message.channel.send("The fee structure for the Pay Upfront option is as follows: \n> - INR 6,999 registration fees payable now + INR + GST payable after 7 day trial \n> - 100% refund of registration fees if not satisfied after the 7-day trial.")
  if all(word in msg_text for word in keyword_17):
    await message.channel.send("> If you have completed all the modules thoroughly and written programs on your own then you will be able to clear the coding test fairly well! If you want more practice questions then you can refer to this link https://expensive-amount-815.notion.site/Further-Practice-Questions-AccioJob-Modules-93a32105a2d8496fb35149e7ef9216f8 and you can even practice more on Hackerrank/Leetcode.")
  if all(word in msg_text for word in keyword_18):
    await message.channel.send("> If you have solved all module questions thoroughly and practiced some more questions on your own then you should be able to clear the coding test! If you want more practice questions then you can refer to this link https://expensive-amount-815.notion.site/Further-Practice-Questions-AccioJob-Modules-93a32105a2d8496fb35149e7ef9216f8 and you can even practice more on Hackerrank/Leetcode.")
  if all(word in msg_text for word in keyword_19):
    await message.channel.send("> You will be able to schedule your interview after coding test for the  Main Batch. \n> Till then you can practice some coding by yourself from this website https://expensive-amount-815.notion.site/Further-Practice-Questions-AccioJob-Modules-93a32105a2d8496fb35149e7ef9216f8 and you can even practice more on Hackerrank/Leetcode.")
  if all(word in msg_text for word in keyword_20):
    await message.channel.send("> There will be a variety of projects! you'll be working on atleast 2 projects on DSA and a lot of projects on front-end, you'll have a repository of projects you can choose to work on post selection in the main batch.")
  if any(word in msg_text for word in keyword_21):
    await message.channel.send("> You will have 2 instructors one for main class and the other for doubt class!")
  if all(word in msg_text for word in keyword_22):
    await message.channel.send("> The course curriculum is: \n> First 2 months we teach you DSA in Java, OOPS, SQL, System Design \n> Next 2 month we teach you front end webdev - HTML, CSS, Javascript, ReactJS and Redux \n> The last 2 months we teach you back end webdev - NodeJS, Express and MongoDB. \n> This covers the DSA and Full stack development!")
  if all(word in msg_text for word in keyword_23):
    await message.channel.send("> There will be 2 questions in the coding test to be solved within an hour. \n> You need to clear 50% i.e., all test cases of at least 1 question at least or half test cases of both the questions.")
  if all(word in msg_text for word in keyword_24):
    await message.channel.send("> You will need a webcam for the coding test and the interview.")
  if all(word in msg_text for word in keyword_25):
    await message.channel.send("> We have more 200 hiring partners, most of these are product based, we also have some service based companies that hire from us. You can find a sample list of hiring partners on our website. \n> Some partners are- Thoughworks, Gainsight, Visa, Converj, Paytm, Maersk, Tata Digital, Makemytrip, salesforce, etc.")
  if all(word in msg_text for word in keyword_26):
    await message.channel.send("> Notes will be made available in <#977500137473585153>")
  if all(word in msg_text for word in keyword_27):
    await message.channel.send("> Recordings will be made available in <#977500100597272596>")
  if all(word in msg_text for word in keyword_28):
    await message.channel.send("> The server invite link is: https://discord.gg/pbJTaxScuJ")
  if all(word in msg_text for word in keyword_29):
    await message.channel.send("> Once you pass the coding test, you will be able to book an interview. A person from Acciojob will contact you and schedule your interview. During the interview: \n> 1. There will be some questions regarding your previous experience and some to judge your dedication and consistency. \n> 2. Then it will be followed by a coding round in which we will test your coding skills. \n\n> (Note: if you have watched our videos and completed all the questions in the modules, then you won't be facing any issues in the coding round.) \n\n> And once you pass the interview, you will be placed in the next Main Batch!")
  if all(word in msg_text for word in keyword_30):
    await message.channel.send("> There is no registration as such. \nYou can just solve the coding questions given the day before in <#958972904345837598> and clear any doubts you have when the mentor shows how to solve the problem.")
    if all(word in msg_text for word in keyword_31):
      await message.channel.send("> There are no classes on weekends. We usually have weekly coding contests, profile building and soft skills sessions on weekends.")

    if all(word in msg_text for word in keyword_32):
      await message.channel.send("> The next AccioJob Precourse is starting from September 3.")
      if all(word in msg_text for word in keyword_33):
        await message.channel.send("> Your batch manager will contact you first after that you can contact him.")
        
    if all(word in msg_text for word in keyword_34):
       await message.channel.send("> Is there anything else I can help you with?")
    if all(word in msg_text for word in keyword_35):
      await message.channel.send("> Hi there, how can I help you?")
      
    if all(word in msg_text for word in keyword_36):
      await message.channel.send("> Please DM us your age and the year you graduated. These details will help us to assist you further.")
      if all(word in msg_text for word in keyword_37):
        await message.channel.send("> Please hard refresh your page using *Ctrl* and *Shift* and then press *R* on your keyboard.This would help you with your concern. In case, you are still unable to resolve the issue, please get back to us here again")
      if all(word in msg_text for word in keyword_38):
        await message.channel.send("> You can refer to our channel #assignment-doubts for code relate queries. Our tech buddy will assist you there.")
      if all(word in msg_text for word in keyword_39):
        await message.channel.send("< We have sent you a DM in this regard. Please check.")

        if all(word in msg_text for word in keyword_40):
          await message.channel.send("> Hey there!The FREE LIVE class starts at 8 pm Click here to join: http://precourse.acciojob.com/join-live-class ")

      if all(word in msg_text for word in keyword_41):
        await message.channel.send("> We offer an online placement guaranteed full stack web development course, after which we help the students in getting placed upto 41lpa. The program is divided into 3 sections, DSA, Frontend and Backend, all these 3 sections will be covered in Java and JavaScript.")

        if all(word in msg_text for word in keyword_42):
          await message.channel.send("> Please check your DM. We have shared the course Syllabus there. ")

        if all(word in msg_text for word in keyword_43):
          await message.channel.send("> Please don't worry. You shall be contacted within 24 hours regarding the same. ")

        if all(word in msg_text for word in keyword_44):
          await message.channel.send("> Please join our open doubt session between 6PM to 8PM to clear your doubts and queries related to our program.")
      if all(word in msg_text for word in keyword_45):
        await message.channel.send("> Classes will be Monday - Friday (8pm - 11pm) live ")

      if all(word in msg_text for word in keyword_46):
        await message.channel.send("> Hello everyone! Keep sharing all your Coding Doubts here! Our Tech Team will soon be resolving and responding to all your queries.")
      
      

# bot = commands.Bot(
# command_prefix="!",  # Change to desired prefix
# case_insensitive=True,  # Commands aren't case-sensitive
# help_command=help_command)


# @tasks.loop(seconds=60)  #Check for schedule every minute.
# async def background_checker():
#     print("Checking now (" + schd.get_now(with_second=True) + ").")
#     commands, channels = schd.get_sent_now()
#     if len(commands) > 0:
#         for i in range(len(commands)):
#             channel_conn = bot.get_channel(int(channels[i]))
#             await channel_conn.send(commands[i])
          
# announcement_channel_id = 943214038077292574
# bot = commands.Bot(command_prefix="$")
# WHEN = time(18, 0, 0)  # 6:00 PM
# channel_id = 943214038077292574

# async def called_once_a_day():  # Fired every day
#     await bot.wait_until_ready()  
#     channel = bot.get_channel(channel_id) 
#     await channel.send("your message here")

# async def background_task():
#     now = datetime.now()
    
#     if now.time() > WHEN:  
#         tomorrow = datetime.combine(now.time() + timedelta(hours=6), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)  # Sleep until tomorrow and then the loop will start 
    
#     while True:
#         now = datetime.now() 

#         target_time = datetime.combine(now.date(), WHEN)  # 6:00 PM today (In UTC)
        
#         seconds_until_target = (target_time - now).total_seconds()
        
#         await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
        
#         await called_once_a_day()  # Call the helper function that sends the message
        
#         tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))

#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
        
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration


# if _name_ == "_main_":
#     bot.loop.create_task(background_task())
  
keep_alive()
client.run(os.getenv('token'))