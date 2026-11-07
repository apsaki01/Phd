# Rehearsal feedback — iteration 303 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 1.99, 'damp': 0.31, 'tol': 0.21, 'offset': 0.54, 'seg_timeout': 30.57}
  role0 prep: (none) | play: search then to ramp[yaw2,door] -> grab box to quadrant_interior[target,door] release
  role1 prep: (none) | play: chase then to away_from_opponent[yaw2,door] -> grab box to quadrant_interior[target,door] release -> to quadrant_interior[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.645
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.28, "door_blocking": 0.8, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 41.3
- doors sealed+locked at prep end: 0.86, ramp inside quadrant at prep end: 0.07
- seekers entered quadrant: 0.15, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.82, 1.42] | seeker 3 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.76, 1.66] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.22, 0.85] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.37, 0.94] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.79, 0.77] | seeker 2 saw hider 0 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.58, 1.14] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.03, 0.61] | seeker 2 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.39, 1.19] | hiders never seen | segments: no segments executed