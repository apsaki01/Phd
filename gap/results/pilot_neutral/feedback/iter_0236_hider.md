# Rehearsal feedback — iteration 236 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: chase then grab box to stay[yaw3,door] lock -> grab box to ramp_inside[target,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.672
- hider win-rate: 0.65
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.65, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 38.1
- doors sealed+locked at prep end: 0.72, ramp inside quadrant at prep end: 0.07
- seekers entered quadrant: 0.25, mean max seeker z: 0.17

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.69, 3.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@14; prep0/1:dropped@15; prep0/1:no_target@16; prep1/0:dropped@22; prep1/0:done@29; prep1/1:dropped@30
- p_door=0.50 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[2.56, 1.84] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@18; prep0/1:dropped@19; prep1/0:dropped@16
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.81, 0.19] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@21; prep0/1:dropped@22; prep0/1:no_target@24
- p_door=0.75 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.01, 1.83] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@17; prep0/1:dropped@18; prep0/1:done@26; prep1/0:done@17; prep1/1:dropped@18; prep1/1:done@21
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=True boxes_moved=[1.2, 0.97] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep0/1:done@17; prep1/0:dropped@11
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=False boxes_moved=[2.41, 0.89] | hiders never seen | segments: prep0/0:done@26; prep0/1:dropped@27; prep0/1:done@30; prep1/0:dropped@9; prep1/0:done@10; prep1/1:dropped@11; prep1/1:done@27
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.49, 0.74] | seeker 2 saw hider 1 at play step 39 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.4, 1.51] | seeker 3 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@27; prep0/1:dropped@28; prep0/1:done@31; prep1/0:dropped@11; prep1/0:dropped@16; prep1/0:done@29; prep1/1:dropped@30