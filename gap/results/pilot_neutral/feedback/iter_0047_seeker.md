# Rehearsal feedback — iteration 47 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.0, 'damp': 0.6, 'tol': 0.3, 'offset': 0.2, 'seg_timeout': 20.0}
  role0 prep: (none) | play: search then [when door] to door_block[yaw0,door] -> [when doors_sealed] grab box to ramp[target,door] lock release -> [when ramp_inside] grab ramp to quadrant_corner[target,direct] -> [when opponent_visible] to outside_wall[yaw0,direct] release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.188
- hider win-rate: 0.10
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.0, "ramp_use": 0.05, "ramp_defense": 0.1}
- mean first-seen play step: 35.2
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.30
- seekers entered quadrant: 1.00, mean max seeker z: 0.22

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.57, 0.71] | seeker 3 saw hider 1 at play step 62 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed