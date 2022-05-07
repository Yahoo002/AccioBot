import discord
import os
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
  print('We are logged in as {0.user}'.format(client))


@client.event

async def on_message(message):

  #ignores the following channels

  if message.channel.id == 968901761463091232: #imp announcements in precourse
    return
  if message.channel.id == 968901761463091233: #session links in precourse
    return
  if message.channel.id == 809337381407948812: #announcements in main
    return

  #Questions and answers upon $help
  
  async def adminquery():
    await message.channel.send("Congratulations you have reached Admin query portal. Here are a list of FAQs that might be similar to your question:\n")

  #questions
    await message.channel.send("*$1a* Am I eligible to join AccioJob \n*$1b* What's the minimum educational qualification to join the course? \n*$1c* When will I get joining details of my Batch?"
    )
    
  async def coursequery():
    await message.channel.send("Congratulations you have reached Course query portal. Here are a list of FAQs that might be similar to your question:\n")
    await message.channel.send("*$2a* What is the duration of the course? \n*$2b* When is the next batch starting? \n*$2c* What is the ISA (Terms and conditions agreement)? \n*$2d* Can I solve module questions and coding test in x language? \n*$2e* Is there any way to join the Main Batch without clearing the Aptitude, coding and interview rounds? \n*$2f* Does previous academic performance, field of study or gap years matter? \n*$2g* How many hours do we need to put in during the course?")

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
    
  if "$3"==message.content:
    await interview_query()
    
  if "$3a"==message.content:
    await message.channel.send("> Once you pass the coding test, you will be able to book an interview. A person from Acciojob will contact you and schedule your interview. During the interview: \n> 1. There will be some questions regarding your previous experience and some to judge your dedication and consistency. \n> 2. Then it will be followed by a coding round in which we will test your coding skills. \n\n> (Note: if you have watched our videos and completed all the questions in the modules, then you won't be facing any issues in the coding round.) \n\n> And once you pass the interview, you will be placed in the next Main Batch!")

  if "$3b"==message.content:
    await message.channel.send("> You will receive a call from our team within 48 hours. You can ping Team AccioJob here if you don't receive a call even then.")

  if "$4"==message.content:
    await message.channel.send("Your question will be solved shortly by a human!")

  #keyword trigger based response

  msg_text = message.content.strip().lower()

  #keyword_1 = ['interview', 'when']
  #keyword_1a = ['interview', 'what', 'time']
  keyword_2 = ['coding', 'test', 'times']
  keyword_3 = ['eligible', 'join']
  keyword_4 = ['minimum', 'join', 'qualification']
  keyword_5 = ['when', 'joining', 'batch']
  keyword_6 = ['duration', 'course']
  keyword_7 = ['batch', 'next', 'starting']
  keyword_8 = ['what', 'isa']
  keyword_9 = ['solve', 'language']
  keyword_10 = ['join', 'without', 'clearing']
  keyword_11 = ['grade', 'gap', 'grades', 'mechanical', 'electrical', 'civil']
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
  #if all(word in msg_text for word in keyword_1):
    #await message.channel.send("> Your will receive a call within 48 hours of booking your interview on the website. If you have not, then you can then ping the staff here!")
  #if all(word in msg_text for word in keyword_1a):
    #await message.channel.send("> Your will receive a call within 48 hours of booking your interview on the website. If you have not, then you can then ping the staff here!")
  if all(word in msg_text for word in keyword_2):
    await message.channel.send("> Do not worry if you fail the coding test. We do not have any limit for the number of attempts. You will be able to re-attempt it after 7 days time until you pass it.")
  if all(word in msg_text for word in keyword_3):
    await message.channel.send("> You need to be a 2023 graduate or earlier to apply for AccioJob. You will be eligible for Pay after placement offer if you are a graduate between 2018 and 2023. You will be applicable for payupfront option if you are 2017 graduate or earlier.")
  if all(word in msg_text for word in keyword_4):
    await message.channel.send("> You need to be a 2023 graduate or earlier to be eligible to join the course.")
  if all(word in msg_text for word in keyword_5):
    await message.channel.send("> You will receive the joining details of your batch one day before your batch starts.")
  if all(word in msg_text for word in keyword_6):
    await message.channel.send("> The course duration is 6 months.")
  if all(word in msg_text for word in keyword_7):
    await message.channel.send("> The next batch is starting on May 18th!")
  if all(word in msg_text for word in keyword_8):
    await message.channel.send("> Terms and conditions are straight forward. We have a 12 month agreement with the student. Training goes on for the first 6 months. Placements start from the 3rd month onwards and goes on till the 12th month. The student starts paying only after they get placed above 5 LPA during these 12 months.")
  if all(word in msg_text for word in keyword_9):
    await message.channel.send("> You can use any language to solve the modules and further in the interview also but the course we have is in Java so you would have to work your skills in Java once you get selected.")
  if all(word in msg_text for word in keyword_10):
    await message.channel.send("> You can pay the fee upfront if you don't want to clear the tests.")
  if any(word in msg_text for word in keyword_11):
    await message.channel.send("> No, it will not matter for course joining or even for placements. Companies coming for placement only look for your coding skills, which we, here at AccioJob teach you!")
  if all(word in msg_text for word in keyword_12):
    await message.channel.send("> Once you start the course with us and sign the ISA, you will have to pay us the course fee when you get placed in IT sector above 5 LPA. If you get placed in a non-IT company or below 5 LPA and you want to quit the Main Batch then you will have to pay the course fee.")
  if all(word in msg_text for word in keyword_13):
    await message.channel.send("> The timings for live classes are from 8 PM to 11 PM on weekdays. You will have to put in 2-3 hours of extra effort to get your assignment and learning done everyday. And we have soft skills practice sessions, contests and profile building on weekends.")
  if all(word in msg_text for word in keyword_14):
    await message.channel.send("> Please check your spam folder for the email. If you have still not received the email then you can ping a staff member here with your email ID.")
  if all(word in msg_text for word in keyword_15):
    await message.channel.send("> You will need to spend at least 5-6 hours per day throughout the duration of the course.")
  if all(word in msg_text for word in keyword_16):
    await message.channel.send("The fee structure for the Pay Upfront option is as follows: \n> - INR 4,999 registration fees payable now + INR 45,000 + GST payable after 7 day trial \n> - 100% refund of registration fees if not satisfied after the 7-day trial.")
  if all(word in msg_text for word in keyword_17):
    await message.channel.send("> If you have completed all the modules thoroughly and written programs on your own then you will be able to clear the coding test fairly well! If you want more practice questions then you can refer to this link https://expensive-amount-815.notion.site/Further-Practice-Questions-AccioJob-Modules-93a32105a2d8496fb35149e7ef9216f8 and you can even practice more on Hackerrank/Leetcode.")
  if all(word in msg_text for word in keyword_18):
    await message.channel.send("> If you have solved all module questions thoroughly and practiced some more questions on your own then you should be able to clear the coding test! If you want more practice questions then you can refer to this link https://expensive-amount-815.notion.site/Further-Practice-Questions-AccioJob-Modules-93a32105a2d8496fb35149e7ef9216f8 and you can even practice more on Hackerrank/Leetcode.")
  if all(word in msg_text for word in keyword_19):
    await message.channel.send("> We have closed interviews and admittance to the April 27th Batch. \n> You will be able to schedule your interview from May 13th onwards for the May 18th Main Batch. \n> Till then you can practice some coding by yourself from this website https://expensive-amount-815.notion.site/Further-Practice-Questions-AccioJob-Modules-93a32105a2d8496fb35149e7ef9216f8 and you can even practice more on Hackerrank/Leetcode.")
  if all(word in msg_text for word in keyword_20):
    await message.channel.send("> There will be a variety of projects! you'll be working on atleast 2 projects on DSA and a lot of projects on front-end, you'll have a repository of projects you can choose to work on post selection in the main batch.")
  if any(word in msg_text for word in keyword_21):
    await message.channel.send("> You'll have 2 instructors one for main class and the other for doubt class!")
  if all(word in msg_text for word in keyword_22):
    await message.channel.send("> The course curriculum is: \n> First 2 months we teach you DSA in Java, OOPS, SQL, System Design \n> Next 2 month we teach you front end webdev - HTML, CSS, Javascript, ReactJS and Redux \n> The last 2 months we teach you back end webdev - NodeJS, Express and MongoDB. \n> This covers the DSA and Full stack development!")
  if all(word in msg_text for word in keyword_23):
    await message.channel.send("> There will be 2 questions in the coding test to be solved within an hour. \n> You need to clear 50% i.e., all test cases of at least 1 question at least or half test cases of both the questions.")
  if all(word in msg_text for word in keyword_24):
    await message.channel.send("> You will need a webcam for the coding test and the interview.")
  if all(word in msg_text for word in keyword_25):
    await message.channel.send("> We have more 200 hiring partners, most of these are product based, we also have some service based companies that hire from us. You can find a sample list of hiring partners on our website. \n> Some partners are- Thoughworks, Gainsight, Visa, Converj, Paytm, Maersk, Tata Digital, Makemytrip, salesforce, etc.")

keep_alive()
client.run(os.getenv('token'))