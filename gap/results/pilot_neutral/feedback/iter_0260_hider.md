# Rehearsal feedback — iteration 260 — learning team: hider

## Current graph
```
assign=nearest_object params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.660
- hider win-rate: 0.70
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 36.3
- doors sealed+locked at prep end: 0.71, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.28, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.83, 1.42] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:no_target@24; prep1/1:dropped@25; prep1/1:no_target@26
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.84, 1.31] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; prep1/0:done@24; prep1/1:dropped@25; prep1/1:done@30
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.92, 0.58] | seeker 3 saw hider 1 at play step 34 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:no_target@22; prep0/1:dropped@23; prep0/1:no_target@27; prep1/0:done@21; prep1/1:dropped@22; prep1/1:done@26
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.56, 0.98] | seeker 3 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep0/1:done@27; prep1/0:no_target@15; prep1/1:dropped@16; prep1/1:no_target@17
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.98, 1.88] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@21; prep1/0:dropped@24; prep1/0:dropped@30
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.03, 0.22] | seeker 3 saw hider 1 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@24; prep0/1:dropped@25; prep0/1:no_target@27; prep1/0:dropped@15
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.96, 2.17] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; prep0/1:dropped@23; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[2.15, 0.35] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep0/1:dropped@19; prep0/1:done@22; prep1/0:no_target@13; prep1/1:dropped@14; prep1/1:no_target@15