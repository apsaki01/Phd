# Rehearsal feedback — iteration 354 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.27, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 40.0}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to away_from_opponent[yaw1,door] lock release -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
  role1 prep: grab box to box[align,door] release -> grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to away_from_opponent[yaw1,door] lock release -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.681
- hider win-rate: 0.68
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.55, "ramp_use": 0.0, "ramp_defense": 0.06}
- mean first-seen play step: 38.9
- doors sealed+locked at prep end: 0.65, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.35, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.8, 1.69] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep0/1:dropped@22; prep0/1:no_target@23; prep1/0:done@12; prep1/1:dropped@13; prep1/1:done@17; prep1/2:dropped@18; prep1/2:done@26
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.6, 1.79] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@25; prep0/1:dropped@26; prep1/0:done@11; prep1/1:dropped@12; prep1/1:done@13; prep1/2:dropped@14; prep1/2:dropped@17; prep1/2:dropped@20; prep1/2:done@27
- p_door=0.75 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.47, 1.28] | seeker 3 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep0/1:no_target@17; prep1/0:done@4; prep1/1:dropped@5; prep1/1:dropped@8; prep1/1:done@11; prep1/2:dropped@12
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.38, 2.22] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:done@22; prep1/0:done@13; prep1/1:dropped@14; prep1/1:dropped@17; prep1/1:done@18; prep1/2:dropped@19; prep1/2:dropped@22
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.83, 2.27] | seeker 2 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@7; prep0/1:dropped@8; prep0/1:done@20; prep1/0:done@6; prep1/1:dropped@7; prep1/1:done@12; prep1/2:dropped@13; prep1/2:done@24
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.95, 1.53] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@12; prep1/1:dropped@13; prep1/1:dropped@19; prep1/1:done@26; prep1/2:dropped@27
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[1.3, 0.72] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; prep0/1:dropped@11; prep1/0:done@12; prep1/1:dropped@13; prep1/1:dropped@16
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.64, 1.95] | seeker 2 saw hider 1 at play step 52 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@13; prep0/0:done@15; prep0/1:dropped@16; prep0/1:dropped@18; prep1/0:done@7; prep1/1:dropped@8; prep1/1:done@13; prep1/2:dropped@14