# Rehearsal feedback — iteration 350 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.61, 'damp': 0.75, 'tol': 0.25, 'offset': 0.0, 'seg_timeout': 40.0}
  role0 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
  role1 prep: grab box to climb[align,door] release -> grab box to door_block[target,door] lock release | play: flee then grab box to ramp_inside[target,door] lock -> to quadrant_interior[align,direct] -> grab box to stay[yaw3,direct] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.645
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.12, "door_blocking": 0.57, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 35.9
- doors sealed+locked at prep end: 0.69, ramp inside quadrant at prep end: 0.17
- seekers entered quadrant: 0.33, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 1.21] | seeker 2 saw hider 0 at play step 36 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@5; prep0/1:dropped@6; prep0/1:dropped@8
- p_door=0.50 doors=2 sealed=[True, False] ramp_inside=True boxes_moved=[1.24, 2.3] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep0/1:dropped@19; prep1/0:done@6; prep1/1:dropped@7; prep1/1:done@23
- p_door=0.00 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[0.32, 1.64] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@8; prep1/1:dropped@9; prep1/1:done@27
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.42, 0.54] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@7; prep0/1:dropped@8; prep0/1:done@15; prep1/0:done@9; prep1/1:dropped@10; prep1/1:done@17
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.09, 0.22] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@19; prep0/1:dropped@20; prep1/0:done@15; prep1/1:dropped@16
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.21, 0.47] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; prep0/1:dropped@7; prep0/1:done@18; prep1/0:dropped@8; prep1/0:dropped@11; prep1/0:done@12; prep1/1:dropped@13; prep1/1:no_target@15
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.49, 1.37] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@18; prep1/0:done@17; prep1/1:dropped@18; prep1/1:dropped@26
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.59, 1.06] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@11; prep0/1:dropped@12; prep0/1:dropped@21; prep0/1:dropped@27; prep0/1:dropped@30; prep1/0:done@28; prep1/1:dropped@29; prep1/1:no_target@30