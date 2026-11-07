# Rehearsal feedback — iteration 268 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.511
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.62, "ramp_use": 0.03, "ramp_defense": 0.03}
- mean first-seen play step: 36.7
- doors sealed+locked at prep end: 0.71, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.30, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.15, 1.38] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep1/0:done@12; prep1/1:dropped@13; prep1/1:done@16
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[1.63, 1.95] | seeker 2 saw hider 1 at play step 40 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@17; prep1/0:done@15; prep1/1:dropped@16; prep1/1:done@19
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.63, 2.08] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@10; prep0/0:dropped@13; prep1/0:no_target@18; prep1/1:dropped@19; prep1/1:no_target@21
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.87, 2.18] | hiders never seen | segments: prep0/0:no_target@15; prep0/1:dropped@16; prep0/1:no_target@17; prep1/0:done@11; prep1/1:dropped@12; prep1/1:dropped@20; prep1/1:done@28
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.92, 1.99] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; prep0/1:done@20; prep1/0:done@23; prep1/1:dropped@24; prep1/1:done@27
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.73, 1.77] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:done@20; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.84, 0.64] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@11; prep0/1:dropped@12; prep0/1:no_target@16; prep1/0:dropped@8
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.19, 0.67] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; prep0/1:dropped@18; prep0/1:done@21; prep1/0:dropped@8; prep1/0:done@14; prep1/1:dropped@15; prep1/1:done@18