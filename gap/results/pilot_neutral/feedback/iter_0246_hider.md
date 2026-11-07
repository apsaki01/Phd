# Rehearsal feedback — iteration 246 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.549
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.2
- doors sealed+locked at prep end: 0.78, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.20, mean max seeker z: 0.15

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.17, 0.31] | seeker 3 saw hider 1 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@8; prep1/0:dropped@9
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.91, 0.86] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@21; prep0/1:dropped@22; prep0/1:no_target@23; prep1/0:done@21; prep1/1:dropped@22; prep1/1:done@28
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[2.19, 2.22] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep1/0:dropped@10; prep1/0:dropped@15; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.9, 2.28] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@12; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.58, 2.9] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; prep0/1:done@20; prep1/0:done@27; prep1/1:dropped@28; prep1/1:done@31
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.3, 0.16] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.56] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.62, 1.38] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10; prep1/0:no_target@24; prep1/1:dropped@25; prep1/1:no_target@26