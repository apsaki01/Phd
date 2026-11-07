# Rehearsal feedback — iteration 256 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.604
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.55, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.0
- doors sealed+locked at prep end: 0.59, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.42, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.13, 0.68] | seeker 3 saw hider 0 at play step 51 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep0/0:done@21; prep0/1:dropped@22; prep0/1:done@25; prep1/0:no_target@15; prep1/1:dropped@16; prep1/1:no_target@17
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.46, 0.2] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@13; prep0/0:dropped@18; prep0/0:dropped@23; prep1/0:no_target@16; prep1/1:dropped@17; prep1/1:no_target@18
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.27, 0.13] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.74] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.57, 0.52] | seeker 3 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@8
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.91, 1.14] | seeker 3 saw hider 0 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep1/0:done@23; prep1/1:dropped@24; prep1/1:done@27
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[3.01, 2.47] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep0/1:dropped@24; prep1/0:no_target@18; prep1/1:dropped@19; prep1/1:no_target@28
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.97, 2.52] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@10