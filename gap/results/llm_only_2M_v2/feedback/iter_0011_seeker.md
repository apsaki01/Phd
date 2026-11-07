# Rehearsal feedback — iteration 11 — learning team: seeker

## Current graph
```
assign=nearest_object params={'gain': 5.0, 'damp': 0.6, 'tol': 0.25, 'offset': 0.2, 'seg_timeout': 35.0}
  role0 prep: (none) | play: search then [when doors_sealed] to door_block[target,direct]
  role1 prep: (none) | play: chase then [when doors_sealed] to door_block[target,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.070
- hider win-rate: 0.00
- behaviour detection rates: {"chasing": 0.0, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.07}
- mean first-seen play step: 34.4
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.30
- seekers entered quadrant: 1.00, mean max seeker z: 0.18

## Failure analysis (lost instances)