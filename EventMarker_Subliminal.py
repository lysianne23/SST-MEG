#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

###
#Description : this code is to set up event marker in our Subliminal task 
#currently each stimuli of interest is marked as a trigger of different amplitude on channel UPPT001
#The amplitude is set at 16 (for red fonts) , 32 (for other words), or 64 (for subject's words)
#Participant is asked to press a button when the red font appears (analogue channel)

"""
import pandas as pd
import sys, os, tempfile
from math import floor
import numpy as np
import scipy
import sys
import mne
## load the required modules: 

from nih2mne.utilities.trigger_utilities import (check_analog_inverted, threshold_detect, parse_marks, detect_digital, append_conditions)
from nih2mne.utilities.markerfile_write import main as writemarkerfile


### DEFINE THE FILENAME ##
#filename = '/Volumes/MEG/T026_Baseline/VLURABJX_sst_20240708_001.ds'
#filename = '~/Desktop/VLURABJX_sst_20240708_001.ds'
filename = sys.argv[1]

 ################ Code digital MEG events  #####################


TRIGGERS = detect_digital(filename, channel='UPPT001')
TRIGGERS.loc[TRIGGERS.condition=='16','condition']='RED'
TRIGGERS.loc[TRIGGERS.condition=='32','condition']='OTHER_WORDS'
TRIGGERS.loc[TRIGGERS.condition=='64','condition']='SUBJECT_WORDS'

 ################ Code Button response -  Analogue  #####################
 
RESPONSE = threshold_detect(dsname=filename, mark='response', deadTime=0.5, 
                     derivThresh=0.5, channel='UADC007')
 
dframe = append_conditions([TRIGGERS,RESPONSE]) 

##### Parse Marks ###################
parse_response = parse_marks(dframe, lead_condition='RED', lag_condition='response', marker_on='lag', marker_name='ButtonPress', window=[0, 0.5])
 

##### Generate Marker Files

writemarkerfile(parse_response, filename) 


 ##### This allows to see the plot and check which channels the button press 
raw = mne.io.read_raw_ctf(filename, system_clock='ignore')
raw.pick_types(misc=True,meg=False)
raw.plot(block=True)
