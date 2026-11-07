# Rehearsal feedback — iteration 235 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.63, 'damp': 0.4, 'tol': 0.3, 'offset': 0.25, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock
  role1 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw2,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.554
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.7, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 37.6
- doors sealed+locked at prep end: 0.72, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.07, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.37, 0.6] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.99, 0.76] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.33, 0.97] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.56, 1.77] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.26, 0.75] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.15, 0.92] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.94] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.56, 2.07] | hiders never seen | segments: no segments executed