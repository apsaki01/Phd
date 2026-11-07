# Rehearsal feedback — iteration 161 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 5.0, 'damp': 0.6, 'tol': 0.35, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: (none) | play: chase then grab ramp to away_from_opponent[yaw0,direct] lock -> [when ramp_inside] to ramp[yaw2,door] release
  role1 prep: (none) | play: chase then [when ramp_inside] grab ramp to ramp[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.278
- hider win-rate: 0.20
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 35.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.72, mean max seeker z: 0.19

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 1.14] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.14, 0.71] | seeker 2 saw hider 1 at play step 49 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 1.37] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.59, 0.41] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.9, 1.86] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.72, 1.35] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.52, 0.57] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.55, 1.28] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed