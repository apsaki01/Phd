# Rehearsal feedback — iteration 250 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> [when doors_sealed] grab box to wander[yaw2,direct] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.658
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.72, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 39.0
- doors sealed+locked at prep end: 0.78, ramp inside quadrant at prep end: 0.15
- seekers entered quadrant: 0.15, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.58, 1.84] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep0/1:done@23; prep1/0:done@16; prep1/1:dropped@17; prep1/1:dropped@19; prep1/1:dropped@21; prep1/1:done@29
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.86, 1.88] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@10; prep0/1:dropped@11; prep0/1:no_target@13; prep1/0:done@8; prep1/1:dropped@9
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.16, 2.46] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:done@18; prep1/0:done@15; prep1/1:dropped@16; prep1/1:done@20
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.75, 2.15] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@11; prep0/0:done@26; prep0/1:dropped@27; prep0/1:done@30
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.72, 0.6] | seeker 2 saw hider 1 at play step 51 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@25; prep0/1:dropped@26; prep0/1:done@29; prep1/0:no_target@23; prep1/1:dropped@24; prep1/1:no_target@28
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.43, 1.87] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@6; prep0/0:done@14; prep0/1:dropped@15; prep0/1:done@22; prep1/0:dropped@10; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@21
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.2, 0.73] | seeker 2 saw hider 1 at play step 55 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@10; prep0/1:done@13; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@17
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.74, 1.53] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@19; prep0/1:dropped@20; prep0/1:no_target@21; prep1/0:dropped@10; prep1/0:done@17; prep1/1:dropped@18; prep1/1:dropped@24