# Rehearsal feedback — iteration 181 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.0, 'damp': 0.44, 'tol': 0.35, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase then grab ramp to away_from_opponent[yaw0,direct] lock -> [when ramp_inside] grab box to ramp[yaw2,door] release -> grab box to climb[target,direct]
  role1 prep: (none) | play: chase then grab ramp to away_from_opponent[yaw0,direct] lock -> [when ramp_inside] grab box to ramp[yaw2,door] release -> grab box to climb[target,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.535
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.23, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 39.9
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.45, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.97, 0.64] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.7, 0.31] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.63, 0.11] | seeker 2 saw hider 0 at play step 44 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.01, 1.03] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.47, 2.58] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.74, 1.51] | seeker 3 saw hider 1 at play step 77 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.28, 0.19] | seeker 3 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.07, 0.45] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed