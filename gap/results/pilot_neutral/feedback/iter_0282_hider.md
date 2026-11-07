# Rehearsal feedback — iteration 282 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,door] lock -> grab ramp to quadrant_interior[yaw2,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: segments then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.569
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 40.4
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.45, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.38, 0.72] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep0/0:dropped@17; play1/0:done@56; play1/1:dropped@59; play1/1:done@65
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.0, 2.03] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep0/1:dropped@19; prep0/1:no_target@20; prep1/0:done@2; prep1/1:dropped@3; prep1/1:dropped@6; play1/0:timeout@66; play1/1:dropped@67
- p_door=0.75 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[0.9, 1.57] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@4; prep0/1:dropped@5; prep0/1:done@15; prep1/0:dropped@30; play1/0:done@38; play1/1:timeout@73; play1/2:dropped@74; play1/2:no_object@74
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.11, 1.5] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep0/1:dropped@17; prep0/1:dropped@20; prep0/1:done@29; play1/0:done@42; play1/1:timeout@77; play1/2:dropped@78; play1/2:no_object@78
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.15, 1.29] | seeker 3 saw hider 1 at play step 50 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@4; prep0/1:dropped@5; prep0/1:done@13; prep1/0:done@4; prep1/1:dropped@5; play1/0:dropped@34; play1/0:done@45
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.88, 0.63] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10; prep0/1:done@24; prep1/0:dropped@22; prep1/0:done@23; prep1/1:dropped@24; play1/0:done@39; play1/1:timeout@74; play1/2:dropped@75; play1/2:no_object@75
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.12, 1.53] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:no_target@22; prep1/0:done@18; prep1/1:dropped@19; play1/0:done@45
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.73, 2.27] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; prep0/1:dropped@23; prep1/0:dropped@16; prep1/0:done@19; prep1/1:dropped@20; play1/0:done@41; play1/1:timeout@76; play1/2:dropped@77