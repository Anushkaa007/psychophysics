#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.1),
    on Fri Jul 21 22:33:31 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code_2
fA = 0.5
fB = 0.5
fC = 0.5



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.1'
expName = 'choice_RTT_demo'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ftixidre/CAMP2023/Project/camp2023_psychophysics/choiceRTT_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1, 1, 1], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}
ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='event')

# --- Initialize components for Routine "instructions" ---
instr = visual.TextStim(win=win, name='instr',
    text="In each trial you will recieve audio stimuli.\nAt the end of the trial, respond either 'f', 'g' or 'h' if you think that the loudest sound was the first, second or third stimuli.\n\n\nPush spacebar to continue.",
    font='Arial',
    units='height', pos=(0, 0.1), height=0.035, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
startInst = keyboard.Keyboard()
startMouse = event.Mouse(win=win)
x, y = [None, None]
startMouse.mouseClock = core.Clock()

# --- Initialize components for Routine "trial" ---
keyResp = keyboard.Keyboard()
sound_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=False,
    name='sound_1')
sound_1.setVolume(fA)
sound_2 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(fB)
sound_3 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(fC)

# --- Initialize components for Routine "trial_feedback" ---
feedback = visual.TextStim(win=win, name='feedback',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
moveOnKeys = keyboard.Keyboard()

# --- Initialize components for Routine "end_message" ---
end_text = visual.TextStim(win=win, name='end_text',
    text='That’s the experiment finished!\n\nThanks for your time. You’ve earned a cup of tea.',
    font='Arial',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
# update component parameters for each repeat
startInst.keys = []
startInst.rt = []
_startInst_allKeys = []
# setup some python lists for storing info about the startMouse
gotValidClick = False  # until a click is received
startMouse.mouseClock.reset()
# keep track of which components have finished
instructionsComponents = [instr, startInst, startMouse]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr* updates
    
    # if instr is starting this frame...
    if instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr.frameNStart = frameN  # exact frame index
        instr.tStart = t  # local t and not account for scr refresh
        instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr, 'tStartRefresh')  # time at next scr refresh
        # update status
        instr.status = STARTED
        instr.setAutoDraw(True)
    
    # if instr is active this frame...
    if instr.status == STARTED:
        # update params
        pass
    
    # *startInst* updates
    waitOnFlip = False
    
    # if startInst is starting this frame...
    if startInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startInst.frameNStart = frameN  # exact frame index
        startInst.tStart = t  # local t and not account for scr refresh
        startInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startInst, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'startInst.started')
        # update status
        startInst.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(startInst.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(startInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if startInst.status == STARTED and not waitOnFlip:
        theseKeys = startInst.getKeys(keyList=None, waitRelease=False)
        _startInst_allKeys.extend(theseKeys)
        if len(_startInst_allKeys):
            startInst.keys = _startInst_allKeys[-1].name  # just the last key pressed
            startInst.rt = _startInst_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    # *startMouse* updates
    
    # if startMouse is starting this frame...
    if startMouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        startMouse.frameNStart = frameN  # exact frame index
        startMouse.tStart = t  # local t and not account for scr refresh
        startMouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(startMouse, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('startMouse.started', t)
        # update status
        startMouse.status = STARTED
        prevButtonState = startMouse.getPressed()  # if button is down already this ISN'T a new click
    if startMouse.status == STARTED:  # only update if started and not finished!
        buttons = startMouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # end routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PracticeLoop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('delay_disc_conditions.xlsx'),
    seed=None, name='PracticeLoop')
thisExp.addLoop(PracticeLoop)  # add the loop to the experiment
thisPracticeLoop = PracticeLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
if thisPracticeLoop != None:
    for paramName in thisPracticeLoop:
        exec('{} = thisPracticeLoop[paramName]'.format(paramName))

for thisPracticeLoop in PracticeLoop:
    currentLoop = PracticeLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeLoop.rgb)
    if thisPracticeLoop != None:
        for paramName in thisPracticeLoop:
            exec('{} = thisPracticeLoop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "trial" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from setStimuli
    #positionList = [-0.375,-0.125,0.125,0.375] #list of possible X coordinates for target to appear
    #shuffle(positionList) #randomise these positions
    #targetX = positionList[0] #pick the first value from the list 
    #
    ##thisImage is the variable in the Image field of targetImage
    #if thisImage == 'images/target_square.jpg': #path of where to find the target image
    #    corrAns = 'v' #setting the key press that will be the correct answer
    #    #corrButton = square_button #setting the button that will be the correct answer
    #    corrButtonName = 'square_button' #making this a string so that it can be compared later when checking for acccuracy
    #elif thisImage == 'images/target_cross.jpg':
    #    corrAns = 'c'
    #    #corrButton = cross_button
    #    corrButtonName = 'cross_button'
    #elif thisImage == 'images/target_plus.jpg':
    #    corrAns = 'b'
    #    #corrButton = plus_button
    #    corrButtonName = 'plus_button'
    #
    #
    
    fA = float(f1)
    fB = float(f2)
    fC = float(f3)
    
    startA = float(start1)
    startB = float(start2)
    startC = float(start3)
    
    if f1_greater:
        corrAns = 'f'
    if f2_greater:
        corrAns = 'g'
    if f3_greater:
        corrAns = 'h'
    keyResp.keys = []
    keyResp.rt = []
    _keyResp_allKeys = []
    sound_1.setSound('A', secs=1.0, hamming=False)
    sound_1.setVolume(fA, log=False)
    sound_2.setSound('A', secs=1.0, hamming=True)
    sound_2.setVolume(fB, log=False)
    sound_3.setSound('A', secs=1.0, hamming=True)
    sound_3.setVolume(fC, log=False)
    # keep track of which components have finished
    trialComponents = [keyResp, sound_1, sound_2, sound_3]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *keyResp* updates
        
        # if keyResp is starting this frame...
        if keyResp.status == NOT_STARTED and t >= start2-frameTolerance:
            # keep track of start time/frame for later
            keyResp.frameNStart = frameN  # exact frame index
            keyResp.tStart = t  # local t and not account for scr refresh
            keyResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyResp, 'tStartRefresh')  # time at next scr refresh
            # update status
            keyResp.status = STARTED
            # keyboard checking is just starting
            keyResp.clock.reset()  # now t=0
            keyResp.clearEvents(eventType='keyboard')
        
        # if keyResp is stopping this frame...
        if keyResp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyResp.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                keyResp.tStop = t  # not accounting for scr refresh
                keyResp.frameNStop = frameN  # exact frame index
                # update status
                keyResp.status = FINISHED
                keyResp.status = FINISHED
        if keyResp.status == STARTED:
            theseKeys = keyResp.getKeys(keyList=['f','g','h'], waitRelease=False)
            _keyResp_allKeys.extend(theseKeys)
            if len(_keyResp_allKeys):
                keyResp.keys = _keyResp_allKeys[-1].name  # just the last key pressed
                keyResp.rt = _keyResp_allKeys[-1].rt
                # was this correct?
                if (keyResp.keys == str(corrAns)) or (keyResp.keys == corrAns):
                    keyResp.corr = 1
                else:
                    keyResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_1
        
        # if sound_1 is starting this frame...
        if sound_1.status == NOT_STARTED and tThisFlip >= startA-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_1.started', tThisFlipGlobal)
            # update status
            sound_1.status = STARTED
            sound_1.play(when=win)  # sync with win flip
        
        # if sound_1 is stopping this frame...
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_1.stopped')
                # update status
                sound_1.status = FINISHED
                sound_1.stop()
        # start/stop sound_2
        
        # if sound_2 is starting this frame...
        if sound_2.status == NOT_STARTED and tThisFlip >= startB-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_2.started', tThisFlipGlobal)
            # update status
            sound_2.status = STARTED
            sound_2.play(when=win)  # sync with win flip
        
        # if sound_2 is stopping this frame...
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_2.stopped')
                # update status
                sound_2.status = FINISHED
                sound_2.stop()
        # start/stop sound_3
        
        # if sound_3 is starting this frame...
        if sound_3.status == NOT_STARTED and tThisFlip >= startC-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_3.started', tThisFlipGlobal)
            # update status
            sound_3.status = STARTED
            sound_3.play(when=win)  # sync with win flip
        
        # if sound_3 is stopping this frame...
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'sound_3.stopped')
                # update status
                sound_3.status = FINISHED
                sound_3.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial" ---
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if keyResp.keys in ['', [], None]:  # No response was made
        keyResp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           keyResp.corr = 1;  # correct non-response
        else:
           keyResp.corr = 0;  # failed to respond (incorrectly)
    # store data for PracticeLoop (TrialHandler)
    PracticeLoop.addData('keyResp.keys',keyResp.keys)
    PracticeLoop.addData('keyResp.corr', keyResp.corr)
    if keyResp.keys != None:  # we had a response
        PracticeLoop.addData('keyResp.rt', keyResp.rt)
    # Run 'End Routine' code from recordRTandAccuracy
    #this code is to record the reaction times and accuracy of the trial
    
    thisRoutineDuration = t # how long did this trial last
    
    # keyResp.rt is the time with which a key was pressed
    # mouseResp.time is the time with which a button was clicked/pressed
    # thisRecRT - how long it took for participants to respond after onset of targetImage
    # thisRespType - keeping track of which response component was used
    # thisAcc - whether or not the response was correct
    # correctMouseResp - name of column in data output which records the accuracy of mouse responses
    
    thisRespType = 'keyboard' #record type of response 
    thisRecRT = keyResp.rt - start3 #record time taken to response
    if keyResp.corr == 1: #if the response is correct
        thisAcc = 'correct' #print correct
    else:
        thisAcc = 'incorrect'
    
    
    #if keyResp.keys:
    #    thisRespType = 'keyboard' #record type of response 
    #    thisRecRT = keyResp.rt - onsetTime #record time taken to response
    #    if keyResp.corr == 1: #if the response is correct
    #        thisAcc = 'correct' #print correct
    #    else:
    #        thisAcc = 'incorrect'
    #else:
    #    thisRespType = 'mouse'
    #    thisRecRT = mouseResp.time[0] - onsetTime
    #    if mouseResp.clicked_name[0] == corrButtonName: #check if what was clicked corresponds to the correct button
    #        thisAcc = 'correct'
    #        thisExp.addData('correctMouseResp', 1) #record accuracy of mouse clicks
    #    else:
    #        thisAcc = 'incorrect'
    #        thisExp.addData('correctMouseResp', 0)
    
    #thisExp.addData('trialRespTimes', thisRecRT) #record the actual response times of each trial
    
    #print(thisRoutineDuration, thisRecRT, thisRespType, thisAcc, onsetTime)
    sound_1.stop()  # ensure sound has stopped at end of routine
    sound_2.stop()  # ensure sound has stopped at end of routine
    sound_3.stop()  # ensure sound has stopped at end of routine
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "trial_feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    feedback.setText("Answer was " + str(thisAcc) + "\n \n Press spacebar to continue.")
    moveOnKeys.keys = []
    moveOnKeys.rt = []
    _moveOnKeys_allKeys = []
    # keep track of which components have finished
    trial_feedbackComponents = [feedback, moveOnKeys]
    for thisComponent in trial_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback* updates
        
        # if feedback is starting this frame...
        if feedback.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            feedback.frameNStart = frameN  # exact frame index
            feedback.tStart = t  # local t and not account for scr refresh
            feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback.started')
            # update status
            feedback.status = STARTED
            feedback.setAutoDraw(True)
        
        # if feedback is active this frame...
        if feedback.status == STARTED:
            # update params
            pass
        
        # *moveOnKeys* updates
        waitOnFlip = False
        
        # if moveOnKeys is starting this frame...
        if moveOnKeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            moveOnKeys.frameNStart = frameN  # exact frame index
            moveOnKeys.tStart = t  # local t and not account for scr refresh
            moveOnKeys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(moveOnKeys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'moveOnKeys.started')
            # update status
            moveOnKeys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(moveOnKeys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(moveOnKeys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if moveOnKeys.status == STARTED and not waitOnFlip:
            theseKeys = moveOnKeys.getKeys(keyList=['space'], waitRelease=False)
            _moveOnKeys_allKeys.extend(theseKeys)
            if len(_moveOnKeys_allKeys):
                moveOnKeys.keys = _moveOnKeys_allKeys[-1].name  # just the last key pressed
                moveOnKeys.rt = _moveOnKeys_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_feedback" ---
    for thisComponent in trial_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if moveOnKeys.keys in ['', [], None]:  # No response was made
        moveOnKeys.keys = None
    PracticeLoop.addData('moveOnKeys.keys',moveOnKeys.keys)
    if moveOnKeys.keys != None:  # we had a response
        PracticeLoop.addData('moveOnKeys.rt', moveOnKeys.rt)
    # the Routine "trial_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'PracticeLoop'


# --- Prepare to start Routine "end_message" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
end_messageComponents = [end_text]
for thisComponent in end_messageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end_message" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 3.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    
    # if end_text is starting this frame...
    if end_text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        end_text.status = STARTED
        end_text.setAutoDraw(True)
    
    # if end_text is active this frame...
    if end_text.status == STARTED:
        # update params
        pass
    
    # if end_text is stopping this frame...
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 2.5-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            # update status
            end_text.status = FINISHED
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_messageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end_message" ---
for thisComponent in end_messageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-3.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
