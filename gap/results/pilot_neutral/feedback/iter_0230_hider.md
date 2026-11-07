# Rehearsal feedback — iteration 230 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: go(ramp_inside,door) then grab box to stay[yaw3,door] lock -> grab box to ramp_inside[target,door] lock -> to door_inside[yaw2,direct] release
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: go(ramp_inside,door) then grab box to stay[yaw3,door] lock -> grab box to ramp_inside[target,door] lock -> to door_inside[yaw2,direct] release
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.521
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.23, "door_blocking": 0.57, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 35.1
- doors sealed+locked at prep end: 0.61, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.35, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=True boxes_moved=[0.33, 0.23] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.31, 0.27] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@14; prep1/0:done@21; prep1/1:dropped@22
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.36, 1.27] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@15; prep0/1:dropped@16; prep0/1:done@19; prep1/0:done@25; prep1/1:dropped@26; prep1/1:done@31
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.54, 0.68] | seeker 3 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:done@16; prep1/0:done@13; prep1/1:dropped@14; prep1/1:done@17
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 0.0] | seeker 2 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=1.00 doors=1 sealed=[True] ramp_inside=False boxes_moved=[2.03, 1.69] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker inside, seeker z=0.15) | segments: prep0/0:no_target@17; prep0/1:dropped@18; prep0/1:no_target@21; prep1/0:done@18; prep1/1:dropped@19; prep1/1:done@22
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.62, 2.57] | seeker 3 saw hider 1 at play step 41 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@6; prep0/1:dropped@7; prep0/1:no_target@18
- p_door=0.00 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[1.34, 1.21] | seeker 2 saw hider 1 at play step 50 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@12; prep0/1:dropped@13; prep0/1:done@16; prep1/0:dropped@13; prep1/0:done@18; prep1/1:dropped@19; prep1/1:done@25