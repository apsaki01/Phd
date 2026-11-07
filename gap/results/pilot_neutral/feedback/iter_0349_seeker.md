# Rehearsal feedback — iteration 349 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.89, 'damp': 0.61, 'tol': 0.35, 'offset': 0.21, 'seg_timeout': 26.66}
  role0 prep: (none) | play: go(climb,direct) then grab box to box[yaw0,door] lock
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.705
- hider win-rate: 0.72
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.85, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.9
- doors sealed+locked at prep end: 0.90, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.10, mean max seeker z: 0.15

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.84, 2.31] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.34, 1.19] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.69, 2.12] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.95, 1.73] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.96, 1.68] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.25, 2.35] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.64, 2.55] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.78, 1.6] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed