# from celery import shared_task
# from time import sleep
# from django.core.mail import send_mail
# from django.conf import settings

# @shared_task()
# def testfunction(self):
#     for i in range(10):
#         print(i)
#     return 'Done'
# @shared_task()
# def send_feedback_email_task(subject,message):
#     sleep(20)
#     send_mail(
#             # name =name,
#             subject =subject,
#             message=message,
#             from_email = settings.EMAIL_HOST_USER,
#             recipient_list = [settings.RECIPIENT_ADDRESS]
#         )