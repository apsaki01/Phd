# Rehearsal feedback — iteration 239 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.63, 'damp': 0.4, 'tol': 0.3, 'offset': 0.25, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock
  role1 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.627
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.28, "door_blocking": 0.85, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.0
- doors sealed+locked at prep end: 0.88, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.05, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.33, 1.64] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.47, 1.6] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.19, 1.41] | seeker 2 saw hider 1 at play step 60 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.73, 2.36] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.75, 1.25] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.3, 0.56] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.68, 1.38] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.83, 1.44] | hiders never seen | segments: no segments executed