# Rehearsal feedback — iteration 248 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: stay then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.508
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.17, "door_blocking": 0.53, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 36.2
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.30
- seekers entered quadrant: 0.17, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.51, 1.31] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep1/0:no_target@12; prep1/1:dropped@13; prep1/1:done@26
- p_door=0.50 doors=1 sealed=[True] ramp_inside=True boxes_moved=[0.3, 0.48] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@10; prep0/1:dropped@11; prep0/1:done@17; prep1/0:no_target@8; prep1/1:dropped@9; prep1/1:no_target@10
- p_door=0.50 doors=1 sealed=[False] ramp_inside=True boxes_moved=[0.53, 0.44] | seeker 2 saw hider 1 at play step 34 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:no_target@17; prep1/1:dropped@18; prep1/1:no_target@22
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.45, 1.34] | seeker 2 saw hider 0 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@17; prep0/1:dropped@18; prep0/1:no_target@19; prep1/0:done@15; prep1/1:dropped@16; prep1/1:done@22
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.95, 1.67] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@13; prep0/1:dropped@14; prep0/1:no_object@26; prep1/0:done@11; prep1/1:dropped@12; prep1/1:done@30
- p_door=0.75 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[2.1, 1.9] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; prep0/1:dropped@22; prep0/1:done@25
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.73, 1.36] | seeker 2 saw hider 0 at play step 40 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep0/1:done@23; prep1/0:done@8; prep1/1:dropped@9; prep1/1:done@12
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.71, 1.01] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@15; prep0/1:dropped@16; prep0/1:no_target@17