# Rehearsal feedback — iteration 243 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 3.5, 'damp': 0.4, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door]
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.618
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 38.6
- doors sealed+locked at prep end: 0.64, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.28, mean max seeker z: 0.15

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.07, 2.08] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.03, 0.0] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.65, 0.47] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.91, 1.11] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.01, 1.19] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.46, 0.64] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.13, 1.92] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.53, 0.63] | hiders never seen | segments: no segments executed