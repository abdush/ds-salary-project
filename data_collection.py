# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 16:31:30 2020

@author: abdu
"""

import glassdoor_scraper as gs
import pandas as pd

chromedriver = "./chromedriver"
keyword = "data scientist"
num_jobs = 1000
slp_time = 10

df = gs.get_jobs(keyword, num_jobs, False, chromedriver, slp_time)

df.to_csv("glassdoor_jobs.csv", index=False)