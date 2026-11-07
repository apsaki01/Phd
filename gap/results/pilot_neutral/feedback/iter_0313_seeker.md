# Rehearsal feedback — iteration 313 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.5, 'tol': 0.3, 'offset': 0.15, 'seg_timeout': 24.98}
  role0 prep: (none) | play: chase then [when doors_sealed] grab box to quadrant_interior[yaw0,door] release
  role1 prep: (none) | play: chase then [when doors_sealed] grab box to quadrant_interior[yaw0,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.672
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.9
- doors sealed+locked at prep end: 0.69, ramp inside quadrant at prep end: 0.07
- seekers entered quadrant: 0.25, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.56, 1.17] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.55, 1.55] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.43, 0.58] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.47, 0.92] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.19, 0.98] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.21, 0.7] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.45, 1.96] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.18, 1.68] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed