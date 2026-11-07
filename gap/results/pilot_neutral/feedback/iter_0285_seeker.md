# Rehearsal feedback — iteration 285 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.17, 'damp': 0.25, 'tol': 0.23, 'offset': 0.44, 'seg_timeout': 26.67}
  role0 prep: (none) | play: search
  role1 prep: (none) | play: chase then [when doors_sealed] to away_from_opponent[yaw1,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.498
- hider win-rate: 0.42
- behaviour detection rates: {"chasing": 0.4, "door_blocking": 0.4, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 41.1
- doors sealed+locked at prep end: 0.55, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.53, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.93, 1.28] | seeker 3 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.55, 0.2] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.58, 1.77] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.45, 1.85] | seeker 2 saw hider 0 at play step 63 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.44, 1.21] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.62, 2.31] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[1.45, 1.11] | seeker 2 saw hider 0 at play step 76 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.21, 1.13] | hiders never seen | segments: no segments executed