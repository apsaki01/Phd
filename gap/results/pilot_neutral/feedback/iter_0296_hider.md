# Rehearsal feedback — iteration 296 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.75, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 39.53}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
  role1 prep: grab box to door_block[target,door] lock release -> grab box to climb[align,door] release | play: chase then grab box to ramp_inside[target,door] lock -> grab ramp to quadrant_interior[yaw2,direct] -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.550
- hider win-rate: 0.53
- behaviour detection rates: {"chasing": 0.05, "door_blocking": 0.55, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.0
- doors sealed+locked at prep end: 0.62, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.33, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.72, 2.06] | seeker 3 saw hider 1 at play step 42 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:dropped@9
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.27, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@26; prep1/1:dropped@27; prep1/1:no_object@27
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.95, 1.28] | seeker 3 saw hider 1 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@27; prep0/1:dropped@28; prep0/1:no_target@29; prep1/0:dropped@10; prep1/0:done@18; prep1/1:dropped@19; prep1/1:dropped@25; prep1/1:done@26
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.65, 0.28] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.9, 1.4] | seeker 2 saw hider 0 at play step 38 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@8; prep0/1:dropped@9; prep0/1:done@26; prep1/0:done@22; prep1/1:dropped@23; prep1/1:no_object@23
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.66, 0.81] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; prep0/1:dropped@7; prep0/1:done@25
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.96, 1.96] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.50 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.17, 1.53] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:done@28; prep1/0:done@19; prep1/1:dropped@20; prep1/1:no_object@20