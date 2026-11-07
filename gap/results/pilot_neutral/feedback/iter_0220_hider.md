# Rehearsal feedback — iteration 220 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 38.83}
  role0 prep: grab box to door_block[target,door] lock | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[target,door] lock -> [when teammate_inside] grab ramp to away_from_opponent[yaw0,door] lock release | play: segments then grab box to stay[yaw3,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.662
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.8, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.8
- doors sealed+locked at prep end: 0.86, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.17, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.24, 1.57] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker inside, seeker z=0.16) | segments: play0/0:timeout@70; play0/1:dropped@71; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@78
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.78, 0.65] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; prep1/0:done@19; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@72
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.37, 0.65] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@38; prep1/0:dropped@12; prep1/0:done@24; play1/0:timeout@70; play1/1:dropped@71
- p_door=0.75 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.36, 0.41] | seeker 3 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; play0/1:done@74; prep1/0:done@16; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@72
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.21, 2.12] | seeker 2 saw hider 1 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@34; prep1/0:done@20; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@72
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[0.45, 0.99] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: play0/0:timeout@70; play0/1:dropped@71; prep1/0:done@13; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.39, 0.09] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@15; play0/0:dropped@32; play0/0:no_object@32; play0/1:no_target@33; prep1/0:done@16; play1/0:timeout@70; play1/1:dropped@71
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.7, 1.81] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@9; play0/0:dropped@32; play0/0:timeout@70; play0/1:no_target@71; prep1/0:done@12; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@74