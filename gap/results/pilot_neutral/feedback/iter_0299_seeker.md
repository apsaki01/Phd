# Rehearsal feedback — iteration 299 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 1.99, 'damp': 0.31, 'tol': 0.21, 'offset': 0.54, 'seg_timeout': 26.67}
  role0 prep: (none) | play: search then [when doors_sealed] grab box to outside_wall[yaw1,door] release -> grab ramp to door_block[target,direct] lock release
  role1 prep: (none) | play: chase then to away_from_opponent[yaw2,door] -> grab box to quadrant_interior[target,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.535
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.4, "door_blocking": 0.47, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 40.9
- doors sealed+locked at prep end: 0.60, ramp inside quadrant at prep end: 0.07
- seekers entered quadrant: 0.45, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.27, 0.82] | seeker 2 saw hider 0 at play step 67 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.44, 1.79] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.07, 2.02] | seeker 2 saw hider 1 at play step 48 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.25, 1.06] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.53, 0.85] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.92, 0.63] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.4, 2.63] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.83, 1.58] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed