# Rehearsal feedback — iteration 262 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.666
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.3, "door_blocking": 0.75, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.8
- doors sealed+locked at prep end: 0.78, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.10, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.77, 1.08] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:done@16; prep1/0:done@21; prep1/1:dropped@22; prep1/1:done@27
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.96, 1.35] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep0/1:dropped@22; prep0/1:done@25; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@17
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.98, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@9; prep1/1:dropped@10; prep1/1:done@13
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.74, 0.0] | seeker 2 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:no_target@10; prep1/1:dropped@11; prep1/1:no_target@12
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.65, 1.34] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.73, 2.76] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@7; prep0/0:dropped@12; prep0/0:dropped@16; prep0/0:done@23; prep0/1:dropped@24; prep0/1:done@29; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.36, 1.03] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@30; prep0/1:dropped@31; prep1/0:done@22; prep1/1:dropped@23; prep1/1:done@27
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[3.87, 1.53] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@23; prep0/1:dropped@24; prep0/1:no_target@27; prep1/0:done@16; prep1/1:dropped@17; prep1/1:dropped@24