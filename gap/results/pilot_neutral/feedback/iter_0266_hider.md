# Rehearsal feedback — iteration 266 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.595
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.55, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.5
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.33, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.51, 0.48] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep0/1:done@20; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.07, 0.15] | seeker 2 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@10; prep0/1:dropped@11; prep0/1:no_target@13; prep1/0:done@12; prep1/1:dropped@13; prep1/1:done@16
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.42, 1.6] | seeker 3 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.64, 0.73] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:done@25; prep1/0:done@21; prep1/1:dropped@22; prep1/1:done@25
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.47, 1.5] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:dropped@23; prep1/0:no_target@20; prep1/1:dropped@21; prep1/1:no_target@22
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.02, 2.33] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@31; prep1/0:dropped@15; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@25
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.94, 2.21] | seeker 2 saw hider 1 at play step 37 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@19; prep1/0:no_target@21; prep1/1:dropped@22; prep1/1:no_target@23
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.66, 0.47] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed