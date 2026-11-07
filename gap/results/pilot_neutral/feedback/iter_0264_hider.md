# Rehearsal feedback — iteration 264 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.656
- hider win-rate: 0.70
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.68, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 35.9
- doors sealed+locked at prep end: 0.71, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.28, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.53, 1.58] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.27, 1.73] | seeker 3 saw hider 0 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep0/1:done@17; prep1/0:done@19; prep1/1:dropped@20; prep1/1:done@23
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.01, 1.24] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@13; prep0/0:done@20; prep0/1:dropped@21; prep0/1:done@27; prep1/0:dropped@16; prep1/0:dropped@19; prep1/0:done@25; prep1/1:dropped@26; prep1/1:done@29
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.21, 1.35] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; prep0/1:dropped@24; prep1/0:no_target@28; prep1/1:dropped@29; prep1/1:no_target@31
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.94, 0.54] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@11; prep0/1:dropped@12; prep0/1:no_target@13; prep1/0:done@12; prep1/1:dropped@13; prep1/1:done@19
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.98] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.35, 1.53] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@8
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 1.32] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed