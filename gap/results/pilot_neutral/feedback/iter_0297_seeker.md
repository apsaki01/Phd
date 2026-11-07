# Rehearsal feedback — iteration 297 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 1.99, 'damp': 0.31, 'tol': 0.21, 'offset': 0.54, 'seg_timeout': 26.67}
  role0 prep: (none) | play: search then grab ramp to door_block[target,direct] lock release -> grab ramp to quadrant_corner[yaw3,direct] release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.535
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.28, "door_blocking": 0.47, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.0
- doors sealed+locked at prep end: 0.57, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.45, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.46, 1.22] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.1, 1.53] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.0, 1.35] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.82, 0.65] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.54, 1.02] | seeker 3 saw hider 0 at play step 52 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.55, 1.23] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.91, 2.38] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.12, 2.13] | hiders never seen | segments: no segments executed