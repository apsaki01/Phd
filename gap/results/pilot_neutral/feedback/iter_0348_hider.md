# Rehearsal feedback — iteration 348 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 38.08}
  role0 prep: grab box to climb[yaw1,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,direct] lock -> grab ramp to quadrant_interior[align,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.578
- hider win-rate: 0.55
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.1
- doors sealed+locked at prep end: 0.74, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.30, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.24, 1.05] | seeker 3 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep1/0:done@14; prep1/1:dropped@15
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.55, 0.85] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@13; prep0/0:dropped@15; prep1/0:done@11; prep1/1:dropped@12
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.45, 1.33] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:done@26; prep1/0:done@27; prep1/1:dropped@28; prep1/1:no_target@29
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.14, 0.82] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep0/1:done@28; prep1/0:done@26; prep1/1:dropped@27; prep1/1:no_target@28
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.44, 1.22] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@16; prep0/0:dropped@20; prep0/0:done@30; prep0/1:dropped@31; prep1/0:done@17; prep1/1:dropped@18; prep1/1:done@31
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.96, 0.98] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:dropped@22; prep0/1:done@29; prep1/0:done@15; prep1/1:dropped@16; prep1/1:dropped@26
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.79, 1.66] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@18; prep0/1:dropped@19; prep0/1:done@30; prep1/0:done@20; prep1/1:dropped@21
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.71, 1.05] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@12; prep1/0:dropped@19; prep1/0:done@22; prep1/1:dropped@23