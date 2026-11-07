# Rehearsal feedback — iteration 355 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.89, 'damp': 0.69, 'tol': 0.35, 'offset': 0.21, 'seg_timeout': 26.66}
  role0 prep: (none) | play: go(climb,door) then grab box to box[yaw0,door] lock
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.656
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.9
- doors sealed+locked at prep end: 0.64, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.40, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.08, 2.11] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.69, 1.19] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.71, 2.64] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.58, 1.78] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.16, 1.35] | seeker 3 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.95, 0.65] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.82, 2.59] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.31, 0.6] | hiders never seen | segments: no segments executed