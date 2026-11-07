# Rehearsal feedback — iteration 249 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 3.5, 'damp': 0.38, 'tol': 0.3, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then [when ramp_inside] to teammate[yaw1,door] release
  role1 prep: (none) | play: chase then grab box to door_block[yaw0,direct] lock release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.532
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.1
- doors sealed+locked at prep end: 0.65, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.23, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.84, 0.72] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.23, 1.95] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[2.65, 1.23] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.31, 2.34] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.63, 2.01] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.27, 2.46] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.88, 0.67] | seeker 2 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.1, 0.64] | hiders never seen | segments: no segments executed