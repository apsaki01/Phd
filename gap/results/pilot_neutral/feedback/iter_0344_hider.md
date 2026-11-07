# Rehearsal feedback — iteration 344 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 38.08}
  role0 prep: grab box to climb[yaw1,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,direct] lock -> grab ramp to quadrant_interior[align,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.644
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.68, "ramp_use": 0.03, "ramp_defense": 0.0}
- mean first-seen play step: 38.1
- doors sealed+locked at prep end: 0.74, ramp inside quadrant at prep end: 0.30
- seekers entered quadrant: 0.23, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.04, 0.7] | seeker 2 saw hider 1 at play step 45 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@10; prep0/1:dropped@11; prep1/0:done@19; prep1/1:dropped@20; prep1/1:no_target@21
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.77, 0.59] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10; prep0/1:done@18; prep1/0:dropped@10; prep1/0:dropped@13; prep1/0:dropped@22; prep1/0:done@24; prep1/1:dropped@25
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.74, 0.51] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep1/0:done@21; prep1/1:dropped@22
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.41, 2.46] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10; prep0/1:done@20; prep1/0:done@18; prep1/1:dropped@19; prep1/1:no_target@28
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.28, 0.06] | hiders never seen | segments: prep0/0:done@16; prep0/1:dropped@17; prep0/1:done@28; prep1/0:done@18; prep1/1:dropped@19; prep1/1:no_target@25
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.09, 1.67] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:done@29; prep1/0:done@29; prep1/1:dropped@30
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[0.47, 1.72] | seeker 2 saw hider 1 at play step 46 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; prep0/1:dropped@11; prep0/1:done@28; prep1/0:dropped@23; prep1/0:dropped@26; prep1/0:done@31
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.0, 0.42] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; prep0/1:dropped@11; prep0/1:done@21; prep1/0:dropped@10; prep1/0:done@14; prep1/1:dropped@15; prep1/1:no_target@17