# Rehearsal feedback — iteration 317 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.5, 'tol': 0.3, 'offset': 0.15, 'seg_timeout': 26.66}
  role0 prep: (none) | play: chase then to teammate[yaw2,door] release -> [when doors_sealed] grab box to quadrant_interior[yaw0,door]
  role1 prep: (none) | play: chase then to teammate[yaw2,door] release -> [when doors_sealed] grab box to quadrant_interior[yaw0,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.607
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.7, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 37.4
- doors sealed+locked at prep end: 0.78, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.20, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.17, 0.79] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.03, 0.41] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.32, 0.09] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.99, 1.33] | seeker 3 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.58, 2.19] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.6, 1.76] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.04, 2.48] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.98, 0.18] | hiders never seen | segments: no segments executed