# Rehearsal feedback — iteration 25 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.9, 'damp': 0.5, 'tol': 0.27, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: (none) | play: flee then [when door] to opponent[yaw2,door] -> grab ramp to quadrant_corner[target,direct]
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.162
- hider win-rate: 0.03
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.03, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 33.5
- doors sealed+locked at prep end: 0.03, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.68, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed