# Rehearsal feedback — iteration 215 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.19, 'seg_timeout': 28.17}
  role0 prep: (none) | play: chase
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.620
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.25, "door_blocking": 0.47, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 39.0
- doors sealed+locked at prep end: 0.50, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.28, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.77, 0.52] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.01, 0.13] | seeker 2 saw hider 1 at play step 56 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.71, 1.86] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.76, 0.43] | seeker 3 saw hider 1 at play step 38 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.17, 1.19] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.04, 1.65] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.94, 2.38] | seeker 3 saw hider 1 at play step 58 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.78, 0.16] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed