# -*- coding:utf8 -*-

import os
import re
import sys
import time
from lib import mailfunc

def main():
	mail = mailfunc.mailfunc()
	now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
	mail.domail(now)

if __name__ == "__main__":
	main()

