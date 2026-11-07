# Rehearsal feedback — iteration 294 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.75, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.614
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.0
- doors sealed+locked at prep end: 0.70, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.35, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.62, 1.86] | seeker 2 saw hider 1 at play step 47 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.35, 1.78] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; prep0/1:dropped@24; prep0/1:no_target@27; prep1/0:done@15; prep1/1:dropped@16
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.6, 0.59] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:no_target@22; prep1/0:done@12; prep1/1:dropped@13; prep1/1:done@22
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.9, 1.1] | seeker 3 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:done@20; prep1/0:dropped@8; prep1/0:done@19; prep1/1:dropped@20; prep1/1:no_target@21
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.3, 1.43] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:done@22; prep1/0:done@15; prep1/1:dropped@16; prep1/1:no_target@18
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.58, 1.97] | seeker 2 saw hider 1 at play step 54 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep0/1:dropped@22; prep0/1:no_target@28; prep1/0:done@9; prep1/1:dropped@10; prep1/1:done@28
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.66, 0.94] | seeker 3 saw hider 0 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:dropped@11; prep0/1:done@26; prep1/0:done@23; prep1/1:dropped@24
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.3, 1.3] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@7; prep0/1:dropped@8; prep1/0:done@9; prep1/1:dropped@10; prep1/1:dropped@27