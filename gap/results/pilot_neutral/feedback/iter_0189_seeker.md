# Rehearsal feedback — iteration 189 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.15, 'seg_timeout': 27.71}
  role0 prep: (none) | play: chase
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.468
- hider win-rate: 0.45
- behaviour detection rates: {"chasing": 0.28, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 40.9
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.78, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.13, 1.2] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.28, 2.05] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.83, 0.27] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[2.11, 0.96] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.69, 0.06] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.7, 2.44] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.86, 0.1] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.99, 0.06] | seeker 2 saw hider 1 at play step 80 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed