# Rehearsal feedback — iteration 309 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 1.99, 'damp': 0.31, 'tol': 0.21, 'offset': 0.54, 'seg_timeout': 30.57}
  role0 prep: (none) | play: search then to ramp[yaw2,door] -> grab ramp to quadrant_interior[target,door] release
  role1 prep: (none) | play: chase then to away_from_opponent[yaw2,door] -> grab box to quadrant_interior[target,door] release -> to quadrant_interior[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.507
- hider win-rate: 0.47
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.2
- doors sealed+locked at prep end: 0.64, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.45, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.85, 0.74] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.84, 2.43] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.09, 1.04] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.91, 2.61] | seeker 3 saw hider 0 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.01, 1.28] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.54, 0.63] | seeker 2 saw hider 1 at play step 62 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.03, 0.76] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.15, 0.64] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed