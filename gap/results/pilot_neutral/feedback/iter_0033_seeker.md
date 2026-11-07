# Rehearsal feedback — iteration 33 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.9, 'damp': 0.5, 'tol': 0.27, 'offset': 0.15, 'seg_timeout': 30.26}
  role0 prep: (none) | play: flee then [when door] to opponent[yaw2,door] -> grab box to ramp[target,door] lock release -> grab ramp to quadrant_corner[target,direct] -> [when opponent_visible] to outside_wall[yaw0,direct] release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.171
- hider win-rate: 0.03
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.14}
- mean first-seen play step: 34.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.82, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 65 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed