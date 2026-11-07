# Rehearsal feedback — iteration 339 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.53, 'tol': 0.35, 'offset': 0.21, 'seg_timeout': 26.66}
  role0 prep: (none) | play: go(climb,door) then grab ramp to teammate[yaw2,direct] release
  role1 prep: (none) | play: chase then grab ramp to wander[yaw0,door] lock release -> grab box to away_from_opponent[yaw0,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.597
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.1
- doors sealed+locked at prep end: 0.68, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.38, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.63, 0.81] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.0, 1.82] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.24, 2.36] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.93, 1.1] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.03, 1.53] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.82, 0.98] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.25, 1.88] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.46, 1.42] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed