# SST-MEG
This repository contains the MEG scripts to analyze MEG data collected before and after 6 weeks of rTMS treatment combined with psychotherapy as a treatment for patients with treatment resistant depression. 
For this study we have three tasks: a subliminal goal priming task, a working memory task, and a resting state.

### Subliminal goal priming task 


Task description:

```
This is a subliminal task in which we present a total of 4468 flashing stimuli.
Most of those stimuli (n = 4397) are simply random characters of random letters that we are not analyzing.
Then, we have 3 stimuli of interest:
- Subject-generated words (n = 40) ,
- Other words that are not semantically related (n = 20),
- Red font non-words (n= 40).

The red font category is only to ensure participants are paying attention to the task,
as they are asked to press a button when the color font change to red.

We have 4 blocks of this task (each block lasting about 9 minutes).
Each block corresponds to a different word condition related to:
- Promotion goals (making good things happen). This category is generated by contrasting:
characteristics that participants think they have,  to characteristics they would ideally like to have.

- Prevention goals (preventing bad things from happening). This category is generated by contrasting:
characteristics that participants think they have, to characteristics they ought to have.

For each of those two categories, we generate:
- synonyms: "match" (this illustrates that participants are close to reach the goal)
- antonyms: "mismatch" (this illustrates that participants are far from reaching the goal)

Therefore resulting in our four blocks:
promotion match ("Promatch")
promotion mismatch ("Promismatch")
prevention match ("Prevmatch")
prevention mismatch ("Prevmismatch")
```

Hypothesis:


```
This task has been ran with fMRI already with participants without depression (Detloff et al., 2020)
Contrasts were done between each priming condition and other words from the same block.
Promotion priming discriminantly engaged left prefrontal cortex (BA 9),
Prevention priming discriminantly engaged right prefrontal cortex (BA 8/9)

More precisely,
Promotion match > Other workds led to 2 clusters of activations:
- Left middle frontal gyrus (BA 9), left inferior and superior temporal gyrus (BA 20 and 38), and left fusiform gyrus (BA 10).
- Right inferior and middle temporal gyrus and precuneus (BA 7, 20, and 21) and right lateral occipital cortex (BA 19).

Promotion mismatch > Other words led to activations:
Left frontal lobe (specifically left middle frontal gyrus and inferior frontal gyrus, BA 9 and 45/46/47).

Prevention match > Others: Two significant clusters were found:
- Right middle and superior frontal gyrus (BA 8/9/10) and left middle frontal gyrus (BA 6).
- Right and left supramarginal gyrus and right angular gyrus (BA 7 and 40)

Prevention mismatch > Others: 
Bilateral caudate as well as bilateral occipital lobe, specifically left and right intracalcarine cortex (BA 18

so we hypothesize that:
Promatch and promismatch should lead to left prefrontal cortex activation
Prevmatch and prevmismatch should lead to right prefrontal cortex activation

As a quality check, Red font should lead to motor cortex activations
```


Technical informations :


```
Currently the task is set up at the MEG so that the display of the stimuli of interest are associated with a different amplitude for the trigger on channel UPPT001. (No pixel in the task yet).

- Subject-specific words are saved with an amplitude of 64
- Other words are saved with an amplitude of 32
- Red fonts are saved with an amplitude of 16

We are recording eye blinks (EEG054) and heart bit (EEG055) 

Code: 
```

On Biowulf: 
module use --append /data/MEGmodules/modulefiles

sinteractive --mem=6G --cpus-per-task=4 --gres=lscratch:50

#module load mne_scripts
#This command gave me a warning on using mne instead so switching

module load mne

make_meg_bids.py -bids_dir /data/FMRI_SST_Therapy/MEG_BIDS -meg_input_dir /data/FMRI_SST_Therapy/MEG/T026_Baseline -mri_bsight /data/FMRI_SST_Therapy/MEG/T026_T1fs_conform.nii.gz -mri_bsight_elec /data/FMRI_SST_Therapy/MEG/T026_baseline_electrodes.txt -bids_session 01




### Working Memory task 

Task description:

```
This is a basic Sternberg task. Each trial begins with a fixation cross displayed for 2 seconds,
followed by the presentation of a sequence of 4 or 6 letters for another 2 seconds.
Participants are instructed to memorize the letters during a 3-second delay period.
After the delay, a probe is shown for 3 seconds,
participants must indicate whether the letter in the probe was part of the initial sequence.
If the letter was in the probe, participants have to press the left (green) button
If the letter was not in the probe, participants have to press the right (blue) button
The task consists in one block with 80 trials for a total duration of 800 seconds. 
 - 40 trials with a set size of 4 ;
 - 40 trials with a set size of 6, 

```

Hypothesis:


```
We expect fronto-parietal activations while participants are performing the task,
mainly during the delay period of the task when they are actually reharsing the letters;
and especially on the left hemishphere, and stronger when the task is harder (set size of 6)


```


Technical informations :
```
UADC006 green button
UADC007 blue button
We are recording eye blinks (EEG054) and heart bit (EEG055) 
At the moment I do not know about the task trigger.

```

### Resting state 


Task description:

```
This is only a 10 minutes task with eyes open and a fixation cross for participants to look at
