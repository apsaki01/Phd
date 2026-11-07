# Rehearsal feedback — iteration 119 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.43, 'damp': 0.7, 'tol': 0.25, 'offset': 0.2, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase then [when doors_sealed] to ramp[yaw3,door] lock release
  role1 prep: (none) | play: chase then [when opponent_visible] to outside_wall[yaw0,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.286
- hider win-rate: 0.17
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.31}
- mean first-seen play step: 34.8
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.45
- seekers entered quadrant: 0.88, mean max seeker z: 0.22

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 50 (hider outside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.71] | hiders never seen | segments: no segments executed