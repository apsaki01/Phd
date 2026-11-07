# Rehearsal feedback — iteration 171 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 5.0, 'damp': 0.44, 'tol': 0.35, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase then grab ramp to away_from_opponent[yaw0,direct] lock -> [when ramp_inside] grab box to ramp[yaw2,door] release -> grab box to climb[target,direct]
  role1 prep: (none) | play: chase then grab ramp to away_from_opponent[yaw0,direct] lock -> [when ramp_inside] grab box to ramp[yaw2,door] release -> grab box to climb[target,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.322
- hider win-rate: 0.25
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 37.9
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.70, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.88, 1.28] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.78, 1.35] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.32, 0.18] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.1, 1.82] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.11, 1.07] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.02, 0.26] | seeker 2 saw hider 1 at play step 48 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.97, 0.18] | seeker 2 saw hider 1 at play step 64 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.32, 0.23] | hiders never seen | segments: no segments executed