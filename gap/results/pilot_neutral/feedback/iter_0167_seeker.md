# Rehearsal feedback — iteration 167 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 5.0, 'damp': 0.44, 'tol': 0.35, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase then grab ramp to away_from_opponent[yaw0,direct] lock -> [when ramp_inside] grab box to ramp[yaw2,door] release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.341
- hider win-rate: 0.28
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.06}
- mean first-seen play step: 36.3
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.28
- seekers entered quadrant: 0.78, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.84, 1.55] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.35, 0.72] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.98, 0.89] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.69, 0.76] | seeker 2 saw hider 1 at play step 49 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.61, 1.56] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.55, 2.43] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.05, 0.86] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.79, 0.7] | hiders never seen | segments: no segments executed