# Rehearsal feedback — iteration 340 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 38.08}
  role0 prep: grab box to climb[yaw1,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,direct] lock -> grab ramp to quadrant_interior[align,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.620
- hider win-rate: 0.60
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.55, "ramp_use": 0.0, "ramp_defense": 0.08}
- mean first-seen play step: 36.1
- doors sealed+locked at prep end: 0.64, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.35, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.05, 1.19] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@15; prep0/0:done@22; prep0/1:dropped@23; prep1/0:done@14; prep1/1:dropped@15; prep1/1:dropped@17
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.05, 1.21] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep1/0:dropped@7; prep1/0:done@14; prep1/1:dropped@15
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.62, 1.23] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep0/1:no_target@21; prep1/0:done@7; prep1/1:dropped@8
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.52, 0.63] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@4; prep0/1:dropped@5
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.12, 1.74] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; prep0/1:no_target@18; prep1/0:done@10; prep1/1:dropped@11; prep1/1:done@21
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.54, 0.0] | seeker 3 saw hider 1 at play step 51 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep1/0:done@2; prep1/1:dropped@3; prep1/1:no_target@5
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.51, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@5; prep0/1:dropped@6; prep0/1:no_target@7
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.96, 0.83] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:dropped@16; prep1/0:done@17; prep1/1:dropped@18