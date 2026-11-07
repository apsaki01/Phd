# Rehearsal feedback — iteration 335 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.5, 'tol': 0.35, 'offset': 0.22, 'seg_timeout': 26.66}
  role0 prep: (none) | play: search then grab box to door_block[yaw0,direct] -> to teammate[yaw2,door] release
  role1 prep: (none) | play: chase then grab ramp to wander[yaw0,door] lock release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.532
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.9
- doors sealed+locked at prep end: 0.59, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.42, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.76, 0.79] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.38, 2.09] | seeker 2 saw hider 0 at play step 46 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[1.0, 2.03] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[2.37, 2.06] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.93, 1.59] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.69, 0.72] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.73, 1.41] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.18, 2.3] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed