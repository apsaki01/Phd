# Rehearsal feedback — iteration 272 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock release | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.643
- hider win-rate: 0.62
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.06}
- mean first-seen play step: 36.4
- doors sealed+locked at prep end: 0.69, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.20, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.19, 2.03] | seeker 2 saw hider 1 at play step 42 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10; prep0/1:dropped@16; prep0/1:done@27
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.14, 2.48] | seeker 2 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@17; prep0/1:dropped@18; prep0/1:no_target@19; prep1/0:dropped@13; prep1/0:dropped@17; prep1/0:done@26; prep1/1:dropped@27
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.04, 0.16] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@29; prep0/1:dropped@30; prep1/0:done@26; prep1/1:dropped@27; prep1/1:done@30
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[1.41, 1.25] | seeker 3 saw hider 1 at play step 44 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@11; prep1/0:done@8; prep1/1:dropped@9; prep1/1:done@12
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.16, 0.95] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep1/0:no_target@21; prep1/1:dropped@22; prep1/1:no_target@26
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.81, 2.34] | seeker 2 saw hider 1 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@11; prep0/1:dropped@12; prep0/1:no_target@13
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.37, 1.44] | seeker 2 saw hider 0 at play step 40 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:dropped@14; prep1/0:done@16; prep1/1:dropped@17; prep1/1:done@20
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.9, 0.5] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@3