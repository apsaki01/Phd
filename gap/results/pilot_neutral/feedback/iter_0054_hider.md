# Rehearsal feedback — iteration 54 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.47, 'tol': 0.32, 'offset': 0.16, 'seg_timeout': 36.09}
  role0 prep: grab ramp to ramp_inside[yaw3,direct] release | play: segments then grab box to door_block[yaw3,door] lock release -> [when teammate_inside] grab box to teammate[align,direct]
  role1 prep: grab ramp to ramp_inside[yaw3,direct] release | play: segments then grab box to door_block[yaw3,door] lock release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.260
- hider win-rate: 0.25
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.17}
- mean first-seen play step: 34.7
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.28
- seekers entered quadrant: 0.65, mean max seeker z: 0.25

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@40; play0/1:dropped@41; play0/1:done@73; prep1/0:no_object@0; play1/0:timeout@68
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.78, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@39; play0/1:dropped@40; play0/1:timeout@76; prep1/0:no_object@0; play1/0:done@49
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | hiders never seen | segments: play0/0:timeout@68; play0/1:dropped@69; prep1/0:no_object@0; play1/0:dropped@36; play1/0:done@46
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@54; play0/1:dropped@55; prep1/0:no_object@0; play1/0:no_target@35
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@68; play0/1:dropped@69; prep1/0:no_object@0; play1/0:no_target@45
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:done@54; play0/1:dropped@55; play0/1:dropped@61; prep1/0:no_object@0; play1/0:no_target@35
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:no_target@53; play0/1:dropped@54; prep1/0:no_object@0; play1/0:done@65
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.44, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; play0/0:dropped@32; play0/0:done@44; play0/1:dropped@45; play0/1:no_object@45; prep1/0:no_object@0; play1/0:timeout@68