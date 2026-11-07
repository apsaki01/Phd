# Rehearsal feedback — iteration 286 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,door] lock -> grab ramp to quadrant_interior[yaw2,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: segments then grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.647
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.3, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 43.5
- doors sealed+locked at prep end: 0.71, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.28, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.25, 0.84] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; prep0/1:dropped@18; prep0/1:done@28; prep1/0:done@5; prep1/1:dropped@6; prep1/1:done@13; play1/0:dropped@32; play1/0:timeout@66; play1/1:no_object@67
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.94, 0.87] | seeker 2 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:dropped@15; prep1/0:done@29; prep1/1:dropped@30; play1/0:timeout@66
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.99, 1.64] | seeker 2 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep1/0:done@10; prep1/1:dropped@11; prep1/1:done@20; play1/0:dropped@32; play1/0:timeout@66
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.79, 0.9] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@22; prep1/0:done@13; prep1/1:dropped@14; play1/0:done@32; play1/1:timeout@67
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.13, 0.72] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:done@26; prep1/0:done@9; prep1/1:dropped@10; prep1/1:done@27; play1/0:dropped@32; play1/0:timeout@66; play1/1:no_object@67
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.41, 1.97] | seeker 3 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@5; prep0/1:dropped@6; prep0/1:done@16; prep1/0:done@15; prep1/1:dropped@16; prep1/1:no_target@24; play1/0:dropped@32; play1/0:timeout@66; play1/1:dropped@74
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.31, 1.59] | seeker 3 saw hider 1 at play step 51 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; prep0/1:dropped@18; prep0/1:done@24; prep1/0:done@15; prep1/1:dropped@16; prep1/1:done@27; play1/0:dropped@32; play1/0:timeout@66; play1/1:no_object@67
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.95, 0.86] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@13; prep0/0:done@25; prep0/1:dropped@26; prep1/0:done@10; prep1/1:dropped@11; prep1/1:done@18; play1/0:dropped@32; play1/0:done@43; play1/1:timeout@78