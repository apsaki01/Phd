# Rehearsal feedback — iteration 15 — learning team: seeker

## Current graph
```
assign=fixed params={'gain': 4.9, 'damp': 0.5, 'tol': 0.3, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: (none) | play: flee then grab ramp to quadrant_corner[target,direct]
  role1 prep: (none) | play: chase
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.154
- hider win-rate: 0.00
- behaviour detection rates: {"chasing": 0.07, "door_blocking": 0.03, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.6
- doors sealed+locked at prep end: 0.03, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.72, mean max seeker z: 0.17

## Failure analysis (lost instances)