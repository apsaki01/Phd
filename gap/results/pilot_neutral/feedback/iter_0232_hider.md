# Rehearsal feedback — iteration 232 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: search then grab box to stay[yaw3,door] lock -> grab box to ramp_inside[target,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.576
- hider win-rate: 0.57
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.6, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 37.4
- doors sealed+locked at prep end: 0.68, ramp inside quadrant at prep end: 0.23
- seekers entered quadrant: 0.23, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.81, 0.7] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@15; prep0/1:dropped@16; prep0/1:no_target@18; prep1/0:done@13; prep1/1:dropped@14
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[2.64, 2.04] | seeker 3 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@27; prep0/1:dropped@28; prep0/1:done@31; prep1/0:dropped@7; prep1/0:dropped@9; prep1/0:done@23; prep1/1:dropped@24
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.62, 3.54] | seeker 2 saw hider 1 at play step 35 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep1/0:done@9; prep1/1:dropped@10; prep1/1:dropped@17; prep1/1:dropped@20
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.46, 1.1] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@22; prep1/1:dropped@23
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.93, 2.28] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@11; prep0/1:dropped@12; prep0/1:no_target@13; prep1/0:done@15; prep1/1:dropped@16; prep1/1:done@19
- p_door=1.00 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.2, 1.07] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@17; prep0/1:dropped@18; prep0/1:no_target@19; prep1/0:done@12; prep1/1:dropped@13
- p_door=0.25 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[1.26, 1.82] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; prep0/1:dropped@18; prep0/1:done@21; prep1/0:no_target@17; prep1/1:dropped@18
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.43, 1.46] | seeker 3 saw hider 0 at play step 36 (hider outside quadrant, seeker outside, seeker z=0.16) | segments: no segments executed