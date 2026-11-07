# Rehearsal feedback — iteration 241 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 3.5, 'damp': 0.4, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door]
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.627
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 36.4
- doors sealed+locked at prep end: 0.76, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.15, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.15, 2.26] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.25, 0.97] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.62, 0.53] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.13, 1.17] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.78, 1.59] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.91, 2.09] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.47, 1.25] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.47, 2.08] | hiders never seen | segments: no segments executed