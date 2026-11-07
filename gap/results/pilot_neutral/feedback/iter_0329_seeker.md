# Rehearsal feedback — iteration 329 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.0, 'damp': 0.5, 'tol': 0.35, 'offset': 0.22, 'seg_timeout': 26.66}
  role0 prep: (none) | play: search then grab box to door_block[yaw0,direct] -> to teammate[yaw2,door] release -> [when doors_sealed] grab box to quadrant_interior[yaw0,door]
  role1 prep: (none) | play: chase then to opponent[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.563
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.78, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.1
- doors sealed+locked at prep end: 0.81, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.20, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.14, 0.71] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.89, 1.85] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.88, 1.62] | seeker 3 saw hider 1 at play step 56 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.25, 2.22] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.49, 1.97] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.62, 0.64] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.82, 0.88] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.13, 2.42] | hiders never seen | segments: no segments executed