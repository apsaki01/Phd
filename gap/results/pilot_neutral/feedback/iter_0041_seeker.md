# Rehearsal feedback — iteration 41 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.9, 'damp': 0.5, 'tol': 0.27, 'offset': 0.15, 'seg_timeout': 30.26}
  role0 prep: (none) | play: flee then [when door] to opponent[yaw2,door] -> grab box to ramp[target,door] lock release -> grab ramp to quadrant_corner[target,direct] -> [when opponent_visible] to outside_wall[yaw0,direct] release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.190
- hider win-rate: 0.07
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.12}
- mean first-seen play step: 35.1
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.70, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.65] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.41] | seeker 3 saw hider 1 at play step 37 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.54] | seeker 3 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed