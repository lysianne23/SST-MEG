# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#### Import required stuff ######
import pandas as pd
import sys, os, tempfile
from math import floor
import numpy as np
import scipy
import sys
import mne
import copy
## load the required modules: 

#from nih2mne.utilities.trigger_utilities import (check_analog_inverted, threshold_detect, parse_marks, detect_digital, append_conditions)
#from nih2mne.utilities.markerfile_write import main as writemarkerfile

filename = '~/sub-T026_ses-1_task-sst_run-01_meg.ds/sub-T026_ses-1_task-sst_run-01_meg_cleaned_cut.fif'

raw = mne.io.read_raw_fif(filename, preload=True)
raw.plot()


raw.filter(1,110,n_jobs=-1)
raw.notch_filter([60, 120],n_jobs=-1)
ica = mne.preprocessing.ICA(n_components=20)
ica.fit(raw)
#Plot the components 
ica.plot_components()
#Plot the TS of the components 
ica.plot_sources(raw)
#Click on the components that could be heart beat, eye blinks, general noise
# They should show up as greyed out 
ica.apply(raw)
# plot power spectrum density
raw.plot_psd()

#Events of interest
EOI = ['SUBJECT_WORDS', 'OTHER_WORDS',  'RED']
EVTS, EVTSID = mne.events_from_annotations(raw)
EVTSID = {i:j for i,j in EVTSID.items() if i in EOI}

EPO = mne.Epochs(raw,events=EVTS, event_id = EVTSID)
Button = EPO['RED']
Button_psd = Button.compute_psd()
Button.plot_psd_topomap()
SUBJECT_WORDS = EPO['SUBJECT_WORDS']
SUBJECT_WORDS_psd = SUBJECT_WORDS.compute_psd()
diff = copy.deepcopy(Button_psd)
Button.plot_psd

diff._data = np.mean(diff._data, axis=0, keepdims=True)
diff._data -= np.mean(SUBJECT_WORDS_psd._data, axis=0, keepdims=True)


