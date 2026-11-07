# Rehearsal feedback — iteration 238 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: chase then grab box to stay[yaw3,door] lock -> grab box to ramp_inside[target,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.529
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.2, "door_blocking": 0.68, "ramp_use": 0.0, "ramp_defense": 0.06}
- mean first-seen play step: 38.7
- doors sealed+locked at prep end: 0.72, ramp inside quadrant at prep end: 0.20
- seekers entered quadrant: 0.28, mean max seeker z: 0.18

## Failure analysis (lost instances)
- p_door=0.25 doors=1 sealed=[False] ramp_inside=True boxes_moved=[1.48, 0.63] | seeker 2 saw hider 1 at play step 46 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@30; prep0/1:dropped@31; prep1/0:no_target@20; prep1/1:dropped@21; prep1/1:no_target@22
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.13, 0.86] | seeker 2 saw hider 1 at play step 42 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@20; prep0/1:dropped@21; prep0/1:done@24; prep1/0:no_target@21; prep1/1:dropped@22; prep1/1:no_target@23
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.38, 1.9] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; prep0/1:dropped@23; prep0/1:done@26; prep1/0:done@20; prep1/1:dropped@21; prep1/1:done@24
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.65] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.75 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.28, 1.89] | hiders never seen | segments: prep0/0:no_target@19; prep0/1:dropped@20; prep0/1:no_target@23; prep1/0:done@22; prep1/1:dropped@23; prep1/1:done@26
- p_door=1.00 doors=1 sealed=[True] ramp_inside=True boxes_moved=[1.19, 1.24] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@8; prep0/1:dropped@9; prep0/1:no_target@10; prep1/0:done@21; prep1/1:dropped@22; prep1/1:done@25
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.0, 0.42] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@6; prep0/1:dropped@7; prep0/1:done@18
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[0.94, 1.88] | hiders never seen | segments: prep0/0:done@16; prep0/1:dropped@17; prep0/1:done@20; prep1/0:no_target@10; prep1/1:dropped@11; prep1/1:dropped@14; prep1/1:done@26