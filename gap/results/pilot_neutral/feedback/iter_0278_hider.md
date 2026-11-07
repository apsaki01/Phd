# Rehearsal feedback — iteration 278 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,door] lock -> grab ramp to quadrant_interior[yaw2,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: segments then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.642
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 41.1
- doors sealed+locked at prep end: 0.72, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.25, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.83, 1.3] | seeker 3 saw hider 1 at play step 44 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@4; prep1/1:dropped@5; play1/0:done@46; play1/1:done@58
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.01, 2.05] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep1/0:done@27; prep1/1:dropped@28; play1/0:done@47; play1/1:done@53
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.73, 1.31] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep1/0:done@29; prep1/1:dropped@30; prep1/1:no_target@31; play1/0:dropped@32; play1/0:done@40; play1/1:timeout@75; play1/2:dropped@76
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.91, 0.1] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@5; prep1/1:dropped@6; prep1/1:done@21; play1/0:dropped@32; play1/0:no_object@32; play1/1:timeout@67; play1/2:no_object@68
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.42, 1.26] | seeker 2 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:dropped@23; prep1/0:done@22; prep1/1:dropped@23; prep1/1:no_target@24; play1/0:dropped@32; play1/0:done@43; play1/1:timeout@78; play1/2:dropped@79
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.23, 1.07] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@29; prep0/1:dropped@30; prep1/0:done@13; prep1/1:dropped@14; prep1/1:dropped@16; play1/0:timeout@66; play1/1:dropped@67
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.38, 0.55] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@9; prep1/1:dropped@10; prep1/1:no_target@18; play1/0:dropped@32; play1/0:dropped@34; play1/0:done@47
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.57, 2.2] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@19; prep0/0:done@20; prep0/1:dropped@21; prep0/1:dropped@24; prep1/0:dropped@16; prep1/0:done@21; prep1/1:dropped@22; play1/0:timeout@66; play1/1:dropped@67