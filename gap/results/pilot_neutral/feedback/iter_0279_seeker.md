# Rehearsal feedback — iteration 279 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 3.17, 'damp': 0.38, 'tol': 0.23, 'offset': 0.31, 'seg_timeout': 26.67}
  role0 prep: (none) | play: chase then to climb[align,direct] release
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.556
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.57, "ramp_use": 0.0, "ramp_defense": 0.04}
- mean first-seen play step: 37.6
- doors sealed+locked at prep end: 0.66, ramp inside quadrant at prep end: 0.30
- seekers entered quadrant: 0.38, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.53, 1.8] | hiders never seen | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.86, 0.65] | hiders never seen | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.44, 1.03] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[2.01, 1.55] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.26, 2.81] | hiders never seen | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.75, 0.92] | seeker 2 saw hider 0 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.62, 1.58] | seeker 3 saw hider 1 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.96, 1.54] | hiders never seen | segments: no segments executed