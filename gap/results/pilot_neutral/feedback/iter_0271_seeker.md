# Rehearsal feedback — iteration 271 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.77, 'damp': 0.38, 'tol': 0.27, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then grab ramp to door_block[yaw0,door] release -> to quadrant_corner[target,door]
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.613
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.9
- doors sealed+locked at prep end: 0.70, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.30, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.74, 1.31] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.89, 2.3] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.08, 1.35] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.25, 1.13] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.78, 0.65] | seeker 2 saw hider 0 at play step 50 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.14, 0.79] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.41, 0.73] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.16, 1.04] | hiders never seen | segments: no segments executed