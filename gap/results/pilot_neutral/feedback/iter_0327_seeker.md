# Rehearsal feedback — iteration 327 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.0, 'damp': 0.5, 'tol': 0.35, 'offset': 0.22, 'seg_timeout': 26.66}
  role0 prep: (none) | play: search then grab box to door_block[yaw0,direct] -> to teammate[yaw2,door] release -> [when doors_sealed] grab box to quadrant_interior[yaw0,door]
  role1 prep: (none) | play: chase then to opponent[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.452
- hider win-rate: 0.40
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.57, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 35.5
- doors sealed+locked at prep end: 0.66, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.33, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.51, 1.15] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.35, 1.37] | seeker 3 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.32, 2.77] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.83, 0.89] | seeker 3 saw hider 0 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[2.43, 0.8] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.05, 1.47] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.13, 1.24] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.96, 2.14] | hiders never seen | segments: no segments executed