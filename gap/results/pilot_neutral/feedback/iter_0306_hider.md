# Rehearsal feedback — iteration 306 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 39.53}
  role0 prep: grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.580
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.28, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 39.5
- doors sealed+locked at prep end: 0.72, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.33, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.65, 1.62] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@31; prep1/0:dropped@30
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.28, 1.71] | seeker 3 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@18; prep0/0:done@27; prep1/0:done@18; prep1/1:dropped@19; prep1/1:dropped@21
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.73, 1.91] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@31; prep1/0:done@15; prep1/1:dropped@16
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.0, 1.64] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@3; prep0/0:done@12
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.04, 0.47] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep1/0:done@6; prep1/1:dropped@7; prep1/1:no_target@8
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.81, 0.97] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep1/0:done@9; prep1/1:dropped@10; prep1/1:done@25
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.64, 1.57] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@15; prep1/0:dropped@8; prep1/0:done@10; prep1/1:dropped@11; prep1/1:done@21
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.14, 1.27] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@25