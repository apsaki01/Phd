# Rehearsal feedback — iteration 183 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.0, 'damp': 0.42, 'tol': 0.23, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase then grab ramp to away_from_opponent[yaw0,direct] lock -> grab box to climb[target,direct]
  role1 prep: (none) | play: chase then grab box to away_from_opponent[yaw0,direct] lock -> [when ramp_inside] grab box to ramp[yaw2,door] release -> grab box to climb[target,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.479
- hider win-rate: 0.47
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 42.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.50, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.14, 1.71] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.37, 1.47] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.54, 1.39] | seeker 2 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.89, 1.87] | seeker 2 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.65, 0.19] | seeker 2 saw hider 1 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.93, 0.94] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.81, 0.86] | seeker 2 saw hider 1 at play step 46 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[2.36, 1.96] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed