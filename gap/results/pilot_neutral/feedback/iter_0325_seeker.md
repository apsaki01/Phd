# Rehearsal feedback — iteration 325 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.5, 'tol': 0.35, 'offset': 0.19, 'seg_timeout': 26.66}
  role0 prep: (none) | play: search then grab box to door_block[yaw0,direct] -> to teammate[yaw2,door] release -> grab box to teammate[yaw3,door] -> [when doors_sealed] grab box to quadrant_interior[yaw0,door]
  role1 prep: (none) | play: chase then to opponent[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.625
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.5, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.9
- doors sealed+locked at prep end: 0.59, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.40, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.21, 1.87] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.7, 0.57] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.68, 0.96] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[1.36, 1.38] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.99, 1.16] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.58, 0.25] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.84, 1.55] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.96, 1.51] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed