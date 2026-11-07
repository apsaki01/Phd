# Rehearsal feedback — iteration 353 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.89, 'damp': 0.69, 'tol': 0.35, 'offset': 0.21, 'seg_timeout': 26.66}
  role0 prep: (none) | play: go(climb,door) then grab box to box[yaw0,door] lock
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.521
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.5, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.7
- doors sealed+locked at prep end: 0.62, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.42, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.36, 1.92] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.52, 1.6] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.12, 0.69] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.46, 0.12] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.28, 1.42] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.31, 1.94] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.18, 0.31] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.97, 1.14] | hiders never seen | segments: no segments executed