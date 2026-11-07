# Rehearsal feedback — iteration 1 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.5, 'tol': 0.3, 'offset': 0.15, 'seg_timeout': 30}
  role0 prep: (none) | play: stay
  role1 prep: (none) | play: stay
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.458
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.0, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.1
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.00, mean max seeker z: 0.15

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.62] | seeker 2 saw hider 1 at play step 43 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.23, 0.06] | seeker 2 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | hiders never seen | segments: no segments executed