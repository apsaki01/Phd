# Rehearsal feedback — iteration 244 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.517
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.5, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.8
- doors sealed+locked at prep end: 0.56, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.33, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.99, 0.98] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@10; prep0/0:done@18; prep0/1:dropped@19; prep0/1:done@22; prep1/0:done@21; prep1/1:dropped@22; prep1/1:done@28
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.03, 1.0] | seeker 3 saw hider 1 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@17
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 37 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.02, 0.34] | seeker 3 saw hider 0 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@8; prep0/1:dropped@9; prep0/1:done@16
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.21, 1.56] | seeker 2 saw hider 0 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[2.41, 0.69] | seeker 3 saw hider 1 at play step 39 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; prep0/1:dropped@28; prep1/0:no_target@21; prep1/1:dropped@22
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.42, 1.42] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:done@24; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.23, 1.69] | seeker 2 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@29; prep0/1:dropped@30; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@17