# Rehearsal feedback — iteration 201 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 4.98, 'damp': 0.42, 'tol': 0.23, 'offset': 0.19, 'seg_timeout': 27.71}
  role0 prep: (none) | play: chase then [when opponent_visible] grab ramp to opponent[yaw0,direct] lock
  role1 prep: (none) | play: chase then grab ramp to opponent[yaw0,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.424
- hider win-rate: 0.40
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 42.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.75, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.85, 2.03] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.22, 0.07] | seeker 2 saw hider 0 at play step 77 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.13, 0.06] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.03, 2.14] | seeker 2 saw hider 1 at play step 79 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.22, 2.25] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.34, 1.49] | seeker 3 saw hider 0 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.0, 0.62] | seeker 2 saw hider 0 at play step 51 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.37, 1.57] | seeker 2 saw hider 1 at play step 74 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed