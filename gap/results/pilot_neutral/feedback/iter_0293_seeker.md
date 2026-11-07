# Rehearsal feedback — iteration 293 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 1.99, 'damp': 0.31, 'tol': 0.23, 'offset': 0.55, 'seg_timeout': 26.67}
  role0 prep: (none) | play: search then grab ramp to door_block[target,direct] lock release -> grab ramp to quadrant_corner[yaw0,direct] release
  role1 prep: (none) | play: chase then [when ramp_inside] grab box to ramp_inside[yaw3,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.565
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.6
- doors sealed+locked at prep end: 0.62, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.38, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.12, 0.83] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.36, 2.18] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.18, 0.94] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.86, 1.76] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.47, 1.41] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.29, 0.64] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.49, 1.58] | seeker 2 saw hider 0 at play step 52 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.58, 0.67] | hiders never seen | segments: no segments executed