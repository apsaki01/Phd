# Rehearsal feedback — iteration 281 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 3.17, 'damp': 0.38, 'tol': 0.23, 'offset': 0.44, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.689
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.57, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.2
- doors sealed+locked at prep end: 0.64, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.25, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.83, 1.55] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.23, 0.56] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.83, 0.75] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.92, 1.83] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.83, 0.99] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.69, 1.94] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.54, 0.51] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.58, 0.67] | hiders never seen | segments: no segments executed