# Rehearsal feedback — iteration 240 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: chase then grab box to stay[yaw3,door] lock -> grab box to ramp_inside[target,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw1,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.591
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.1, "door_blocking": 0.7, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.4
- doors sealed+locked at prep end: 0.74, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.17, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.67, 3.11] | seeker 3 saw hider 1 at play step 37 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; prep0/1:dropped@7; prep0/1:done@22; prep1/0:no_target@10; prep1/1:dropped@11; prep1/1:no_target@19
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.41, 0.45] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@15; prep0/0:done@23; prep0/1:dropped@24; prep0/1:done@30; prep1/0:no_target@17; prep1/1:dropped@18; prep1/1:no_target@22
- p_door=0.50 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.26, 1.15] | seeker 3 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@21; prep1/0:done@22; prep1/1:dropped@23; prep1/1:done@26
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.0, 2.02] | seeker 2 saw hider 0 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.64) | segments: prep0/0:no_target@18; prep0/1:dropped@19; prep0/1:no_target@20; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.86, 2.17] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@24; prep1/1:dropped@25
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.37, 0.47] | seeker 3 saw hider 0 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@13; prep0/1:dropped@14; prep0/1:no_target@15; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@17
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.01, 2.31] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@2; prep0/0:dropped@9; prep0/0:dropped@12
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.87, 0.76] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9