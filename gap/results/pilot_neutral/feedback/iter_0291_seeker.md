# Rehearsal feedback — iteration 291 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 1.99, 'damp': 0.31, 'tol': 0.23, 'offset': 0.55, 'seg_timeout': 26.67}
  role0 prep: (none) | play: search then grab ramp to door_block[target,direct] lock release -> grab ramp to quadrant_corner[yaw0,direct] release
  role1 prep: (none) | play: chase then [when ramp_inside] grab box to ramp_inside[yaw3,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.569
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.23, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 43.0
- doors sealed+locked at prep end: 0.71, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.38, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.1, 0.82] | seeker 2 saw hider 1 at play step 66 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.43, 1.92] | seeker 2 saw hider 0 at play step 72 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[2.73, 1.06] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.94, 0.83] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.91, 2.26] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.67, 0.67] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.21, 1.12] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.02, 1.1] | hiders never seen | segments: no segments executed