# Rehearsal feedback — iteration 283 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 3.17, 'damp': 0.38, 'tol': 0.23, 'offset': 0.44, 'seg_timeout': 26.67}
  role0 prep: (none) | play: search then to teammate[yaw3,direct] lock release
  role1 prep: (none) | play: chase then [when doors_sealed] to away_from_opponent[yaw1,direct] lock release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.593
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.57, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 40.4
- doors sealed+locked at prep end: 0.64, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.40, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.93, 1.91] | seeker 2 saw hider 0 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.91, 1.97] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.75, 1.15] | seeker 2 saw hider 1 at play step 61 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.39, 1.17] | seeker 2 saw hider 1 at play step 51 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.9, 0.84] | seeker 2 saw hider 1 at play step 43 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.04, 1.93] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.29, 1.95] | seeker 2 saw hider 1 at play step 46 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.35, 0.87] | hiders never seen | segments: no segments executed