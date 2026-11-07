# Rehearsal feedback — iteration 275 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 3.17, 'damp': 0.38, 'tol': 0.23, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then to quadrant_corner[target,door] -> grab ramp to door_block[yaw0,door] release -> to climb[align,direct] release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.417
- hider win-rate: 0.42
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.8
- doors sealed+locked at prep end: 0.62, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.40, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.45, 0.14] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.39, 1.53] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.92, 1.63] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.36, 2.03] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.32, 0.97] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.73, 0.86] | seeker 3 saw hider 1 at play step 72 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.97, 1.28] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.77, 1.31] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: no segments executed