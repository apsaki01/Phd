# Rehearsal feedback — iteration 14 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.0, 'damp': 0.5, 'tol': 0.3, 'offset': 0.15, 'seg_timeout': 30.0}
  role0 prep: [when doors_sealed] grab box to door_block[yaw0,direct] lock release | play: stay then [when opponent_visible] to stay[align,direct]
  role1 prep: [when teammate_inside] grab ramp to ramp_inside[yaw2,direct] lock release | play: stay then [when opponent_visible] to climb[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.197
- hider win-rate: 0.17
- behaviour detection rates: {"chasing": 0.0, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 34.8
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.57, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 56 (hider outside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 36 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 38 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@30; prep1/0:timeout@30