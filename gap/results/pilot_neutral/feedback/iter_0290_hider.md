# Rehearsal feedback — iteration 290 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: segments then grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.567
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.06}
- mean first-seen play step: 39.5
- doors sealed+locked at prep end: 0.57, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.42, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[2.41, 0.63] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@28; prep0/1:dropped@29; prep0/1:no_target@30; prep1/0:dropped@16; prep1/0:dropped@19; prep1/0:done@24; prep1/1:dropped@25; play1/0:timeout@66
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.31, 1.8] | seeker 2 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep1/0:done@9; prep1/1:dropped@10; prep1/1:dropped@12; prep1/1:done@25; play1/0:dropped@32; play1/0:timeout@66
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.13, 0.17] | seeker 2 saw hider 1 at play step 59 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@4; prep0/1:dropped@5; play1/0:timeout@66
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.23, 0.4] | seeker 3 saw hider 1 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; prep0/1:dropped@7; prep0/1:done@21; prep1/0:done@9; prep1/1:dropped@10; prep1/1:done@23; play1/0:dropped@32; play1/0:no_object@32
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.55, 0.82] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:done@16; prep1/0:done@8; prep1/1:dropped@9; prep1/1:done@20; play1/0:dropped@32; play1/0:no_object@32
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[2.01, 1.92] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep0/0:done@15; prep0/1:dropped@16; prep0/1:dropped@19; prep1/0:done@8; prep1/1:dropped@9; prep1/1:done@18; play1/0:dropped@32; play1/0:no_object@32
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.94, 0.54] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@10; prep1/1:dropped@11; play1/0:timeout@66
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.12, 0.55] | seeker 3 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@5; prep0/1:dropped@6; prep0/1:no_target@30; prep1/0:done@25; prep1/1:dropped@26; prep1/1:dropped@28; play1/0:dropped@35; play1/0:timeout@66