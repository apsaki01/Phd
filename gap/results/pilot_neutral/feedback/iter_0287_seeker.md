# Rehearsal feedback — iteration 287 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 3.17, 'damp': 0.25, 'tol': 0.23, 'offset': 0.44, 'seg_timeout': 26.67}
  role0 prep: (none) | play: search then grab ramp to door_block[target,direct] lock release
  role1 prep: (none) | play: chase then [when doors_sealed] to away_from_opponent[yaw1,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.566
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.45, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 37.6
- doors sealed+locked at prep end: 0.60, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.42, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.45, 0.24] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.0, 2.24] | seeker 2 saw hider 0 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.28, 0.95] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[2.02, 2.15] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.82, 1.76] | seeker 2 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.35, 1.25] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.61, 0.62] | seeker 3 saw hider 1 at play step 47 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.37, 0.86] | hiders never seen | segments: no segments executed