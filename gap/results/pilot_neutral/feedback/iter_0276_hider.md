# Rehearsal feedback — iteration 276 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: segments then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: segments then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.598
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.7
- doors sealed+locked at prep end: 0.71, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.35, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.89, 0.73] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10; prep0/1:dropped@28; play0/0:dropped@32; play0/0:timeout@66; play0/1:dropped@67; prep1/0:dropped@25; prep1/0:done@26; prep1/1:dropped@27; prep1/1:no_target@28; play1/0:dropped@32; play1/0:done@41; play1/1:timeout@76; play1/2:dropped@77; play1/2:no_object@77
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.53, 0.15] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@4; prep0/1:dropped@5; prep0/1:dropped@7; play0/0:done@44; play0/1:timeout@79; prep1/0:done@10; prep1/1:dropped@11; prep1/1:no_target@12; play1/0:dropped@32; play1/0:timeout@66; play1/1:dropped@67
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.15, 1.34] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@23; prep0/1:dropped@24; prep0/1:no_target@25; play0/0:dropped@32; play0/0:timeout@66; play0/1:dropped@67; prep1/0:done@22; prep1/1:dropped@23; prep1/1:dropped@26; play1/0:done@36; play1/1:dropped@39; play1/1:dropped@47; play1/1:done@48
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.3, 2.26] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:done@21; play0/0:dropped@32; play0/0:timeout@66; play1/0:timeout@66; play1/1:dropped@67; play1/1:no_object@67
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[1.82, 0.62] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@9; prep0/0:done@15; prep0/1:dropped@16; play0/0:timeout@66; play0/1:dropped@67; play0/1:no_object@67; play0/2:no_object@68; prep1/0:done@11; prep1/1:dropped@12; prep1/1:done@22; play1/0:dropped@32; play1/0:no_object@32; play1/1:done@46
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.6, 0.02] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@2; prep0/1:dropped@3; play0/0:timeout@66; play0/1:dropped@67; prep1/0:dropped@26; play1/0:done@40; play1/1:timeout@75; play1/2:dropped@76; play1/2:no_object@76
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.43, 1.1] | seeker 2 saw hider 1 at play step 46 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep0/0:done@15; prep0/1:dropped@16; play0/0:timeout@66; play0/1:dropped@67; play0/1:no_object@67; play0/2:no_object@68; prep1/0:done@5; prep1/1:dropped@6; prep1/1:dropped@9; prep1/1:done@20; play1/0:dropped@32; play1/0:no_object@32; play1/1:timeout@67; play1/2:no_object@68
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.56, 2.42] | seeker 2 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:dropped@18; prep0/1:done@28; play0/0:dropped@32; play0/0:no_object@32; play0/1:done@46; prep1/0:done@16; prep1/1:dropped@17; prep1/1:no_target@21; play1/0:dropped@32; play1/0:done@40; play1/1:timeout@75; play1/2:dropped@76; play1/2:no_object@76