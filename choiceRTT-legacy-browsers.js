/****************** 
 * Choicertt Test *
 ******************/


// store info about the experiment session:
let expName = 'choiceRTT';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from code_2
fA = 0.5;
fB = 0.5;
fC = 0.5;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1, 1, 1]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructionsRoutineBegin());
flowScheduler.add(instructionsRoutineEachFrame());
flowScheduler.add(instructionsRoutineEnd());
const PracticeLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PracticeLoopLoopBegin(PracticeLoopLoopScheduler));
flowScheduler.add(PracticeLoopLoopScheduler);
flowScheduler.add(PracticeLoopLoopEnd);
flowScheduler.add(end_messageRoutineBegin());
flowScheduler.add(end_messageRoutineEachFrame());
flowScheduler.add(end_messageRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'delay_disc_conditions.xlsx', 'path': 'delay_disc_conditions.xlsx'},
    {'name': 'images/target_I.jpg', 'path': 'images/target_I.jpg'},
    {'name': 'images/target_plus.jpg', 'path': 'images/target_plus.jpg'},
    {'name': 'images/target_square.jpg', 'path': 'images/target_square.jpg'},
    {'name': 'images/target_T.jpg', 'path': 'images/target_T.jpg'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var instructionsClock;
var instr;
var startInst;
var startMouse;
var trialClock;
var keyResp;
var sound_1;
var sound_2;
var sound_3;
var trial_feedbackClock;
var feedback;
var moveOnKeys;
var end_messageClock;
var end_text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr',
    text: "In each trial you will recieve audio stimuli.\nAt the end of the trial, respond either 'f', 'g' or 'h' if you think that the loudest sound was the first, second or third stimuli.\n\n\nPush spacebar to continue.",
    font: 'Arial',
    units: 'height', 
    pos: [0, 0.1], height: 0.035,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1,
    depth: 0.0 
  });
  
  startInst = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  startMouse = new core.Mouse({
    win: psychoJS.window,
  });
  startMouse.mouseClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  keyResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  sound_1 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 1.0,
    });
  sound_1.setVolume(fA);
  sound_2 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 1.0,
    });
  sound_2.setVolume(fB);
  sound_3 = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: 1.0,
    });
  sound_3.setVolume(fC);
  // Initialize components for Routine "trial_feedback"
  trial_feedbackClock = new util.Clock();
  feedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  moveOnKeys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end_message"
  end_messageClock = new util.Clock();
  end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'end_text',
    text: 'That’s the experiment finished!\n\nThanks for your time. You’ve earned a cup of tea.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _startInst_allKeys;
var gotValidClick;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startInst.keys = undefined;
    startInst.rt = undefined;
    _startInst_allKeys = [];
    // setup some python lists for storing info about the startMouse
    gotValidClick = false; // until a click is received
    startMouse.mouseClock.reset();
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instr);
    instructionsComponents.push(startInst);
    instructionsComponents.push(startMouse);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instr* updates
    if (t >= 0.0 && instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instr.tStart = t;  // (not accounting for frame time here)
      instr.frameNStart = frameN;  // exact frame index
      
      instr.setAutoDraw(true);
    }

    
    // *startInst* updates
    if (t >= 0.0 && startInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startInst.tStart = t;  // (not accounting for frame time here)
      startInst.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { startInst.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { startInst.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { startInst.clearEvents(); });
    }

    if (startInst.status === PsychoJS.Status.STARTED) {
      let theseKeys = startInst.getKeys({keyList: [], waitRelease: false});
      _startInst_allKeys = _startInst_allKeys.concat(theseKeys);
      if (_startInst_allKeys.length > 0) {
        startInst.keys = _startInst_allKeys[_startInst_allKeys.length - 1].name;  // just the last key pressed
        startInst.rt = _startInst_allKeys[_startInst_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *startMouse* updates
    if (t >= 0.0 && startMouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startMouse.tStart = t;  // (not accounting for frame time here)
      startMouse.frameNStart = frameN;  // exact frame index
      
      startMouse.status = PsychoJS.Status.STARTED;
      prevButtonState = startMouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (startMouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = startMouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // end routine on response
          continueRoutine = false;
        }
      }
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    startInst.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var PracticeLoop;
function PracticeLoopLoopBegin(PracticeLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    PracticeLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'delay_disc_conditions.xlsx',
      seed: undefined, name: 'PracticeLoop'
    });
    psychoJS.experiment.addLoop(PracticeLoop); // add the loop to the experiment
    currentLoop = PracticeLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    PracticeLoop.forEach(function() {
      snapshot = PracticeLoop.getSnapshot();
    
      PracticeLoopLoopScheduler.add(importConditions(snapshot));
      PracticeLoopLoopScheduler.add(trialRoutineBegin(snapshot));
      PracticeLoopLoopScheduler.add(trialRoutineEachFrame());
      PracticeLoopLoopScheduler.add(trialRoutineEnd(snapshot));
      PracticeLoopLoopScheduler.add(trial_feedbackRoutineBegin(snapshot));
      PracticeLoopLoopScheduler.add(trial_feedbackRoutineEachFrame());
      PracticeLoopLoopScheduler.add(trial_feedbackRoutineEnd(snapshot));
      PracticeLoopLoopScheduler.add(PracticeLoopLoopEndIteration(PracticeLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function PracticeLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(PracticeLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function PracticeLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var fA;
var fB;
var fC;
var startA;
var startB;
var startC;
var corrAns;
var _keyResp_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from setStimuli
    fA = Number.parseFloat(f1);
    fB = Number.parseFloat(f2);
    fC = Number.parseFloat(f3);
    startA = Number.parseFloat(start1);
    startB = Number.parseFloat(start2);
    startC = Number.parseFloat(start3);
    if (f1_greater) {
        corrAns = "f";
    }
    if (f2_greater) {
        corrAns = "g";
    }
    if (f3_greater) {
        corrAns = "h";
    }
    
    keyResp.keys = undefined;
    keyResp.rt = undefined;
    _keyResp_allKeys = [];
    sound_1.secs=1.0;
    sound_1.setVolume(fA);
    sound_2.secs=1.0;
    sound_2.setVolume(fB);
    sound_3.secs=1.0;
    sound_3.setVolume(fC);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(keyResp);
    trialComponents.push(sound_1);
    trialComponents.push(sound_2);
    trialComponents.push(sound_3);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *keyResp* updates
    if (t >= start2 && keyResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyResp.tStart = t;  // (not accounting for frame time here)
      keyResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      keyResp.clock.reset();
      keyResp.start();
      keyResp.clearEvents();
    }

    frameRemains = start2 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (keyResp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      keyResp.status = PsychoJS.Status.FINISHED;
  }

    if (keyResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyResp.getKeys({keyList: ['f', 'g', 'h'], waitRelease: false});
      _keyResp_allKeys = _keyResp_allKeys.concat(theseKeys);
      if (_keyResp_allKeys.length > 0) {
        keyResp.keys = _keyResp_allKeys[_keyResp_allKeys.length - 1].name;  // just the last key pressed
        keyResp.rt = _keyResp_allKeys[_keyResp_allKeys.length - 1].rt;
        // was this correct?
        if (keyResp.keys == corrAns) {
            keyResp.corr = 1;
        } else {
            keyResp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // start/stop sound_1
    if (t >= startA && sound_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_1.tStart = t;  // (not accounting for frame time here)
      sound_1.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_1.play(); });  // screen flip
      sound_1.status = PsychoJS.Status.STARTED;
    }
    frameRemains = startA + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (1.0 > 0.5) {
        sound_1.stop();  // stop the sound (if longer than duration)
      }
      sound_1.status = PsychoJS.Status.FINISHED;
    }
    // start/stop sound_2
    if (t >= startB && sound_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_2.tStart = t;  // (not accounting for frame time here)
      sound_2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_2.play(); });  // screen flip
      sound_2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = startB + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (1.0 > 0.5) {
        sound_2.stop();  // stop the sound (if longer than duration)
      }
      sound_2.status = PsychoJS.Status.FINISHED;
    }
    // start/stop sound_3
    if (t >= startC && sound_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      sound_3.tStart = t;  // (not accounting for frame time here)
      sound_3.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ sound_3.play(); });  // screen flip
      sound_3.status = PsychoJS.Status.STARTED;
    }
    frameRemains = startC + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (sound_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (1.0 > 0.5) {
        sound_3.stop();  // stop the sound (if longer than duration)
      }
      sound_3.status = PsychoJS.Status.FINISHED;
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var thisRoutineDuration;
var thisRespType;
var thisRecRT;
var thisAcc;
function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (keyResp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         keyResp.corr = 1;  // correct non-response
      } else {
         keyResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(keyResp.corr, level);
    }
    psychoJS.experiment.addData('keyResp.keys', keyResp.keys);
    psychoJS.experiment.addData('keyResp.corr', keyResp.corr);
    if (typeof keyResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('keyResp.rt', keyResp.rt);
        routineTimer.reset();
        }
    
    keyResp.stop();
    // Run 'End Routine' code from recordRTandAccuracy
    thisRoutineDuration = t;
    thisRespType = "keyboard";
    thisRecRT = (keyResp.rt - start3);
    if ((keyResp.corr === 1)) {
        thisAcc = "correct";
    } else {
        thisAcc = "incorrect";
    }
    
    sound_1.stop();  // ensure sound has stopped at end of routine
    sound_2.stop();  // ensure sound has stopped at end of routine
    sound_3.stop();  // ensure sound has stopped at end of routine
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _moveOnKeys_allKeys;
var trial_feedbackComponents;
function trial_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_feedback' ---
    t = 0;
    trial_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    feedback.setText((("Answer was " + thisAcc.toString()) + "\n \n Press spacebar to continue."));
    moveOnKeys.keys = undefined;
    moveOnKeys.rt = undefined;
    _moveOnKeys_allKeys = [];
    // keep track of which components have finished
    trial_feedbackComponents = [];
    trial_feedbackComponents.push(feedback);
    trial_feedbackComponents.push(moveOnKeys);
    
    trial_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trial_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_feedback' ---
    // get current time
    t = trial_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback* updates
    if (t >= 1.0 && feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback.tStart = t;  // (not accounting for frame time here)
      feedback.frameNStart = frameN;  // exact frame index
      
      feedback.setAutoDraw(true);
    }

    
    // *moveOnKeys* updates
    if (t >= 0.0 && moveOnKeys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      moveOnKeys.tStart = t;  // (not accounting for frame time here)
      moveOnKeys.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { moveOnKeys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { moveOnKeys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { moveOnKeys.clearEvents(); });
    }

    if (moveOnKeys.status === PsychoJS.Status.STARTED) {
      let theseKeys = moveOnKeys.getKeys({keyList: ['space'], waitRelease: false});
      _moveOnKeys_allKeys = _moveOnKeys_allKeys.concat(theseKeys);
      if (_moveOnKeys_allKeys.length > 0) {
        moveOnKeys.keys = _moveOnKeys_allKeys[_moveOnKeys_allKeys.length - 1].name;  // just the last key pressed
        moveOnKeys.rt = _moveOnKeys_allKeys[_moveOnKeys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_feedback' ---
    trial_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(moveOnKeys.corr, level);
    }
    psychoJS.experiment.addData('moveOnKeys.keys', moveOnKeys.keys);
    if (typeof moveOnKeys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('moveOnKeys.rt', moveOnKeys.rt);
        routineTimer.reset();
        }
    
    moveOnKeys.stop();
    // the Routine "trial_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var end_messageComponents;
function end_messageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end_message' ---
    t = 0;
    end_messageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    end_messageComponents = [];
    end_messageComponents.push(end_text);
    
    end_messageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function end_messageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end_message' ---
    // get current time
    t = end_messageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_text* updates
    if (t >= 0.5 && end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_text.tStart = t;  // (not accounting for frame time here)
      end_text.frameNStart = frameN;  // exact frame index
      
      end_text.setAutoDraw(true);
    }

    frameRemains = 0.5 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (end_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      end_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    end_messageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function end_messageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end_message' ---
    end_messageComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
