# -*- coding:utf8 -*-
#!/usr/bin/env python
import os
import re
import sys
import smtplib
import database
import email
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class mailfunc:
	def _send(self, msg, reciver, part):
		msg.attach(part)
		sender = "kkk@gmail.com"	
		s = smtplib.SMTP('smtp.gmail.com')
		s.sendmail(sender, reciver, msg.as_string())
		s.quit()

	def domail(self, IP, time):
		msg = MIMEMultipart('alternative')
		msg['Subject'] = u"【公告】OOOO"
		msg['From'] = "qqq@gmail.com"
		recivers = ('aaaa@gmail.com', 'bbbb@gmail.com')
		msg['To'] = "; ".join(recivers)
#		msg['CC'] = "cccc@gmail.com"
#		recivers = recivers + (msg['CC'],)
		
		html = """\
		<html>
		<head></head>
			<body>
			</body>
		</html>
		"""
		part = MIMEText(html, 'html', 'utf-8')
		self._send(msg, recivers, part)

