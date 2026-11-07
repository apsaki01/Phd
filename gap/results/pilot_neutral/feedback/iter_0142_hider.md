# Rehearsal feedback — iteration 142 — learning team: hider

## Current graph
```
assign=fixed params={'gain': 4.7, 'damp': 0.52, 'tol': 0.33, 'offset': 0.16, 'seg_timeout': 38.83}
  role0 prep: grab box to climb[yaw3,door] release -> [when opponent_visible] grab ramp to climb[target,door] lock -> [when ramp_inside] grab ramp to climb[align,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
  role1 prep: [when ramp_inside] grab ramp to climb[yaw0,door] release | play: segments then grab box to outside_wall[align,door] -> to stay[yaw0,door] release -> grab box to stay[yaw3,door] lock
```

## Aggregate (n=40 instances)
- hider objective J (fraction of play steps all hiders hidden): 0.232
- hider win-rate: 0.20
- behaviour detection rates: {"chasing": 0.15, "door_blocking": 0.0, "ramp_use": 0.0, "ramp_defense": 0.0}
- mean first-seen play step: 34.3
- doors sealed+locked at prep end: 0.00, ramp inside quadrant at prep end: 0.12
- seekers entered quadrant: 0.65, mean max seeker z: 0.23

## Failure analysis (lost instances)
- p_door=0.25 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.73, 0.0] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@9; prep0/1:dropped@14; play0/0:done@37; play0/1:timeout@76; play0/2:dropped@77; play1/0:done@56
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 1.51] | seeker 2 saw hider 0 at play step 35 (hider inside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; play0/0:dropped@32; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:timeout@70; play1/1:done@71
- p_door=0.75 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.0, 1.1] | seeker 3 saw hider 1 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@21; play0/0:dropped@32; play0/0:dropped@52; play0/0:dropped@66; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:dropped@63; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71
- p_door=0.25 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.79, 0.0] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@6; prep0/1:dropped@8; play0/0:done@41; play1/0:done@58
- p_door=1.00 doors=1 sealed=[False] ramp_inside=False boxes_moved=[1.45, 0.28] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; play0/0:dropped@39; play0/0:timeout@70; play0/1:dropped@71; play0/1:done@71; play1/0:done@56
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[1.3, 0.02] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@14; prep0/1:dropped@15; prep0/1:dropped@30; play0/0:done@38; play0/1:dropped@40; play0/1:done@40; play0/2:timeout@79; play1/0:done@51
- p_door=0.00 doors=2 sealed=[False, False] ramp_inside=False boxes_moved=[0.97, 0.89] | seeker 3 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:dropped@13; prep0/0:done@18; prep0/1:dropped@19; play0/0:done@47; play1/0:done@65
- p_door=0.50 doors=1 sealed=[False] ramp_inside=False boxes_moved=[0.05, 0.58] | seeker 2 saw hider 0 at play step 33 (hider outside quadrant, seeker outside, seeker z=0.15) | segments: prep0/0:done@16; prep0/1:dropped@17; play0/0:done@40; play0/1:dropped@43; play0/1:done@43; play1/0:timeout@70; play1/1:dropped@71; play1/1:done@71