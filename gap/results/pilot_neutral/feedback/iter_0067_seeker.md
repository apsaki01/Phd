# Rehearsal feedback — iteration 67 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.0, 'damp': 0.6, 'tol': 0.3, 'offset': 0.2, 'seg_timeout': 20.0}
  role0 prep: (none) | play: chase then [when door] to door_block[yaw0,door] lock -> [when doors_sealed] grab box to ramp[yaw3,door] lock release -> [when ramp_inside] to quadrant_corner[target,direct]
  role1 prep: (none) | play: chase then [when door] to door_block[yaw0,door] lock -> [when doors_sealed] grab box to ramp[yaw3,door] lock release -> [when ramp_inside] to quadrant_corner[target,direct] -> [when opponent_visible] to outside_wall[yaw0,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.372
- hider win-rate: 0.45
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.06}
- mean first-seen play step: 35.8
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.28
- seekers entered quadrant: 0.72, mean max seeker z: 0.23

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 36 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 36 (hider outside quadrant, seeker outside, seeker z=0.16) | segments: no segments executed
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.44, 0.33] | seeker 2 saw hider 0 at play step 70 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | hiders never seen | segments: no segments executed