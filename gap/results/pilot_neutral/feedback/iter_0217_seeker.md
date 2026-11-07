# Rehearsal feedback — iteration 217 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.98, 'damp': 0.3, 'tol': 0.21, 'offset': 0.19, 'seg_timeout': 28.17}
  role0 prep: (none) | play: chase then grab ramp to door_inside[align,direct] lock release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.619
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.35, "door_blocking": 0.57, "ramp_use": 0.03, "ramp_defense": 0.0}
- mean first-seen play step: 40.4
- doors sealed+locked at prep end: 0.64, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.40, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.71, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.56, 2.59] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[2.58, 1.6] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.66, 1.08] | seeker 3 saw hider 1 at play step 37 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.4, 1.78] | seeker 2 saw hider 0 at play step 68 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.31, 1.17] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.53, 1.96] | seeker 2 saw hider 0 at play step 71 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.87, 0.93] | seeker 3 saw hider 1 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed