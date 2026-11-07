# Rehearsal feedback — iteration 82 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.47, 'tol': 0.32, 'offset': 0.16, 'seg_timeout': 36.09}
  role0 prep: grab ramp to ramp_inside[yaw3,direct] release | play: segments then to door_block[yaw0,door] release -> grab box to stay[yaw3,door] lock -> [when opponent_visible] to door_inside[yaw2,door]
  role1 prep: grab ramp to ramp_inside[yaw3,direct] release | play: segments then to door_block[yaw0,door] release -> grab box to stay[yaw3,door] lock -> [when opponent_visible] to door_inside[yaw2,door]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.359
- hider win-rate: 0.30
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.19}
- mean first-seen play step: 36.0
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.90, mean max seeker z: 0.27

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@40; play0/1:dropped@41; play0/1:dropped@55; play0/1:done@58; play0/2:done@77; prep1/0:no_object@0; play1/0:done@40; play1/1:timeout@77; play1/2:dropped@78
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:dropped@34; play0/0:done@34; play0/1:timeout@71; play0/2:dropped@72; play0/2:done@74; prep1/0:no_object@0; play1/0:timeout@68
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:dropped@34; play0/0:done@45; prep1/0:no_object@0; play1/0:no_target@32; play1/1:timeout@69; play1/2:dropped@70; play1/2:no_target@70
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@13; play0/0:done@40; play0/1:dropped@41; play0/1:timeout@77; prep1/0:no_object@0; play1/0:done@43
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; play0/1:dropped@69; prep1/0:no_object@0; play1/0:no_target@32; play1/1:timeout@69
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@6; play0/0:timeout@68; play0/1:dropped@69; prep1/0:no_object@0; play1/0:timeout@68
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@44; play0/1:dropped@45; play0/1:dropped@55; prep1/0:no_object@0; play1/0:no_target@32; play1/1:timeout@69; play1/2:dropped@70; play1/2:no_target@70
- p_door=0.25 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.01, 1.67] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@25; play0/0:done@63; play0/1:dropped@64; prep1/0:no_object@0; play1/0:no_target@32; play1/1:done@48; play1/2:no_target@65