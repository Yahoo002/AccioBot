import discord
import os
from keep_alive import keep_alive

client = discord.Client()


@client.event
async def on_ready():
  print('We are logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
  async def adminquery():
    await message.channel.send("Congratulations you have reached Admin query portal. Here are a list of FAQs that might be similar to your question:\n")
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
  
  if "$help" in message.content:
    await message.channel.send("How can I help you?\n*$1* - Admin query\n*$2* - course query\n*$3* - Interview based query\n*$4* - Coding Query" )
    
  if "$1"==message.content:
    await adminquery()
    
  if "$1a"==message.content:
    await message.channel.send("> You need to be a 2023 graduate or earlier to apply for AccioJob. You will be eligible for Pay after placement offer if you are a graduate between 2018 and 2023. You will be applicable for payupfront option if you are 2017 graduate or earlier.")

  if "$1b"==message.content:
    await message.channel.send("> You need to be a 2023 graduate to be eligible to join the course.")
    
  if "$1c"==message.content:
    await message.channel.send("> You will receive the joining details of your batch 1 day before your batch starts.")

  if "$2"==message.content:
    await coursequery()

  if "$2a"==message.content:
    await message.channel.send("> The course duration is 6 months.")

  if "$2b"==message.content:
    await message.channel.send("> The next batch is starting on April 25th.")

  if "$2c"==message.content:
    await message.channel.send("> Terms and conditions are straight forward. We have a 12 month agreement with the student. Training goes on for the first 6 months. Placements start from the 3rd month onwards and go on till the 12th month. The student pays the course fees only after they get placed above 5 LPA during these 12 months.")

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


keep_alive()
client.run(os.getenv('token'))