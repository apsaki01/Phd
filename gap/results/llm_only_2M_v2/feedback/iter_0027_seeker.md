# Rehearsal feedback — iteration 27 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 5.0, 'damp': 0.6, 'tol': 0.25, 'offset': 0.2, 'seg_timeout': 35.0}
  role0 prep: (none) | play: search then [when doors_sealed] to door_block[target,direct]
  role1 prep: (none) | play: chase then [when doors_sealed] to door_block[target,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.092
- hider win-rate: 0.03
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.03, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 33.9
- doors sealed+locked at prep end: 0.03, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.95, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed