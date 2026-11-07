# Rehearsal feedback — iteration 321 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.5, 'tol': 0.35, 'offset': 0.19, 'seg_timeout': 26.66}
  role0 prep: (none) | play: chase then grab box to door_block[yaw0,direct] lock -> to teammate[yaw2,door] release -> [when doors_sealed] grab box to quadrant_interior[yaw0,door]
  role1 prep: (none) | play: chase then to teammate[yaw2,door] release -> [when doors_sealed] grab box to quadrant_interior[yaw0,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.705
- hider win-rate: 0.72
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.68, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 35.8
- doors sealed+locked at prep end: 0.79, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.17, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.07, 2.15] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.63, 2.06] | seeker 2 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.12, 0.09] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.59, 0.17] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.85, 2.03] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.0, 0.48] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.86, 1.64] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.63, 0.64] | hiders never seen | segments: no segments executed