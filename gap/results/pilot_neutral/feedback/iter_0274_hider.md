# Rehearsal feedback — iteration 274 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.577
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.7
- doors sealed+locked at prep end: 0.71, ramp inside quadrant at prep end: 0.07
- seekers entered quadrant: 0.30, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 1.86] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.03, 1.7] | seeker 3 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@7
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.52, 1.82] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@7; prep0/1:dropped@8; prep0/1:no_target@9; prep1/0:dropped@8; prep1/0:done@18; prep1/1:dropped@19; prep1/1:done@23
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.8, 2.65] | seeker 3 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@14; prep0/1:dropped@15; prep0/1:no_target@19; prep1/0:done@18; prep1/1:dropped@19; prep1/1:done@22
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.96, 0.53] | seeker 2 saw hider 1 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:no_target@20; prep1/1:dropped@21; prep1/1:no_target@24
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[1.46, 0.75] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep0/1:dropped@19; prep0/1:done@22; prep1/0:done@25; prep1/1:dropped@26
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.04, 1.62] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@10; prep0/0:dropped@14; prep0/0:done@17; prep0/1:dropped@18; prep0/1:done@30; prep1/0:dropped@9; prep1/0:done@17; prep1/1:dropped@18; prep1/1:done@21
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.78, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@29; prep0/1:dropped@30