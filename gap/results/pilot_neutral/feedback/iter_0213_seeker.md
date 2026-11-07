# Rehearsal feedback — iteration 213 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.19, 'seg_timeout': 28.17}
  role0 prep: (none) | play: chase
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.504
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.07, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.1
- doors sealed+locked at prep end: 0.26, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.72, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.52, 1.34] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.84, 1.36] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.44, 1.86] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.2, 2.53] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.96, 0.13] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.71, 0.87] | seeker 3 saw hider 1 at play step 42 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.53, 0.31] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.21, 1.99] | hiders never seen | segments: no segments executed