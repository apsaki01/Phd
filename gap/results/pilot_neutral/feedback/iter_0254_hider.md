# Rehearsal feedback — iteration 254 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> [when doors_sealed] grab box to wander[yaw2,direct] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.475
- hider win-rate: 0.45
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.62, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.6
- doors sealed+locked at prep end: 0.72, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.28, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.7, 2.52] | seeker 3 saw hider 0 at play step 34 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@13; prep0/1:dropped@14; prep0/1:no_target@15; prep1/0:done@17; prep1/1:dropped@18; prep1/1:done@21
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.03, 1.2] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:done@14; prep1/0:no_target@4; prep1/1:dropped@5; prep1/1:no_target@6
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.32, 2.41] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@24; prep0/1:dropped@25; prep0/1:done@28; prep1/0:done@22; prep1/1:dropped@23; prep1/1:done@29
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.18, 0.25] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@13; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.1, 1.85] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:done@24
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.49, 0.77] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@28; prep0/1:dropped@29; prep0/1:no_target@30
- p_door=0.75 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.98, 0.56] | seeker 2 saw hider 0 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@7; prep0/1:dropped@8; prep0/1:no_target@10; prep1/0:dropped@5; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@17
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.65, 1.02] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep0/1:done@22; prep1/0:done@18; prep1/1:dropped@19; prep1/1:done@22