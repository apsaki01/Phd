# Rehearsal feedback — iteration 346 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 38.08}
  role0 prep: grab box to climb[yaw1,door] release -> grab box to door_block[target,door] lock release | play: flee then [when ramp_inside] to away_from_opponent[yaw2,direct] lock release -> grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,direct] lock -> grab ramp to quadrant_interior[align,direct]
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.653
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 37.4
- doors sealed+locked at prep end: 0.65, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.30, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.89, 1.89] | seeker 3 saw hider 1 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@18; prep1/0:done@20; prep1/1:dropped@21
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.07, 0.57] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@2; prep1/1:dropped@3
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.3, 1.02] | seeker 3 saw hider 1 at play step 48 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10; prep0/1:done@17; prep1/0:done@14; prep1/1:dropped@15; prep1/1:dropped@17
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.66, 1.9] | seeker 2 saw hider 0 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:done@20; prep1/0:done@10; prep1/1:dropped@11; prep1/1:done@21
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.26, 0.53] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; prep0/1:dropped@7; prep0/1:dropped@26; prep1/0:done@13; prep1/1:dropped@14; prep1/1:no_target@30
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.21, 1.35] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@20; prep0/0:dropped@26
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.59, 1.58] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep1/0:done@22; prep1/1:dropped@23
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.35, 0.77] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:no_target@22; prep1/0:done@15; prep1/1:dropped@16; prep1/1:done@26