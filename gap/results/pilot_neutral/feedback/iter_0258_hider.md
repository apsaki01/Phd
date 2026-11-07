# Rehearsal feedback — iteration 258 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.588
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 35.8
- doors sealed+locked at prep end: 0.71, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.33, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.69, 1.15] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:done@16; prep1/0:no_target@14; prep1/1:dropped@15; prep1/1:no_target@16
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.12, 0.03] | seeker 3 saw hider 1 at play step 49 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@12
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[1.47, 2.66] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep1/0:done@19; prep1/1:dropped@20; prep1/1:done@23
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.62, 1.59] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@26; prep0/1:dropped@27; prep0/1:done@30; prep1/0:done@16; prep1/1:dropped@17; prep1/1:done@20
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.32, 0.9] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@15; prep0/0:done@21; prep0/1:dropped@22; prep0/1:done@27; prep1/0:no_target@13; prep1/1:dropped@14; prep1/1:no_target@15
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.93, 0.3] | seeker 2 saw hider 1 at play step 44 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep1/0:no_target@13; prep1/1:dropped@14; prep1/1:no_target@15
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.67, 0.69] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@13; prep0/1:dropped@14; prep0/1:no_target@16; prep1/0:dropped@23; prep1/0:dropped@26; prep1/0:done@29; prep1/1:dropped@30
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.64, 0.72] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:done@12; prep1/0:done@16; prep1/1:dropped@17; prep1/1:done@27