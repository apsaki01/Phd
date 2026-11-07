# Rehearsal feedback — iteration 341 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.53, 'tol': 0.35, 'offset': 0.21, 'seg_timeout': 26.66}
  role0 prep: (none) | play: go(climb,door) then grab ramp to teammate[yaw2,direct] release
  role1 prep: (none) | play: chase then grab ramp to wander[yaw0,door] lock release -> grab box to away_from_opponent[yaw0,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.750
- hider win-rate: 0.80
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.7
- doors sealed+locked at prep end: 0.79, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.15, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.25, 1.91] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.6, 2.11] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.01, 0.93] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.74, 2.15] | seeker 3 saw hider 0 at play step 60 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.21, 1.91] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.74, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.61, 0.07] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.71, 0.78] | hiders never seen | segments: no segments executed