# Rehearsal feedback — iteration 97 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.5, 'damp': 0.7, 'tol': 0.25, 'offset': 0.2, 'seg_timeout': 30.0}
  role0 prep: (none) | play: search then [when opponent_visible] to outside_wall[yaw0,direct] release -> [when ramp_inside] to quadrant_corner[target,direct] -> [when door] to door_block[target,door] lock
  role1 prep: (none) | play: chase then [when doors_sealed] grab box to ramp[yaw3,door] lock release -> [when door] to door_block[target,door] lock -> [when opponent_visible] to outside_wall[yaw0,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.328
- hider win-rate: 0.28
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.34}
- mean first-seen play step: 36.5
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.47
- seekers entered quadrant: 1.00, mean max seeker z: 0.21

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.18] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 71 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 1.38] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.16, 0.0] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 1.22] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed