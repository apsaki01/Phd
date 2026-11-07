# Rehearsal feedback — iteration 245 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.5, 'damp': 0.38, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door]
  role1 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.616
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.7, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 40.2
- doors sealed+locked at prep end: 0.75, ramp inside quadrant at prep end: 0.07
- seekers entered quadrant: 0.28, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.17, 0.85] | seeker 2 saw hider 0 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.99, 1.18] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.1, 1.44] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.83, 0.12] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.5, 1.13] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.67, 0.31] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.01, 0.81] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.18, 2.85] | hiders never seen | segments: no segments executed