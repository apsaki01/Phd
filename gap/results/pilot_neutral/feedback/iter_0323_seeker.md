# Rehearsal feedback — iteration 323 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.5, 'tol': 0.35, 'offset': 0.19, 'seg_timeout': 26.66}
  role0 prep: (none) | play: search then grab box to door_block[yaw0,direct] -> to teammate[yaw2,door] release -> grab box to teammate[yaw3,door] -> [when doors_sealed] grab box to quadrant_interior[yaw0,door]
  role1 prep: (none) | play: chase then to opponent[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.470
- hider win-rate: 0.45
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 40.6
- doors sealed+locked at prep end: 0.68, ramp inside quadrant at prep end: 0.10
- seekers entered quadrant: 0.35, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.87, 2.49] | seeker 2 saw hider 0 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.44, 1.82] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.15, 1.42] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.0, 1.11] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.07, 2.47] | seeker 3 saw hider 0 at play step 54 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.94, 1.18] | seeker 2 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.3, 0.63] | seeker 2 saw hider 0 at play step 65 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.33, 1.27] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed