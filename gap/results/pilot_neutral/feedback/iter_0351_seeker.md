# Rehearsal feedback — iteration 351 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.89, 'damp': 0.69, 'tol': 0.35, 'offset': 0.21, 'seg_timeout': 26.66}
  role0 prep: (none) | play: go(climb,door) then grab box to box[yaw0,door] lock
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.655
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.6
- doors sealed+locked at prep end: 0.75, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.25, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.02, 0.8] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.09, 1.39] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.08, 0.94] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.85, 2.12] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.61, 1.3] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.5, 1.41] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.64, 0.11] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.12, 1.61] | hiders never seen | segments: no segments executed