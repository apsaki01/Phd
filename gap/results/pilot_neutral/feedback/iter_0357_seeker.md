# Rehearsal feedback — iteration 357 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 6.0, 'damp': 0.5, 'tol': 0.25, 'offset': 0.3, 'seg_timeout': 30.0}
  role0 prep: (none) | play: search then [when door] grab box to door_block[target,direct] lock
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.409
- hider win-rate: 0.35
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.42, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 36.8
- doors sealed+locked at prep end: 0.54, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.57, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.26, 2.45] | hiders never seen | segments: no segments executed
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.45, 1.16] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.85, 2.53] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.63, 2.09] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.18, 2.11] | seeker 2 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.72, 2.17] | hiders never seen | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.37, 1.11] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.24, 1.98] | seeker 2 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed