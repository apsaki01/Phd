# Rehearsal feedback — iteration 273 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.77, 'damp': 0.38, 'tol': 0.27, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then grab ramp to door_block[yaw0,door] release -> to quadrant_corner[target,door]
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.583
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.5
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.28, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.52, 1.73] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[2.25, 0.98] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.42, 0.47] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.29, 0.97] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.38, 0.73] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.1, 0.33] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.68, 0.41] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.2, 1.15] | hiders never seen | segments: no segments executed