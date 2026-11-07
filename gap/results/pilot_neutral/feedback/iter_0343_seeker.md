# Rehearsal feedback — iteration 343 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.53, 'tol': 0.35, 'offset': 0.21, 'seg_timeout': 26.66}
  role0 prep: (none) | play: flee then grab ramp to teammate[yaw2,direct] release
  role1 prep: (none) | play: chase then grab ramp to wander[yaw0,door] lock release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.617
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 36.5
- doors sealed+locked at prep end: 0.70, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.33, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.56, 2.26] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.8, 1.01] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.04, 0.57] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.33, 2.32] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.59, 0.49] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.4, 0.49] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.36, 0.59] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[2.22, 0.52] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed