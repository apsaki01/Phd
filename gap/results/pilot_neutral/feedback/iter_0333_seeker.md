# Rehearsal feedback — iteration 333 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.0, 'damp': 0.5, 'tol': 0.35, 'offset': 0.22, 'seg_timeout': 26.66}
  role0 prep: (none) | play: search then grab box to door_block[yaw0,direct] -> to teammate[yaw2,door] release -> [when doors_sealed] grab box to quadrant_interior[yaw0,door]
  role1 prep: (none) | play: chase then to opponent[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.644
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.7, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.4
- doors sealed+locked at prep end: 0.75, ramp inside quadrant at prep end: 0.05
- seekers entered quadrant: 0.30, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.96, 1.47] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.46, 2.08] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.12, 1.51] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.17, 1.35] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.45, 1.21] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.51, 1.22] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.1, 1.27] | seeker 3 saw hider 0 at play step 47 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.96, 2.05] | hiders never seen | segments: no segments executed