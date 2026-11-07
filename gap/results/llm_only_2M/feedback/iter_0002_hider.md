# Rehearsal feedback — iteration 2 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 5.0, 'damp': 0.8, 'tol': 0.4, 'offset': 0.2, 'seg_timeout': 20.0}
  role0 prep: [when ramp_inside] grab ramp to wander[yaw0,direct] lock | play: search then [when doors_sealed] grab box to stay[align,door] release
  role1 prep: [when doors_sealed] grab box to wander[yaw1,direct] lock | play: go(outside_wall,direct) then [when ramp_inside] grab ramp to stay[yaw2,door] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.355
- hider win-rate: 0.40
- behaviour detection rates: {"chasing": 0.0, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.6
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.00, mean max seeker z: 0.15

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.29, 1.09] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:timeout@20; prep0/0:done@7
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:timeout@20; prep0/0:timeout@20
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@20; prep1/0:timeout@20
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:timeout@20; prep0/0:timeout@20
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.41, 0.0] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@20; prep1/0:timeout@20
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@20; prep1/0:timeout@20
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@20; prep1/0:timeout@20
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:timeout@20; prep1/0:timeout@20