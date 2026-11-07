# Rehearsal feedback — iteration 331 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.0, 'damp': 0.5, 'tol': 0.35, 'offset': 0.22, 'seg_timeout': 26.66}
  role0 prep: (none) | play: search then grab box to door_block[yaw0,direct] -> to teammate[yaw2,door] release -> [when doors_sealed] grab box to quadrant_interior[yaw0,door]
  role1 prep: (none) | play: chase then to opponent[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.524
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.8
- doors sealed+locked at prep end: 0.74, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.28, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.7, 1.55] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.29, 2.15] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.66, 1.55] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.46, 0.97] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.67, 2.71] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.82, 1.02] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.8, 0.6] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.37, 1.4] | hiders never seen | segments: no segments executed