# Rehearsal feedback — iteration 234 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 5.2, 'damp': 0.8, 'tol': 0.25, 'offset': 0.06, 'seg_timeout': 34.2}
  role0 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: chase then grab box to stay[yaw3,door] lock -> grab box to ramp_inside[target,door] lock
  role1 prep: grab box to door_block[align,door] release -> grab box to door_block[target,door] lock | play: go(ramp_inside,door) then grab box to ramp_inside[target,door] lock -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.492
- hider win-rate: 0.50
- behaviour detection rates: {"chasing": 0.23, "door_blocking": 0.55, "ramp_use": 0.0, "ramp_defense": 0.03}
- mean first-seen play step: 36.5
- doors sealed+locked at prep end: 0.64, ramp inside quadrant at prep end: 0.25
- seekers entered quadrant: 0.20, mean max seeker z: 0.16

## Failure analysis (lost instances)
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[2.05, 1.08] | seeker 2 saw hider 1 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:no_target@11; prep0/1:dropped@12; prep0/1:no_target@13; prep1/0:done@8; prep1/1:dropped@9
- p_door=0.50 doors=1 sealed=[True] ramp_inside=False boxes_moved=[1.8, 0.57] | hiders never seen | segments: prep0/0:no_target@15; prep0/1:dropped@16; prep0/1:no_target@19; prep1/0:done@21; prep1/1:dropped@22; prep1/1:done@25
- p_door=0.75 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.18, 0.37] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.61, 1.48] | seeker 2 saw hider 0 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: no segments executed
- p_door=0.25 doors=2 sealed=[True, True] ramp_inside=True boxes_moved=[0.78, 2.27] | seeker 2 saw hider 0 at play step 37 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@13; prep0/1:dropped@14; prep0/1:done@17; prep1/0:done@21; prep1/1:dropped@22; prep1/1:done@25
- p_door=0.00 doors=2 sealed=[True, False] ramp_inside=False boxes_moved=[0.59, 1.77] | seeker 3 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@22; prep0/1:dropped@23; prep0/1:done@26; prep1/0:dropped@22
- p_door=0.25 doors=2 sealed=[False, True] ramp_inside=False boxes_moved=[1.24, 0.26] | seeker 2 saw hider 1 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@31; prep1/0:done@23; prep1/1:dropped@24; prep1/1:done@27
- p_door=0.25 doors=1 sealed=[True] ramp_inside=False boxes_moved=[0.0, 1.38] | seeker 2 saw hider 1 at play step 33 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep1/0:done@6; prep1/1:dropped@7; prep1/1:done@10