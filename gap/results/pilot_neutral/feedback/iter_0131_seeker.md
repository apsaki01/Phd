# Rehearsal feedback — iteration 131 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.43, 'damp': 0.7, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.187
- hider win-rate: 0.15
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.4
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.93, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.31, 0.17] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.05, 0.59] | seeker 2 saw hider 0 at play step 80 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.85, 1.06] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.35, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed