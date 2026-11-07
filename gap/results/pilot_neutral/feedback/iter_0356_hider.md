# Rehearsal feedback — iteration 356 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.27, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 40.0}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to away_from_opponent[yaw1,door] lock release -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
  role1 prep: grab box to box[align,door] release -> grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to away_from_opponent[yaw1,door] lock release -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.495
- hider win-rate: 0.45
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.53, "ramp_use": 0.03, "ramp_defense": 0.0}
- mean first-seen play step: 37.6
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.42, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.07, 0.54] | seeker 3 saw hider 0 at play step 45 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@7; prep0/1:dropped@8; prep1/0:done@29; prep1/1:dropped@30
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.19, 0.83] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:dropped@24; prep0/1:dropped@30; prep1/0:done@2; prep1/1:dropped@3; prep1/1:done@8; prep1/2:dropped@9; prep1/2:done@21
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.85, 0.87] | seeker 2 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@16; prep0/0:done@21; prep0/1:dropped@22; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@27; prep1/2:dropped@28; prep1/2:no_target@30
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.74, 1.87] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep0/1:no_target@22; prep1/0:done@5; prep1/1:dropped@6; prep1/1:done@13; prep1/2:dropped@14; prep1/2:no_target@21
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.91, 1.74] | seeker 3 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.17) | segments: prep0/0:done@14; prep0/1:dropped@15; prep1/0:done@17; prep1/1:dropped@18; prep1/1:dropped@22; prep1/1:dropped@26
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.21, 2.62] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep1/0:done@24; prep1/1:dropped@25; prep1/1:done@29; prep1/2:dropped@30
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[1.14, 1.12] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@11; prep0/0:done@16; prep0/1:dropped@17; prep0/1:done@27; prep1/0:done@11; prep1/1:dropped@12; prep1/1:done@19; prep1/2:dropped@20; prep1/2:done@28