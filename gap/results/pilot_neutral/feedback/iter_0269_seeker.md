# Rehearsal feedback — iteration 269 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.77, 'damp': 0.38, 'tol': 0.27, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then grab ramp to teammate[yaw3,door] lock release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.611
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.0
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.25, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.54, 2.01] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.13, 1.89] | seeker 2 saw hider 1 at play step 73 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.54, 0.56] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[0.98, 2.64] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.87, 0.75] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.7, 1.91] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.69, 1.12] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[2.29, 1.24] | hiders never seen | segments: no segments executed