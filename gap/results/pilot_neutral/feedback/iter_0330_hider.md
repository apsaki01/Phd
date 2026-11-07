# Rehearsal feedback — iteration 330 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.05, 'seg_timeout': 38.08}
  role0 prep: grab box to door_block[target,door] lock release -> grab box to ramp_inside[yaw2,door] | play: chase then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: flee then grab box to ramp_inside[target,door] lock -> [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to stay[yaw3,door] lock -> grab ramp to quadrant_interior[align,direct]
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.447
- hider win-rate: 0.45
- behaviour detection rates: {"chasing": 0.03, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 36.1
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.33, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.59, 1.22] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@26; prep0/1:dropped@27; prep1/0:no_target@19; prep1/1:dropped@20; prep1/1:done@25
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.57, 1.71] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@6; prep0/0:done@17; prep0/1:dropped@18; prep1/0:no_target@6; prep1/1:dropped@7; prep1/1:done@13
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.73, 2.35] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@16; prep0/1:dropped@17
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.1, 0.7] | seeker 3 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@5
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.66, 1.0] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@9; prep0/1:dropped@10
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.87, 1.58] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@9; prep0/1:dropped@10; prep1/0:dropped@6
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.82, 2.2] | hiders never seen | segments: prep0/0:done@26; prep0/1:dropped@27; prep0/1:no_object@27; prep1/0:no_target@20; prep1/1:dropped@21; prep1/1:done@28
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.82, 0.72] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:no_target@15; prep1/1:dropped@16