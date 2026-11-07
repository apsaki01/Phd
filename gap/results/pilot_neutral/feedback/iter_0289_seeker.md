# Rehearsal feedback — iteration 289 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.17, 'damp': 0.31, 'tol': 0.23, 'offset': 0.44, 'seg_timeout': 26.67}
  role0 prep: (none) | play: search then grab ramp to door_block[target,direct] lock release
  role1 prep: (none) | play: chase then [when ramp_inside] grab box to ramp_inside[yaw3,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.613
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.5, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 40.9
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.42, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.74, 1.01] | seeker 2 saw hider 0 at play step 50 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.05, 1.13] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.58, 1.86] | seeker 2 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.27, 1.92] | seeker 3 saw hider 1 at play step 62 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.26, 1.51] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.17, 1.9] | seeker 2 saw hider 1 at play step 50 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.75, 2.11] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.35, 0.51] | hiders never seen | segments: no segments executed