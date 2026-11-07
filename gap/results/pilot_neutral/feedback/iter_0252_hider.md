# Rehearsal feedback — iteration 252 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> [when doors_sealed] grab box to wander[yaw2,direct] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.578
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.62, "ramp_use": 0.03, "ramp_defense": 0.0}
- mean first-seen play step: 36.0
- doors sealed+locked at prep end: 0.66, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.30, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.59, 1.39] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10; prep1/0:no_target@16; prep1/1:dropped@17
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 1.35] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.06, 0.0] | seeker 2 saw hider 0 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.81, 0.36] | hiders never seen | segments: prep0/0:no_target@8; prep0/1:dropped@9; prep0/1:no_target@12; prep1/0:done@14; prep1/1:dropped@15; prep1/1:done@18
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.94, 0.7] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:done@12; prep1/0:done@6; prep1/1:dropped@7; prep1/1:done@17
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.57, 1.7] | hiders never seen | segments: prep0/0:done@22; prep0/1:dropped@23; prep0/1:done@26; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@17
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[2.32, 2.45] | seeker 2 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@23; prep0/0:done@31
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.41, 1.12] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.61) | segments: prep0/0:dropped@6; prep0/0:dropped@8; prep0/0:done@24; prep0/1:dropped@25; prep0/1:done@28; prep1/0:done@31