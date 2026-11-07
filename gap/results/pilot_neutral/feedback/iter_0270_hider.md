# Rehearsal feedback — iteration 270 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.540
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.55, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 35.3
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.28, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.89, 2.27] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:done@27; prep1/0:no_target@23; prep1/1:dropped@24; prep1/1:no_target@25
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.45, 2.06] | hiders never seen | segments: prep0/0:done@10; prep0/1:dropped@11; prep0/1:done@30; prep1/0:done@14; prep1/1:dropped@15; prep1/1:done@18
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.0, 1.83] | seeker 2 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.16) | segments: prep1/0:done@11; prep1/1:dropped@12; prep1/1:done@15
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.48, 1.6] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:done@15; prep1/0:done@15; prep1/1:dropped@16; prep1/1:done@22
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[1.09, 0.6] | seeker 3 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; prep0/1:dropped@11; prep0/1:done@17
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.38, 1.4] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@21; prep0/0:done@28; prep0/1:dropped@29; prep1/0:no_target@19; prep1/1:dropped@20; prep1/1:no_target@22
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.64, 1.7] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@17; prep0/1:dropped@18; prep0/1:no_target@19; prep1/0:dropped@12; prep1/0:done@18; prep1/1:dropped@19; prep1/1:done@23
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.79, 1.98] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@24; prep1/1:dropped@25; prep1/1:dropped@27